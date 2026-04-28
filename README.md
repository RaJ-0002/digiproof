# Digiproof.AI - AI-Driven Talent Matching Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![React](https://img.shields.io/badge/React-18.x-blue.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.x-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.x-blue.svg)](https://www.postgresql.org/)

## 🎯 Overview

Digiproof.AI is an innovative AI-driven talent-matching platform that revolutionizes how students connect with real-world opportunities. By combining advanced machine learning algorithms with blockchain-backed credential verification, we bridge the gap between education and employment.

### Key Features

- 🤖 **AI-Powered Matching**: Intelligent skill-based matching connecting students with suitable projects
- 🎓 **Smart Profile Creation**: Automated skill inference from academic records
- 🔐 **Blockchain Verification**: Immutable credential verification system
- 📊 **Analytics Dashboard**: Comprehensive insights for institutions and employers
- 📱 **Responsive Design**: Seamless experience across all devices
- 🔒 **Secure Architecture**: OAuth 2.0 authentication with role-based access control

## 🚀 Quick Start

### Prerequisites

- Node.js 18.x or higher
- Python 3.10 or higher
- PostgreSQL 15.x or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-organization/digiproof-ai.git
   cd digiproof-ai
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Database Setup**
   ```bash
   # Create PostgreSQL database
   createdb digiproof_db
   
   # Run migrations
   cd backend
   alembic upgrade head
   ```

5. **Environment Configuration**
   
   Create `.env` file in the backend directory:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/digiproof_db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```

   Create `.env` file in the frontend directory:
   ```env
   REACT_APP_API_URL=http://localhost:8000/api/v1
   ```

### Running the Application

**Backend Server**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

**Frontend Development Server**
```bash
cd frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 📁 Project Structure

```
digiproof-ai/
├── backend/
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   ├── core/             # Core configuration
│   │   ├── models/           # Database models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   └── ml/               # Machine learning components
│   ├── tests/                # Backend tests
│   ├── alembic/              # Database migrations
│   ├── requirements.txt      # Python dependencies
│   └── main.py               # Application entry point
├── frontend/
│   ├── public/               # Static files
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/            # Page components
│   │   ├── services/         # API service layer
│   │   ├── utils/            # Utility functions
│   │   └── App.js            # Main application component
│   ├── package.json          # Node dependencies
│   └── tailwind.config.js    # Tailwind CSS configuration
├── docs/                     # Documentation
├── scripts/                  # Utility scripts
└── README.md                 # This file
```

## 🛠️ Technology Stack

### Frontend
- **Framework**: React 18.x
- **Styling**: Tailwind CSS
- **State Management**: React Context API
- **HTTP Client**: Axios
- **UI Components**: Custom component library

### Backend
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: OAuth 2.0 with JWT
- **API Documentation**: OpenAPI (Swagger)

### AI/ML
- **Library**: scikit-learn
- **Algorithms**: Hybrid recommendation system (collaborative + content-based filtering)
- **Feature Engineering**: Custom pipeline for skill extraction and matching

### DevOps
- **Version Control**: Git & GitHub
- **CI/CD**: GitHub Actions
- **Deployment**: Vercel (Frontend), Docker (Backend)
- **Monitoring**: (To be implemented)

## 🔧 Development

### Code Style

We follow industry-standard coding conventions:

**Python (Backend)**
- PEP 8 style guide
- Google Python Style Guide for docstrings
- Black for code formatting
- Pylint for linting

**JavaScript (Frontend)**
- ESLint with Airbnb configuration
- Prettier for code formatting

### Running Tests

**Backend Tests**
```bash
cd backend
pytest tests/ -v --cov=app
```

**Frontend Tests**
```bash
cd frontend
npm test
```

### Database Migrations

Create a new migration:
```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migration:
```bash
alembic downgrade -1
```

## 📊 API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Key Endpoints

```
POST   /api/v1/auth/register          # User registration
POST   /api/v1/auth/login             # User login
GET    /api/v1/profiles/me            # Get current user profile
POST   /api/v1/profiles               # Create profile
GET    /api/v1/projects               # List projects
POST   /api/v1/projects               # Create project
GET    /api/v1/matches                # Get AI-generated matches
POST   /api/v1/credentials/verify     # Verify blockchain credential
```

## 👥 Team

### Leadership
- **Team Lead**: Rajesh Avula
- **Deputy Team Lead**: Ume Habiba

### Development Teams

**UI/UX Design & Frontend**
- Saroj Basnet
- Sanjay Kumar Krishna Murthy
- Vineeth Venkata Krishna Akurathi
- Amritha Nandakumar
- Rajesh Avula

**Backend APIs & Database**
- Saroj Basnet
- Ume Habiba
- Samuel Toba Oshagbami
- Rajesh Avula

**AI Matching Engine**
- S.N. Aishwarya Devi Akula
- Inye Fredrick Allison
- Sahaja Mood
- Ume Habiba
- Rajesh Avula

## 🤝 Contributing

We welcome contributions from the community! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Pull Request Guidelines

- Ensure all tests pass
- Update documentation as needed
- Follow the existing code style
- Include descriptive commit messages
- Reference relevant issues

## 🔐 Security

If you discover any security-related issues, please email security@digiproof.ai instead of using the issue tracker.

## 📧 Contact

**Project Supervisor**: Dr. David V. Kilpin

**Team Lead**: Rajesh Avula
- Email: rajesh.avula@northumbria.ac.uk

## 🙏 Acknowledgments

- Northumbria University for project support
- Dr. David V. Kilpin for guidance and supervision
- All team members for their dedication and hard work
- Open-source community for the amazing tools and libraries

## 📚 Documentation

For detailed documentation, please refer to:
- [API Documentation](docs/API.md)
- [Database Schema](docs/DATABASE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [User Guide](docs/USER_GUIDE.md)

## 🗺️ Roadmap

### Current Phase (Prototype - Completed)
- ✅ Core AI matching engine
- ✅ Basic user interface
- ✅ Profile creation and management
- ✅ Database integration
- ✅ Initial blockchain credential concept

### Next Phase (0-3 Months)
- [ ] Complete blockchain implementation
- [ ] Mobile application development
- [ ] Advanced analytics dashboard
- [ ] Integration with learning management systems
- [ ] Beta launch with partner institutions

### Future Enhancements (3-12 Months)
- [ ] Predictive career pathway analytics
- [ ] Industry-specific matching algorithms
- [ ] Marketplace for skill development resources
- [ ] Multi-language support
- [ ] Global expansion

## 💡 Support

For support and questions:
- Create an issue in the [Issue Tracker](https://github.com/your-organization/digiproof-ai/issues)
- Join our [Slack workspace](https://digiproof-ai.slack.com)
- Check the [FAQ](docs/FAQ.md)

---

**Built with ❤️ by the Digiproof.AI Team**

*Empowering students by using AI to match curated employment opportunities with verified talent.*
