"""
Service pour gérer les articles via fichiers JSON (au lieu de MongoDB)
Tous les articles sont stockés dans /app/backend/data/articles.json
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

ARTICLES_FILE = "/app/backend/data/articles.json"

class FileArticleService:
    """Service pour gérer les articles stockés dans des fichiers"""
    
    def __init__(self):
        self.articles_file = ARTICLES_FILE
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Créer le fichier s'il n'existe pas"""
        if not os.path.exists(self.articles_file):
            os.makedirs(os.path.dirname(self.articles_file), exist_ok=True)
            self._save_articles([])
    
    def _load_articles(self) -> List[Dict]:
        """Charger tous les articles depuis le fichier"""
        try:
            with open(self.articles_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading articles: {e}")
            return []
    
    def _save_articles(self, articles: List[Dict]):
        """Sauvegarder tous les articles dans le fichier"""
        try:
            with open(self.articles_file, 'w', encoding='utf-8') as f:
                json.dump(articles, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Error saving articles: {e}")
    
    def get_published_articles(self, category: Optional[str] = None, page: int = 1, page_size: int = 20) -> Dict:
        """Récupérer les articles publiés"""
        articles = self._load_articles()
        
        # Filter published articles
        published = [a for a in articles if a.get('is_published', False)]
        
        # Filter by category if specified
        if category:
            published = [a for a in published if a.get('category') == category]
        
        # Sort by date (most recent first)
        published.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)
        
        # Pagination
        start = (page - 1) * page_size
        end = start + page_size
        paginated = published[start:end]
        
        return {
            'status': 'ok',
            'articles': paginated,
            'totalResults': len(published),
            'page': page,
            'pageSize': page_size
        }
    
    def get_article_by_id(self, article_id: str) -> Optional[Dict]:
        """Récupérer un article par son ID"""
        articles = self._load_articles()
        for article in articles:
            if article.get('id') == article_id:
                return article
        return None
    
    def search_articles(self, query: str) -> Dict:
        """Rechercher des articles"""
        articles = self._load_articles()
        
        # Search in published articles only
        published = [a for a in articles if a.get('is_published', False)]
        
        # Search in title, excerpt, and content
        query_lower = query.lower()
        results = []
        for article in published:
            title = article.get('title', '').lower()
            excerpt = article.get('excerpt', '').lower()
            content = article.get('content', '').lower()
            
            if query_lower in title or query_lower in excerpt or query_lower in content:
                results.append(article)
        
        return {
            'status': 'ok',
            'articles': results,
            'totalResults': len(results)
        }
    
    def get_stats(self) -> Dict:
        """Récupérer les statistiques des articles"""
        articles = self._load_articles()
        
        published = sum(1 for a in articles if a.get('is_published', False))
        unpublished = sum(1 for a in articles if not a.get('is_published', False))
        scheduled = sum(1 for a in articles if a.get('scheduled_publish_at'))
        
        return {
            'status': 'ok',
            'published': published,
            'unpublished': unpublished,
            'scheduled': scheduled,
            'total': len(articles)
        }
    
    def publish_next_article(self) -> Optional[Dict]:
        """Publier le prochain article non publié (pour auto-publisher)"""
        articles = self._load_articles()
        
        # Find first unpublished, non-protected article
        for i, article in enumerate(articles):
            if not article.get('is_published', False) and not article.get('protected', False):
                # Publish it
                article['is_published'] = True
                article['actual_published_at'] = datetime.utcnow().isoformat()
                article['updated_at'] = datetime.utcnow().isoformat()
                
                # Calculate timestamp
                article['timestamp'] = "Il y a quelques instants"
                
                # Save
                articles[i] = article
                self._save_articles(articles)
                
                logger.info(f"Published article: {article.get('title', 'Unknown')}")
                return article
        
        return None
    
    def add_article(self, article: Dict) -> Dict:
        """Ajouter un nouvel article"""
        articles = self._load_articles()
        
        # Add timestamps
        now = datetime.utcnow().isoformat()
        article['created_at'] = now
        article['updated_at'] = now
        
        # Add to list
        articles.append(article)
        self._save_articles(articles)
        
        return article
    
    def update_article(self, article_id: str, updates: Dict) -> bool:
        """Mettre à jour un article"""
        articles = self._load_articles()
        
        for i, article in enumerate(articles):
            if article.get('id') == article_id:
                # Don't update protected articles
                if article.get('protected', False):
                    logger.warning(f"Attempted to update protected article: {article_id}")
                    return False
                
                # Update
                article.update(updates)
                article['updated_at'] = datetime.utcnow().isoformat()
                articles[i] = article
                self._save_articles(articles)
                return True
        
        return False
    
    def delete_article(self, article_id: str) -> bool:
        """Supprimer un article"""
        articles = self._load_articles()
        
        for i, article in enumerate(articles):
            if article.get('id') == article_id:
                # Don't delete protected articles
                if article.get('protected', False):
                    logger.warning(f"Attempted to delete protected article: {article_id}")
                    return False
                
                del articles[i]
                self._save_articles(articles)
                return True
        
        return False

# Global instance
file_article_service = FileArticleService()
