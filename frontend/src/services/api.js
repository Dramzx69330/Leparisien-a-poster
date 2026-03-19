import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export const newsAPI = {
  // Get top headlines
  getTopHeadlines: async (category = null, page = 1, pageSize = 20) => {
    try {
      const params = { page, pageSize };
      if (category) params.category = category;
      
      const response = await axios.get(`${API}/news/top-headlines`, { params });
      return response.data;
    } catch (error) {
      console.error('Error fetching top headlines:', error);
      throw error;
    }
  },

  // Search articles
  searchArticles: async (query, page = 1, pageSize = 20) => {
    try {
      const response = await axios.get(`${API}/news/search`, {
        params: { q: query, page, pageSize }
      });
      return response.data;
    } catch (error) {
      console.error('Error searching articles:', error);
      throw error;
    }
  },

  // Get recent news for sidebar
  getRecentNews: async (page = 1, pageSize = 10) => {
    try {
      const response = await axios.get(`${API}/news/recent`, {
        params: { page, pageSize }
      });
      return response.data;
    } catch (error) {
      console.error('Error fetching recent news:', error);
      throw error;
    }
  },

  // Get news by category
  getNewsByCategory: async (category, page = 1, pageSize = 20) => {
    try {
      const response = await axios.get(`${API}/news/category/${category}`, {
        params: { page, pageSize }
      });
      return response.data;
    } catch (error) {
      console.error('Error fetching category news:', error);
      throw error;
    }
  }
};
