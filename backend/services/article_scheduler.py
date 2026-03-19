import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.article import Article
import asyncio

logger = logging.getLogger(__name__)

class ArticleScheduler:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.articles_collection = db.articles
        
    async def save_articles_to_db(self, articles: List[Dict], category: str = "general"):
        """Save fetched articles to database for later publication"""
        saved_count = 0
        
        for article_data in articles:
            try:
                # Check if article already exists
                existing = await self.articles_collection.find_one({
                    "news_api_id": article_data.get("id")
                })
                
                if existing:
                    logger.info(f"Article already exists: {article_data.get('title')[:50]}...")
                    continue
                
                # Create article object
                article = Article(
                    news_api_id=article_data.get("id"),
                    title=article_data.get("title"),
                    excerpt=article_data.get("excerpt"),
                    content=article_data.get("content"),
                    image=article_data.get("image"),
                    url=article_data.get("url"),
                    source=article_data.get("source"),
                    category=category,
                    publishedAt=article_data.get("publishedAt"),
                    readTime=article_data.get("readTime"),
                    timestamp=article_data.get("timestamp"),
                    is_published=False  # Not published yet
                )
                
                # Save to database
                await self.articles_collection.insert_one(article.dict())
                saved_count += 1
                logger.info(f"Saved article: {article.title[:50]}...")
                
            except Exception as e:
                logger.error(f"Error saving article: {str(e)}")
                continue
        
        logger.info(f"Saved {saved_count} new articles to database")
        return saved_count
    
    async def schedule_next_publication(self):
        """Schedule the next unpublished article for publication in 2 hours"""
        try:
            # Find next unpublished article
            next_article = await self.articles_collection.find_one(
                {"is_published": False},
                sort=[("created_at", 1)]  # Oldest first
            )
            
            if not next_article:
                logger.warning("No unpublished articles available")
                return None
            
            # Schedule for 2 hours from now
            publish_time = datetime.utcnow() + timedelta(hours=2)
            
            await self.articles_collection.update_one(
                {"_id": next_article["_id"]},
                {
                    "$set": {
                        "scheduled_publish_at": publish_time,
                        "updated_at": datetime.utcnow()
                    }
                }
            )
            
            logger.info(f"Scheduled article '{next_article['title'][:50]}...' for {publish_time}")
            return next_article
            
        except Exception as e:
            logger.error(f"Error scheduling publication: {str(e)}")
            return None
    
    async def publish_scheduled_articles(self):
        """Publish articles that are scheduled for now or past"""
        try:
            now = datetime.utcnow()
            
            # Find articles scheduled for publication
            scheduled = await self.articles_collection.find({
                "is_published": False,
                "scheduled_publish_at": {"$lte": now}
            }).to_list(length=100)
            
            published_count = 0
            for article in scheduled:
                await self.articles_collection.update_one(
                    {"_id": article["_id"]},
                    {
                        "$set": {
                            "is_published": True,
                            "actual_published_at": now,
                            "updated_at": now
                        }
                    }
                )
                published_count += 1
                logger.info(f"Published article: {article['title'][:50]}...")
            
            if published_count > 0:
                logger.info(f"Published {published_count} articles")
            
            return published_count
            
        except Exception as e:
            logger.error(f"Error publishing articles: {str(e)}")
            return 0
    
    async def get_published_articles(self, category: Optional[str] = None, limit: int = 20, page: int = 1):
        """Get published articles from database"""
        try:
            query = {"is_published": True}
            if category:
                query["category"] = category
            
            skip = (page - 1) * limit
            
            articles = await self.articles_collection.find(query)\
                .sort("actual_published_at", -1)\
                .skip(skip)\
                .limit(limit)\
                .to_list(length=limit)
            
            total = await self.articles_collection.count_documents(query)
            
            return articles, total
            
        except Exception as e:
            logger.error(f"Error getting published articles: {str(e)}")
            return [], 0
    
    async def get_unpublished_count(self):
        """Get count of unpublished articles"""
        try:
            count = await self.articles_collection.count_documents({"is_published": False})
            return count
        except Exception as e:
            logger.error(f"Error counting unpublished articles: {str(e)}")
            return 0
