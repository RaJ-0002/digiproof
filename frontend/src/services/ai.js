// src/services/ai.js  ← you can also put user registration here
import api from './api';

export const registerUser = async (userData) => {
  const { data } = await api.post('/users', userData);
  return data;
};
