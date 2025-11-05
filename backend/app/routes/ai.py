from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.db.session import get_session
from app.models.user import User
from app.models.project import Project
from app.ai.preprocess import clean_skills

router = APIRouter(prefix="/ai", tags=["AI Matching"])

@router.post("/match/{user_id}")
async def match_user_projects(
    user_id: int,
    db: AsyncSession = Depends(get_session)
):
    # Get the user by ID
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get all projects
    result = await db.execute(select(Project))
    projects = result.scalars().all()

    if not projects:
        raise HTTPException(status_code=404, detail="No projects available")

    # Preprocess data
    user_skills_cleaned = clean_skills(user.skills)
    project_skills_cleaned = [clean_skills(p.required_skills) for p in projects]

    # Vectorization
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user_skills_cleaned] + project_skills_cleaned)

    # Calculate similarity
    user_vector = vectors[0]
    project_vectors = vectors[1:]
    similarities = cosine_similarity(user_vector, project_vectors).flatten()

    # Prepare results
    results = []
    for idx, project in enumerate(projects):
        # Ensure skills are compared as lowercase strings
        matched_skills = list(
            set(map(str.lower, user.skills)) &
            set(map(str.lower, project.required_skills))
        )
        results.append({
            "project_id": project.id,
            "project_name": project.name,
            "similarity_score": float(similarities[idx]),
            "matched_skills": matched_skills
        })

    # Sort by similarity
    sorted_results = sorted(results, key=lambda x: x["similarity_score"], reverse=True)

    return {
        "user_id": user_id,
        "matches": sorted_results
    }
