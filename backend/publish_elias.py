from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from datetime import datetime
import os

async def publish_elias_article():
    # Connect to MongoDB
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    client = AsyncIOMotorClient(mongo_url)
    db = client['test_database']
    
    # Find and publish the Elias article
    result = await db.articles.update_one(
        {"id": "elias-benguezzou-2026"},
        {
            "$set": {
                "is_published": True,
                "actual_published_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        }
    )
    
    if result.modified_count > 0:
        print("✅ Article sur Elias Benguezzou publié avec succès!")
        
        # Get the article
        article = await db.articles.find_one({"id": "elias-benguezzou-2026"})
        print(f"📰 Titre: {article['title']}")
        print(f"🕐 Publié à: {article['actual_published_at']}")
    else:
        print("❌ Article non trouvé ou déjà publié")
    
    # Get stats
    stats = {
        "published": await db.articles.count_documents({"is_published": True}),
        "unpublished": await db.articles.count_documents({"is_published": False})
    }
    print(f"\n📊 Statistiques:")
    print(f"   Articles publiés: {stats['published']}")
    print(f"   Articles en attente: {stats['unpublished']}")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(publish_elias_article())
