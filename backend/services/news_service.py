import os
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class NewsService:
    def __init__(self):
        self.api_key = os.environ.get('NEWS_API_KEY', '').strip('"')
        self.base_url = os.environ.get('NEWS_API_BASE_URL', 'https://newsapi.org/v2').strip('"')
        self.default_country = 'fr'
        self.default_language = 'fr'
        
        if not self.api_key:
            logger.error("NEWS_API_KEY not found in environment variables")
        else:
            logger.info(f"NewsAPI initialized with key: {self.api_key[:10]}...")

    def _make_request(self, endpoint: str, params: Dict) -> Dict:
        """Make request to NewsAPI with error handling"""
        try:
            params['apiKey'] = self.api_key
            url = f"{self.base_url}/{endpoint}"
            
            logger.info(f"Making request to: {url} with params: {params}")
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data.get('status') != 'ok':
                logger.error(f"NewsAPI error: {data.get('message')}")
                return {'status': 'error', 'message': data.get('message'), 'articles': []}
            
            return data
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {str(e)}")
            return {'status': 'error', 'message': str(e), 'articles': []}

    def _format_article(self, article: Dict) -> Dict:
        """Format article from NewsAPI to our format"""
        try:
            published_at = datetime.strptime(article.get('publishedAt', ''), '%Y-%m-%dT%H:%M:%SZ')
            time_diff = datetime.utcnow() - published_at
            
            if time_diff.seconds < 3600:
                time_ago = f"Il y a {time_diff.seconds // 60} min"
            elif time_diff.seconds < 86400:
                time_ago = f"Il y a {time_diff.seconds // 3600}h"
            else:
                time_ago = f"Il y a {time_diff.days}j"
        except:
            time_ago = "Récent"

        # Estimate read time based on content length
        content_length = len(article.get('description', '') or '')
        read_time = max(3, min(15, content_length // 100)) if content_length > 0 else 5

        return {
            'id': hash(article.get('url', '')),
            'title': article.get('title', ''),
            'excerpt': article.get('description', ''),
            'content': article.get('content', ''),
            'image': article.get('urlToImage', ''),
            'url': article.get('url', ''),
            'source': article.get('source', {}).get('name', ''),
            'publishedAt': article.get('publishedAt', ''),
            'timestamp': time_ago,
            'readTime': f"{read_time} min",
            'category': 'Actualité'
        }

    def get_top_headlines(self, category: Optional[str] = None, page: int = 1, page_size: int = 20) -> Dict:
        """Get top headlines from France"""
        # NewsAPI free tier has limited country support, so we use 'everything' with French keywords
        params = {
            'q': 'France OR Paris OR actualité',
            'language': self.default_language,
            'pageSize': page_size,
            'page': page,
            'sortBy': 'publishedAt'
        }
        
        # Map French categories to search queries
        category_queries = {
            'economie': 'économie OR finance OR business France',
            'sports': 'sport OR football OR tennis France',
            'culture': 'culture OR cinéma OR musique France',
            'sante': 'santé OR médecine France',
            'sciences': 'science OR technologie France',
            'technologie': 'technologie OR tech OR innovation France'
        }
        
        if category and category.lower() in category_queries:
            params['q'] = category_queries[category.lower()]
        
        data = self._make_request('everything', params)
        
        if data.get('status') == 'error':
            return data
        
        formatted_articles = [self._format_article(article) for article in data.get('articles', [])]
        
        return {
            'status': 'ok',
            'articles': formatted_articles,
            'totalResults': data.get('totalResults', 0)
        }

    def search_articles(self, query: str, page: int = 1, page_size: int = 20) -> Dict:
        """Search for articles by keyword"""
        params = {
            'q': query,
            'language': self.default_language,
            'pageSize': page_size,
            'page': page,
            'sortBy': 'publishedAt'
        }
        
        data = self._make_request('everything', params)
        
        if data.get('status') == 'error':
            return data
        
        formatted_articles = [self._format_article(article) for article in data.get('articles', [])]
        
        return {
            'status': 'ok',
            'articles': formatted_articles,
            'totalResults': data.get('totalResults', 0)
        }

    def get_recent_news(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get most recent news for 'En continu' section"""
        # Get news from last 24 hours
        from_date = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
        
        params = {
            'q': 'France OR Paris',
            'language': self.default_language,
            'from': from_date,
            'pageSize': page_size,
            'page': page,
            'sortBy': 'publishedAt'
        }
        
        data = self._make_request('everything', params)
        
        if data.get('status') == 'error':
            return data
        
        formatted_articles = [self._format_article(article) for article in data.get('articles', [])]
        
        return {
            'status': 'ok',
            'articles': formatted_articles,
            'totalResults': data.get('totalResults', 0)
        }
