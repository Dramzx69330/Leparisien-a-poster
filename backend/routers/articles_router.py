from fastapi import APIRouter, Query, HTTPException, BackgroundTasks
from typing import Optional
import logging
from services.article_scheduler import ArticleScheduler
from services.news_service import NewsService
import os

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/articles", tags=["articles"])

# Global scheduler instance
_scheduler = None
_news_service = None

def get_scheduler():
    global _scheduler
    if _scheduler is None:
        from server import db
        _scheduler = ArticleScheduler(db)
        logger.info("Initializing ArticleScheduler")
    return _scheduler

def get_news_service():
    global _news_service
    if _news_service is None:
        _news_service = NewsService()
        api_key = os.environ.get('NEWS_API_KEY', '').strip('"')
        logger.info(f"Initializing NewsService with API key present: {bool(api_key)}")
    return _news_service

@router.post("/fetch-and-save")
async def fetch_and_save_articles(
    category: Optional[str] = Query(None, description="Category to fetch"),
    count: int = Query(50, ge=1, le=100, description="Number of articles to fetch")
):
    """
    Fetch articles from NewsAPI and save them to database for scheduled publication
    """
    try:
        news_service = get_news_service()
        scheduler = get_scheduler()
        
        # Fetch articles from NewsAPI
        result = news_service.get_top_headlines(category=category, page=1, page_size=count)
        
        if result.get('status') == 'error':
            raise HTTPException(status_code=500, detail=result.get('message'))
        
        articles = result.get('articles', [])
        
        # Save to database
        saved_count = await scheduler.save_articles_to_db(articles, category or 'general')
        
        return {
            'status': 'ok',
            'message': f'Saved {saved_count} new articles',
            'fetched': len(articles),
            'saved': saved_count
        }
        
    except Exception as e:
        logger.error(f"Error in fetch_and_save_articles: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/schedule-next")
async def schedule_next_article():
    """
    Schedule the next unpublished article for publication in 1 hour
    """
    try:
        scheduler = get_scheduler()
        article = await scheduler.schedule_next_publication()
        
        if not article:
            return {
                'status': 'warning',
                'message': 'No unpublished articles available to schedule'
            }
        
        return {
            'status': 'ok',
            'message': 'Article scheduled successfully',
            'article_title': article['title']
        }
        
    except Exception as e:
        logger.error(f"Error in schedule_next_article: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/publish-scheduled")
async def publish_scheduled_articles():
    """
    Publish all articles that are scheduled for now or past
    """
    try:
        scheduler = get_scheduler()
        count = await scheduler.publish_scheduled_articles()
        
        return {
            'status': 'ok',
            'message': f'Published {count} articles',
            'published_count': count
        }
        
    except Exception as e:
        logger.error(f"Error in publish_scheduled_articles: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/published")
async def get_published_articles(
    category: Optional[str] = Query(None, description="Category filter"),
    page: int = Query(1, ge=1, description="Page number"),
    pageSize: int = Query(20, ge=1, le=100, description="Number of articles per page")
):
    """
    Get published articles from database
    """
    try:
        scheduler = get_scheduler()
        articles, total = await scheduler.get_published_articles(
            category=category,
            limit=pageSize,
            page=page
        )
        
        return {
            'status': 'ok',
            'articles': articles,
            'totalResults': total,
            'page': page,
            'pageSize': pageSize
        }
        
    except Exception as e:
        logger.error(f"Error in get_published_articles: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats")
async def get_article_stats():
    """
    Get statistics about articles
    """
    try:
        scheduler = get_scheduler()
        unpublished = await scheduler.get_unpublished_count()
        
        from server import db
        published = await db.articles.count_documents({"is_published": True})
        scheduled = await db.articles.count_documents({
            "is_published": False,
            "scheduled_publish_at": {"$ne": None}
        })
        
        return {
            'status': 'ok',
            'unpublished': unpublished,
            'published': published,
            'scheduled': scheduled,
            'total': unpublished + published
        }
        
    except Exception as e:
        logger.error(f"Error in get_article_stats: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
