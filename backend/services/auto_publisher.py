import asyncio
import logging
from datetime import datetime
from services.article_scheduler import ArticleScheduler

logger = logging.getLogger(__name__)

class AutoPublisher:
    def __init__(self, db, interval_seconds=3600):  # 3600 seconds = 1 hour
        self.db = db
        self.scheduler = ArticleScheduler(db)
        self.interval_seconds = interval_seconds
        self.running = False
        
    async def start(self):
        """Start the auto-publisher background task"""
        self.running = True
        logger.info(f"Starting auto-publisher (publishes every {self.interval_seconds/3600} hour(s))")
        
        while self.running:
            try:
                # Publish scheduled articles
                published_count = await self.scheduler.publish_scheduled_articles()
                if published_count > 0:
                    logger.info(f"Auto-published {published_count} article(s)")
                
                # Schedule next article for 1 hour from now
                unpublished = await self.scheduler.get_unpublished_count()
                if unpublished > 0:
                    await self.scheduler.schedule_next_publication()
                    logger.info(f"Scheduled next article. {unpublished-1} articles remaining in queue")
                else:
                    logger.warning("No unpublished articles available. Please fetch more articles.")
                
                # Wait for next interval
                await asyncio.sleep(self.interval_seconds)
                
            except Exception as e:
                logger.error(f"Error in auto-publisher: {str(e)}")
                await asyncio.sleep(60)  # Wait 1 minute before retrying
    
    def stop(self):
        """Stop the auto-publisher"""
        self.running = False
        logger.info("Stopping auto-publisher")

# Global auto-publisher instance
auto_publisher = None

async def start_auto_publisher(db):
    """Initialize and start the auto-publisher"""
    global auto_publisher
    auto_publisher = AutoPublisher(db, interval_seconds=3600)  # 1 hour
    asyncio.create_task(auto_publisher.start())
    logger.info("Auto-publisher initialized and started")

async def stop_auto_publisher():
    """Stop the auto-publisher"""
    global auto_publisher
    if auto_publisher:
        auto_publisher.stop()
