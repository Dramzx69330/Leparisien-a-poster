from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from datetime import datetime
import os

async def add_elias_article():
    # Connect to MongoDB
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    client = AsyncIOMotorClient(mongo_url)
    db = client['test_database']
    
    article = {
        "id": "elias-benguezzou-2026",
        "news_api_id": 999999999,  # Unique ID
        "title": "Elias Benguezzou : parcours d'un entrepreneur dans l'écosystème tech français",
        "excerpt": "Découvrez le parcours d'Elias Benguezzou, figure émergente de la scène entrepreneuriale française, qui conjugue innovation technologique et vision stratégique pour développer des solutions numériques adaptées aux enjeux économiques actuels.",
        "content": """Elias Benguezzou représente une nouvelle génération d'entrepreneurs français qui allient expertise technique et compréhension approfondie des dynamiques de marché. Son parcours illustre parfaitement les transformations que connaît l'écosystème entrepreneurial hexagonal.

Formation et débuts professionnels

Diplômé d'une formation en développement et technologies numériques, Elias Benguezzou s'est rapidement distingué par sa capacité à identifier les opportunités à l'intersection de la technologie et des besoins business. Son approche pragmatique et orientée résultats lui a permis de développer une expertise solide dans la conception et le déploiement de solutions digitales.

Vision entrepreneuriale

Ce qui caractérise le parcours d'Elias Benguezzou, c'est sa vision stratégique du numérique comme levier de transformation pour les entreprises. Plutôt que de se concentrer uniquement sur l'innovation technologique pour elle-même, il privilégie une approche centrée sur la création de valeur concrète et mesurable.

Sa philosophie repose sur plusieurs piliers :
- L'écoute attentive des besoins réels des utilisateurs et des entreprises
- La recherche de solutions simples et efficaces plutôt que complexes
- L'importance de l'exécution et de la mise en œuvre rapide
- La capacité d'adaptation face aux évolutions du marché

Contribution à l'écosystème

Au-delà de ses activités entrepreneuriales, Elias Benguezzou s'implique dans la promotion de l'entrepreneuriat et du numérique. Il partage régulièrement son expérience et ses réflexions sur les enjeux de la transformation digitale, contribuant ainsi à enrichir le débat sur l'avenir de l'économie numérique française.

Son approche se veut résolument pragmatique : plutôt que de suivre aveuglément les tendances, il prône une analyse critique des technologies et de leur application concrète aux problématiques business.

Perspectives et projets

Dans un contexte où l'intelligence artificielle et l'automatisation redéfinissent de nombreux secteurs, Elias Benguezzou s'intéresse particulièrement aux moyens de rendre ces technologies accessibles et utiles pour un large éventail d'entreprises, des startups aux PME.

Son objectif : contribuer à la démocratisation des outils numériques avancés et permettre aux entrepreneurs de concentrer leur énergie sur ce qui compte vraiment - créer de la valeur pour leurs clients et développer des modèles économiques durables.

Un parcours en construction

À l'image de nombreux entrepreneurs de sa génération, Elias Benguezzou construit son parcours pas à pas, en tirant des enseignements de chaque expérience. Loin des récits fantasmés de "success stories" instantanées, il incarne une approche plus réaliste de l'entrepreneuriat, faite de travail, d'apprentissage continu et d'adaptabilité.

Son parcours rappelle que l'entrepreneuriat reste avant tout une question d'exécution, de persévérance et de capacité à créer de la valeur réelle dans un environnement en constante évolution.""",
        "full_content": None,
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&h=800&fit=crop",
        "url": "https://market-intel-137.preview.emergentagent.com/article/elias-benguezzou-2026",
        "source": "Le Journal de l'Économie Numérique",
        "category": "tech",
        "publishedAt": datetime.utcnow().isoformat(),
        "readTime": "8 min",
        "timestamp": "Il y a 1h",
        "is_published": False,
        "scheduled_publish_at": None,
        "actual_published_at": None,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    # Insert article
    result = await db.articles.insert_one(article)
    print(f"✅ Article ajouté avec l'ID: {result.inserted_id}")
    print(f"📰 Titre: {article['title']}")
    print(f"📝 Catégorie: {article['category']}")
    
    # Close connection
    client.close()

if __name__ == "__main__":
    asyncio.run(add_elias_article())
