from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from datetime import datetime
import os

async def update_elias_article_html():
    # Connect to MongoDB
    mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
    client = AsyncIOMotorClient(mongo_url)
    db = client['test_database']
    
    # HTML formaté avec une belle structure
    html_content = """<div class="interview-article">
    <div class="intro">
        À 20 ans, Elias Benguezzou développe SayKee, le nom de son entreprise, centrée sur les opportunités du business en ligne. Une activité qui peut lui rapporter plusieurs dizaines de milliers d'euros selon les périodes. Dans cet entretien, il revient sur ses débuts et son parcours.
    </div>

    <div class="author">
        <strong>Par Sophie Marchand</strong> | Publié le 12 mars 2026 à 08h30 | 8 min de lecture
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Comment tout a commencé pour vous ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Honnêtement, j'ai commencé comme beaucoup de jeunes. J'étais encore au lycée et j'avais simplement envie de me faire un peu d'argent. Mais je n'avais pas forcément envie d'aller travailler au McDo, même si pour moi ça reste un métier comme un autre.
        <br><br>
        Du coup j'ai commencé à chercher sur internet, à regarder ce qui existait. J'ai testé plusieurs choses, j'ai galéré au début et j'ai mis environ 500 euros, c'était ce que j'avais.
        <br><br>
        Au début ça me rapportait juste un peu d'argent, rien d'incroyable. Mais j'ai continué et appris petit à petit.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Aujourd'hui votre activité peut générer des revenus importants. Comment cette progression s'est faite ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Aujourd'hui ça va beaucoup mieux. Selon les périodes, je peux faire entre 10 000 et 45 000 euros par mois, même si je ne suis pas quelqu'un qui parle beaucoup de chiffres.
        <br><br>
        Ça varie énormément selon les moments et le travail que je fournis.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Comment votre entourage a-t-il réagi quand vous leur avez parlé de votre activité en ligne ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Au début ils ne comprenaient pas trop. Quand vous dites que vous gagnez de l'argent sur internet, forcément ça paraît un peu abstrait.
        <br><br>
        Mais pour être honnête, en dehors de ma famille proche, mon entourage ne l'a jamais vraiment su. Je n'en parle pas beaucoup.
        <br><br>
        Par contre j'ai souvent eu des remarques, surtout quand je faisais certaines dépenses un peu absurdes que ce soit dans des vêtements ou des voyages. Forcément, ça peut surprendre quand les gens ne comprennent pas vraiment d'où ça vient.
        <br><br>
        Avec le temps j'ai aussi appris à prendre un peu plus de recul. Quand on gagne de l'argent jeune, on ne pense pas toujours aux conséquences ou à la gestion sur le long terme.
        <br><br>
        Aujourd'hui ils me soutiennent plutôt, même si ça reste un univers assez différent de ce qu'ils connaissaient.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Vous vouliez déjà faire du business en ligne avant ou vous aviez d'autres projets ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Pas du tout. À la base je voulais rejoindre la gendarmerie, surtout dans la cybersécurité, parce que j'ai toujours aimé tout ce qui touche à l'informatique.
        <br><br>
        Mais quand j'étais plus jeune j'ai fait quelques bêtises et ça m'a valu quelques problèmes avec la justice. Rien de très glorieux, mais ça arrive quand on est jeune.
        <br><br>
        Du coup cette voie-là s'est fermée et j'ai dû réfléchir à ce que je voulais vraiment faire. C'est comme ça que je me suis tourné vers internet et le business en ligne.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Qu'est-ce qui vous a motivé à continuer ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Au début j'ai eu un déclic grâce à une fille que j'ai connue à une période de ma vie et qui croyait vraiment en moi.
        <br><br>
        Aujourd'hui on ne se parle plus vraiment, mais à ce moment-là ça m'a clairement poussé à continuer.
        <br><br>
        Parfois il suffit juste d'une personne qui croit en vous au bon moment.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Qu'est-ce que l'argent a changé pour vous ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Honnêtement, l'argent apporte surtout de la liberté. Vous avez moins de stress et vous pouvez investir dans vos projets.
        <br><br>
        Mais ça ne change pas qui vous êtes. Si vous étiez quelqu'un de simple avant, vous le restez.
        <br><br>
        Moi ce qui m'intéresse surtout, c'est de continuer à développer mes activités.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> À quel moment avez-vous créé un statut pour votre activité ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Au début je ne connaissais pas vraiment ce monde-là. Je faisais mes activités en ligne sans trop penser à l'administratif.
        <br><br>
        Mais quand les rentrées d'argent ont commencé à devenir plus importantes, on m'a expliqué comment ça fonctionnait : les statuts, les déclarations, tout ça.
        <br><br>
        J'ai donc régularisé la situation et structuré mon activité.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Aujourd'hui concrètement, que fait SayKee ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> SayKee est simplement le nom de mon entreprise. À travers elle je développe différentes activités liées au business en ligne.
        <br><br>
        Je travaille sur plusieurs opportunités digitales et différentes plateformes. Je préfère rester un peu discret sur certains détails, mais l'idée reste la même : trouver des opportunités et savoir les exploiter.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> Quel conseil donneriez-vous aux jeunes qui veulent se lancer ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Arrêter de chercher l'excuse parfaite. Aujourd'hui internet a complètement changé les règles.
        <br><br>
        Vous avez accès à énormément d'informations et d'outils gratuitement.
        <br><br>
        Pour moi, quelqu'un qui veut vraiment réussir finit toujours par trouver un moyen.
    </div>

    <div class="question">
        <span class="journalist">LP :</span> La suite pour vous ?
    </div>
    <div class="answer">
        <strong>Elias Benguezzou :</strong> Continuer à développer mon entreprise et mes activités.
        <br><br>
        Et à titre personnel, j'aimerais bien quitter la France à terme. Internet permet de travailler de n'importe où aujourd'hui, donc autant en profiter.
        <br><br>
        Disons que si je peux travailler avec un peu de soleil… et peut-être un peu moins de courriers de l'URSSAF dans la boîte aux lettres, je ne vais pas me plaindre.
    </div>

    <div class="conclusion">
        <em>Propos recueillis par Sophie Marchand</em>
        <br>
        <em>Interview réalisée par mail</em>
    </div>

    <div class="about">
        <strong>À propos de Elias Benguezzou</strong>
        Elias Benguezzou est un entrepreneur français basé à Lyon. Fondateur de SayKee, il développe des activités autour du business en ligne et des opportunités digitales.
    </div>
</div>"""
    
    # Update the article
    result = await db.articles.update_one(
        {"title": "Elias Benguezzou : « J'ai commencé avec 500 euros »"},
        {
            "$set": {
                "content": html_content,
                "updated_at": datetime.utcnow()
            }
        }
    )
    
    if result.modified_count > 0:
        print("✅ Article mis à jour avec structure HTML formatée!")
        print("🎨 Questions en blocs colorés")
        print("💬 Réponses bien espacées")
        print("📝 Format interview professionnel")
    else:
        print("⚠️ Aucune modification effectuée")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(update_elias_article_html())
