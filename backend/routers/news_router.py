from fastapi import APIRouter, Query, HTTPException
from typing import Optional
import logging
import os

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/news", tags=["news"])

# Initialize news_service as None, will be created on first request
_news_service = None
_scraper_service = None

def get_news_service():
    global _news_service
    if _news_service is None:
        from services.news_service import NewsService
        _news_service = NewsService()
        # Log API key availability
        api_key = os.environ.get('NEWS_API_KEY', '').strip('"')
        logger.info(f"Initializing NewsService with API key present: {bool(api_key)}")
    return _news_service

def get_scraper_service():
    global _scraper_service
    if _scraper_service is None:
        from services.scraper_service import ArticleScraper
        _scraper_service = ArticleScraper()
        logger.info("Initializing ArticleScraper")
    return _scraper_service

@router.get("/top-headlines")
async def get_top_headlines(
    category: Optional[str] = Query(None, description="Category filter"),
    page: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(20, ge=1, le=100, description="Number of articles per page")
):
    """
    Get top headlines from French news sources
    """
    try:
        news_service = get_news_service()
        result = news_service.get_top_headlines(category=category, page=page, page_size=pageSize)
        
        if result.get('status') == 'error':
            raise HTTPException(status_code=500, detail=result.get('message', 'Error fetching news'))
        
        return result
    except Exception as e:
        logger.error(f"Error in get_top_headlines: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search")
async def search_news(
    q: str = Query(..., description="Search query"),
    page: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(20, ge=1, le=100, description="Number of articles per page")
):
    """
    Search for news articles by keyword in database AND NewsAPI
    """
    try:
        from server import db
        news_service = get_news_service()
        
        # Search in published articles from database
        search_regex = {"$regex": q, "$options": "i"}
        db_articles = await db.articles.find(
            {
                "is_published": True,
                "$or": [
                    {"title": search_regex},
                    {"excerpt": search_regex},
                    {"content": search_regex}
                ]
            },
            {"_id": 0}
        ).to_list(100)
        
        # Search in NewsAPI
        newsapi_result = news_service.search_articles(query=q, page=page, page_size=pageSize)
        newsapi_articles = newsapi_result.get('articles', []) if newsapi_result.get('status') == 'ok' else []
        
        # Combine both sources - database articles first
        all_articles = db_articles + newsapi_articles
        
        return {
            'status': 'ok',
            'articles': all_articles,
            'totalResults': len(all_articles)
        }
    except Exception as e:
        logger.error(f"Error in search_news: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/recent")
async def get_recent_news(
    page: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(10, ge=1, le=50, description="Number of articles per page")
):
    """
    Get most recent news for 'En continu' section
    """
    try:
        news_service = get_news_service()
        result = news_service.get_recent_news(page=page, page_size=pageSize)
        
        if result.get('status') == 'error':
            raise HTTPException(status_code=500, detail=result.get('message', 'Error fetching recent news'))
        
        return result
    except Exception as e:
        logger.error(f"Error in get_recent_news: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/category/{category}")
async def get_news_by_category(
    category: str,
    page: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(20, ge=1, le=100, description="Number of articles per page")
):
    """
    Get news by specific category
    """
    try:
        news_service = get_news_service()
        result = news_service.get_top_headlines(category=category, page=page, page_size=pageSize)
        
        if result.get('status') == 'error':
            raise HTTPException(status_code=500, detail=result.get('message', 'Error fetching category news'))
        
        return result
    except Exception as e:
        logger.error(f"Error in get_news_by_category: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/scrape-article")
async def scrape_article_content(article_url: str = Query(..., description="URL of the article to scrape")):
    """
    Scrape the full content of an article from its URL
    """
    try:
        scraper = get_scraper_service()
        content = scraper.scrape_article_content(article_url)
        
        if content:
            return {
                'status': 'ok',
                'content': content,
                'url': article_url
            }
        else:
            raise HTTPException(status_code=404, detail="Could not extract article content")
        
    except Exception as e:
        logger.error(f"Error in scrape_article_content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

        if result.get('status') == 'error':
            raise HTTPException(status_code=500, detail=result.get('message', 'Error fetching category news'))
        
        return result
    except Exception as e:
        logger.error(f"Error in get_news_by_category: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
