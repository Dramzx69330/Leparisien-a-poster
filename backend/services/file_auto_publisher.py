"""
Auto-publisher pour les articles (version fichiers JSON)
Publie automatiquement 1 article toutes les 2 heures
"""
import asyncio
import logging
from datetime import datetime
from services.file_article_service import file_article_service

logger = logging.getLogger(__name__)

class FileAutoPublisher:
    def __init__(self, interval_hours: float = 2.0):
        self.interval_hours = interval_hours
        self.interval_seconds = interval_hours * 3600
        self.task = None
        self.running = False
    
    async def publish_next(self):
        """Publier le prochain article"""
        try:
            article = file_article_service.publish_next_article()
            if article:
                logger.info(f"✅ Auto-published article: {article.get('title', 'Unknown')[:60]}...")
                
                # Get remaining count
                stats = file_article_service.get_stats()
                remaining = stats.get('unpublished', 0)
                logger.info(f"📊 {remaining} articles remaining in queue")
            else:
                logger.info("No unpublished articles available")
        except Exception as e:
            logger.error(f"Error auto-publishing article: {e}")
    
    async def run(self):
        """Boucle principale de publication"""
        logger.info(f"🚀 Starting auto-publisher (publishes every {self.interval_hours} hour(s))")
        self.running = True
        
        while self.running:
            try:
                await self.publish_next()
                await asyncio.sleep(self.interval_seconds)
            except asyncio.CancelledError:
                logger.info("Auto-publisher cancelled")
                break
            except Exception as e:
                logger.error(f"Error in auto-publisher loop: {e}")
                await asyncio.sleep(60)  # Wait 1 minute before retrying
    
    def start(self):
        """Démarrer l'auto-publisher"""
        if not self.task or self.task.done():
            self.task = asyncio.create_task(self.run())
            logger.info("Auto-publisher started")
    
    def stop(self):
        """Arrêter l'auto-publisher"""
        self.running = False
        if self.task:
            self.task.cancel()
            logger.info("Auto-publisher stopped")

# Global instance
_auto_publisher = None

def start_file_auto_publisher():
    """Démarrer l'auto-publisher global"""
    global _auto_publisher
    if _auto_publisher is None:
        _auto_publisher = FileAutoPublisher(interval_hours=2.0)
        _auto_publisher.start()

def stop_file_auto_publisher():
    """Arrêter l'auto-publisher global"""
    global _auto_publisher
    if _auto_publisher:
        _auto_publisher.stop()
