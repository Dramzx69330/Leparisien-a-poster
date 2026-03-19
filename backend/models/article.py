from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    news_api_id: int  # ID from NewsAPI
    title: str
    excerpt: Optional[str] = None
    content: Optional[str] = None
    full_content: Optional[str] = None
    image: Optional[str] = None
    url: str
    source: str
    category: str
    publishedAt: str  # Original publish date from NewsAPI
    readTime: Optional[str] = None
    timestamp: Optional[str] = None
    
    # Publication scheduling fields
    is_published: bool = False
    scheduled_publish_at: Optional[datetime] = None
    actual_published_at: Optional[datetime] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Économie française en hausse",
                "excerpt": "Les marchés européens...",
                "content": "Article complet...",
                "url": "https://example.com/article",
                "source": "Le Figaro",
                "category": "europe"
            }
        }
