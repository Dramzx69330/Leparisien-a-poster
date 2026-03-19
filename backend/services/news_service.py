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
            logger.info(f"API Response status: {data.get('status')}, Total results: {data.get('totalResults')}, Articles count: {len(data.get('articles', []))}")
            
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
        """Get top economic headlines from around the world in French"""
        # Default query for economic news in French
        base_query = '(économie OR finance OR business OR marchés) NOT (sport OR football OR tennis OR cinéma OR musique)'
        
        # Region and category specific queries - MORE SPECIFIC
        category_queries = {
            'europe': '((économie OR finance OR business) AND (Europe OR européenne OR UE OR "Union européenne" OR BCE OR Allemagne OR France OR Italie OR Espagne)) NOT (Asie OR Afrique OR Amérique OR USA)',
            'amerique': '((économie OR finance OR business) AND (États-Unis OR Amérique OR USA OR américain OR Fed OR dollar OR "Wall Street" OR Washington)) NOT (Europe OR Asie OR Afrique)',
            'asie': '((économie OR finance OR business) AND (Asie OR asiatique OR Chine OR chinois OR Japon OR japonais OR Inde OR Corée OR Singapour)) NOT (Europe OR Afrique OR Amérique)',
            'afrique': '((économie OR finance OR business) AND (Afrique OR africain OR africaine)) NOT (Europe OR Asie OR Amérique)',
            'moyen-orient': '((économie OR finance OR business) AND ("Moyen-Orient" OR Golfe OR pétrole OR OPEP OR Dubaï OR Arabie OR Iran OR Irak)) NOT (Europe OR Asie OR Afrique)',
            'marches': '(bourse OR CAC40 OR "marché boursier" OR actions OR traders OR cotation OR "marchés financiers") NOT (crypto OR bitcoin)',
            'crypto': '(cryptomonnaie OR bitcoin OR blockchain OR ethereum OR "monnaie numérique" OR crypto OR NFT) NOT (bourse)',
            'tech': '((startup OR fintech OR "intelligence artificielle" OR innovation OR technologie) AND (économie OR business OR investissement)) NOT (sport OR cinéma)',
            'commerce': '(("commerce international" OR export OR import OR "échanges commerciaux" OR OMC OR douane OR tarifs) AND (économie OR business)) NOT (crypto OR bitcoin)'
        }
        
        query = category_queries.get(category.lower() if category else '', base_query)
        
        # FRENCH ONLY
        params = {
            'q': query,
            'language': 'fr',
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
        """Get most recent economic news for 'En continu' section"""
        # Get economic news from last 24 hours
        from_date = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
        
        params = {
            'q': 'économie OR finance OR business OR marchés OR trading',
            'language': 'fr',
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
