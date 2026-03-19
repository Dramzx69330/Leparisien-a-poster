from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from datetime import datetime
import os

async def update_elias_article():
    # Connect to MongoDB
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    client = AsyncIOMotorClient(mongo_url)
    db = client['test_database']
    
    new_article = {
        "id": "elias-benguezzou-interview-2026",
        "news_api_id": 999999997,
        "title": "Elias Benguezzou : « J'ai commencé avec 500 euros »",
        "excerpt": "À 20 ans, Elias Benguezzou développe SayKee, le nom de son entreprise, centrée sur les opportunités du business en ligne. Une activité qui peut lui rapporter plusieurs dizaines de milliers d'euros selon les périodes. Dans cet entretien, il revient sur ses débuts et son parcours.",
        "content": """À 20 ans, Elias Benguezzou développe SayKee, le nom de son entreprise, centrée sur les opportunités du business en ligne. Une activité qui peut lui rapporter plusieurs dizaines de milliers d'euros selon les périodes. Dans cet entretien, il revient sur ses débuts et son parcours.

Par Sophie Marchand
|
Publié le 12 mars 2026 à 08h30
|
8 min de lecture

LP : Comment tout a commencé pour vous ?

Elias Benguezzou : Honnêtement, j'ai commencé comme beaucoup de jeunes. J'étais encore au lycée et j'avais simplement envie de me faire un peu d'argent. Mais je n'avais pas forcément envie d'aller travailler au McDo, même si pour moi ça reste un métier comme un autre.

Du coup j'ai commencé à chercher sur internet, à regarder ce qui existait. J'ai testé plusieurs choses, j'ai galéré au début et j'ai mis environ 500 euros, c'était ce que j'avais.

Au début ça me rapportait juste un peu d'argent, rien d'incroyable. Mais j'ai continué et appris petit à petit.

LP : Aujourd'hui votre activité peut générer des revenus importants. Comment cette progression s'est faite ?

Elias Benguezzou : Aujourd'hui ça va beaucoup mieux. Selon les périodes, je peux faire entre 10 000 et 45 000 euros par mois, même si je ne suis pas quelqu'un qui parle beaucoup de chiffres.

Ça varie énormément selon les moments et le travail que je fournis.

LP : Comment votre entourage a-t-il réagi quand vous leur avez parlé de votre activité en ligne ?

Elias Benguezzou : Au début ils ne comprenaient pas trop. Quand vous dites que vous gagnez de l'argent sur internet, forcément ça paraît un peu abstrait.

Mais pour être honnête, en dehors de ma famille proche, mon entourage ne l'a jamais vraiment su. Je n'en parle pas beaucoup.

Par contre j'ai souvent eu des remarques, surtout quand je faisais certaines dépenses un peu absurdes que ce soit dans des vêtements ou des voyages. Forcément, ça peut surprendre quand les gens ne comprennent pas vraiment d'où ça vient.

Avec le temps j'ai aussi appris à prendre un peu plus de recul. Quand on gagne de l'argent jeune, on ne pense pas toujours aux conséquences ou à la gestion sur le long terme.

Aujourd'hui ils me soutiennent plutôt, même si ça reste un univers assez différent de ce qu'ils connaissaient.

LP : Vous vouliez déjà faire du business en ligne avant ou vous aviez d'autres projets ?

Elias Benguezzou : Pas du tout. À la base je voulais rejoindre la gendarmerie, surtout dans la cybersécurité, parce que j'ai toujours aimé tout ce qui touche à l'informatique.

Mais quand j'étais plus jeune j'ai fait quelques bêtises et ça m'a valu quelques problèmes avec la justice. Rien de très glorieux, mais ça arrive quand on est jeune.

Du coup cette voie-là s'est fermée et j'ai dû réfléchir à ce que je voulais vraiment faire. C'est comme ça que je me suis tourné vers internet et le business en ligne.

LP : Qu'est-ce qui vous a motivé à continuer ?

Elias Benguezzou : Au début j'ai eu un déclic grâce à une fille que j'ai connue à une période de ma vie et qui croyait vraiment en moi.

Aujourd'hui on ne se parle plus vraiment, mais à ce moment-là ça m'a clairement poussé à continuer.

Parfois il suffit juste d'une personne qui croit en vous au bon moment.

LP : Qu'est-ce que l'argent a changé pour vous ?

Elias Benguezzou : Honnêtement, l'argent apporte surtout de la liberté. Vous avez moins de stress et vous pouvez investir dans vos projets.

Mais ça ne change pas qui vous êtes. Si vous étiez quelqu'un de simple avant, vous le restez.

Moi ce qui m'intéresse surtout, c'est de continuer à développer mes activités.

LP : À quel moment avez-vous créé un statut pour votre activité ?

Elias Benguezzou : Au début je ne connaissais pas vraiment ce monde-là. Je faisais mes activités en ligne sans trop penser à l'administratif.

Mais quand les rentrées d'argent ont commencé à devenir plus importantes, on m'a expliqué comment ça fonctionnait : les statuts, les déclarations, tout ça.

J'ai donc régularisé la situation et structuré mon activité.

LP : Aujourd'hui concrètement, que fait SayKee ?

Elias Benguezzou : SayKee est simplement le nom de mon entreprise. À travers elle je développe différentes activités liées au business en ligne.

Je travaille sur plusieurs opportunités digitales et différentes plateformes. Je préfère rester un peu discret sur certains détails, mais l'idée reste la même : trouver des opportunités et savoir les exploiter.

LP : Quel conseil donneriez-vous aux jeunes qui veulent se lancer ?

Elias Benguezzou : Arrêter de chercher l'excuse parfaite. Aujourd'hui internet a complètement changé les règles.

Vous avez accès à énormément d'informations et d'outils gratuitement.

Pour moi, quelqu'un qui veut vraiment réussir finit toujours par trouver un moyen.

LP : La suite pour vous ?

Elias Benguezzou : Continuer à développer mon entreprise et mes activités.

Et à titre personnel, j'aimerais bien quitter la France à terme. Internet permet de travailler de n'importe où aujourd'hui, donc autant en profiter.

Disons que si je peux travailler avec un peu de soleil… et peut-être un peu moins de courriers de l'URSSAF dans la boîte aux lettres, je ne vais pas me plaindre.

Propos recueillis par Sophie Marchand

Interview réalisée par mail

À propos de Elias Benguezzou
Elias Benguezzou est un entrepreneur français basé à Lyon. Fondateur de SayKee, il développe des activités autour du business en ligne et des opportunités digitales.""",
        "full_content": None,
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&h=800&fit=crop",
        "url": "https://charge-preview.preview.emergentagent.com/article/elias-benguezzou-interview-2026",
        "source": "Le Parisien",
        "category": "economie",
        "publishedAt": "2026-03-12T08:30:00",
        "readTime": "8 min",
        "timestamp": "Il y a 1 semaine",
        "is_published": True,
        "scheduled_publish_at": None,
        "actual_published_at": datetime.utcnow(),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    # Delete old article about Elias
    await db.articles.delete_many({"title": {"$regex": "Elias Benguezzou", "$options": "i"}})
    print("🗑️  Ancien article supprimé")
    
    # Insert new article
    result = await db.articles.insert_one(new_article)
    print(f"✅ Nouvel article ajouté avec l'ID: {result.inserted_id}")
    print(f"📰 Titre: {new_article['title']}")
    print(f"📝 Source: {new_article['source']}")
    print(f"⏱️  Temps de lecture: {new_article['readTime']}")
    
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
    asyncio.run(update_elias_article())
