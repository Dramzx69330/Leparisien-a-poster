"""
Router pour les articles (version fichiers JSON)
"""
from fastapi import APIRouter, Query, HTTPException
from typing import Optional
import logging
from services.file_article_service import file_article_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/articles", tags=["articles"])

@router.get("/published")
async def get_published_articles(
    category: Optional[str] = Query(None, description="Filter by category"),
    page: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(20, ge=1, le=100, description="Number of articles per page")
):
    """
    Get all published articles from JSON file
    """
    try:
        result = file_article_service.get_published_articles(category, page, pageSize)
        return result
    except Exception as e:
        logger.error(f"Error getting published articles: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats")
async def get_articles_stats():
    """
    Get articles statistics
    """
    try:
        return file_article_service.get_stats()
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{article_id}")
async def get_article(article_id: str):
    """
    Get a single article by ID
    """
    try:
        article = file_article_service.get_article_by_id(article_id)
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        return {'status': 'ok', 'article': article}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting article: {e}")
        raise HTTPException(status_code=500, detail=str(e))
