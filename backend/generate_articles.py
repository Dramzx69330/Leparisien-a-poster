import json
from datetime import datetime, timedelta
import random

# Templates d'articles par catégorie
article_templates = {
    'europe': [
        "L'économie européenne affiche une croissance de {pct}% au premier trimestre",
        "Bruxelles annonce un nouveau plan de {amount} milliards pour la transition écologique",
        "La BCE maintient ses taux directeurs malgré les pressions inflationnistes",
        "L'Union européenne renforce sa régulation sur {sujet}",
        "Paris et Berlin s'accordent sur une politique commune de {domaine}",
        "Le marché unique européen fête ses {nb} ans d'existence",
        "L'UE impose de nouvelles sanctions contre {pays}",
        "La Commission européenne enquête sur les pratiques de {entreprise}",
        "Zone euro : le chômage atteint son plus bas niveau depuis {nb} ans",
        "L'Europe investit {amount} milliards dans {secteur}",
    ],
    'amerique': [
        "États-Unis : la Fed annonce une pause dans sa politique monétaire",
        "Wall Street termine en hausse malgré les craintes de récession",
        "Le Canada investit {amount} milliards dans les énergies renouvelables",
        "États-Unis : le PIB progresse de {pct}% au dernier trimestre",
        "Silicon Valley : {entreprise} annonce {nb} suppressions de postes",
        "Washington dévoile un plan de {amount} milliards pour {secteur}",
        "Le dollar atteint son plus haut niveau face à l'euro depuis {nb} mois",
        "États-Unis : les ventes au détail progressent de {pct}%",
        "La Maison Blanche annonce de nouvelles mesures sur {sujet}",
        "Amérique latine : la croissance économique s'accélère à {pct}%",
    ],
    'asie': [
        "Chine : la croissance du PIB atteint {pct}% sur un an",
        "Le Japon annonce un plan de relance de {amount} billions de yens",
        "Inde : l'économie numérique affiche une croissance record",
        "La Corée du Sud investit massivement dans les semi-conducteurs",
        "Asie : les exportations progressent de {pct}% en mars",
        "Chine : {entreprise} devient le leader mondial de {secteur}",
        "Le yuan chinois se renforce face au dollar",
        "Vietnam : l'économie attire {amount} milliards d'investissements étrangers",
        "Singapour se positionne comme hub de {secteur}",
        "Indonésie : le gouvernement annonce des réformes économiques majeures",
    ],
    'afrique': [
        "Afrique : la croissance économique prévue à {pct}% en 2026",
        "Le Nigeria lance un ambitieux plan de diversification économique",
        "Afrique du Sud : les énergies renouvelables en plein essor",
        "Le Kenya devient un hub technologique africain majeur",
        "L'Union africaine annonce un fonds de {amount} milliards pour {secteur}",
        "Ghana : l'économie numérique affiche une croissance de {pct}%",
        "Éthiopie : {amount} milliards d'investissements dans {secteur}",
        "Le Maroc se positionne comme porte d'entrée vers l'Afrique",
        "Sénégal : découverte de gisements de {ressource} valorisés à {amount} milliards",
        "Côte d'Ivoire : le cacao atteint des prix records sur les marchés mondiaux",
    ],
    'moyen-orient': [
        "Arabie Saoudite : Vision 2030 franchit une étape clé",
        "Dubaï attire {amount} milliards d'investissements étrangers",
        "Le pétrole brut atteint {price} dollars le baril",
        "Émirats Arabes Unis : l'économie non pétrolière croît de {pct}%",
        "Qatar : {amount} milliards investis dans la transition énergétique",
        "Israël : le secteur tech lève {amount} milliards en 2026",
        "Turquie : l'inflation recule à {pct}% après les mesures du gouvernement",
        "Le Golfe persique mise sur l'économie verte",
        "Iran : les exportations de {ressource} augmentent malgré les sanctions",
        "Bahreïn devient un centre financier régional majeur",
    ],
    'marches': [
        "Les marchés européens terminent en hausse de {pct}%",
        "Le CAC 40 franchit la barre des {nb} points",
        "Wall Street : le Dow Jones progresse de {pct}%",
        "Les actions technologiques rebondissent de {pct}% après le selloff",
        "Le pétrole grimpe de {pct}% sur fond de tensions géopolitiques",
        "L'or atteint un nouveau record à {price} dollars l'once",
        "Les obligations d'État affichent un rendement de {pct}%",
        "Les investisseurs se ruent vers les valeurs {secteur}",
        "Le marché des matières premières en forte hausse",
        "Les bourses asiatiques terminent en ordre dispersé",
    ],
    'crypto': [
        "Bitcoin dépasse les {price} dollars pour la première fois",
        "Ethereum grimpe de {pct}% après l'annonce de {mise_a_jour}",
        "Les cryptomonnaies attirent {amount} milliards d'investissements institutionnels",
        "La SEC approuve {nb} nouveaux ETF crypto",
        "Le marché des NFT rebondit de {pct}% en mars",
        "Solana devient la {nb}ème blockchain par capitalisation",
        "Les stablecoins représentent désormais {amount} milliards de dollars",
        "Binance annonce l'intégration de {nouvelle_fonctionnalité}",
        "Le Lightning Network traite {nb} millions de transactions quotidiennes",
        "L'adoption crypto progresse de {pct}% en un an",
    ],
    'tech': [
        "Apple annonce un chiffre d'affaires record de {amount} milliards",
        "Google investit {amount} milliards dans l'intelligence artificielle",
        "Microsoft lance {nouveau_produit} pour concurrencer {concurrent}",
        "Meta dévoile sa vision du métaverse avec {montant} milliards d'investissement",
        "Amazon Web Services domine le marché du cloud avec {pct}% de parts",
        "Les semi-conducteurs : pénurie prévue jusqu'en 2027",
        "Samsung investit {amount} milliards dans les écrans pliables",
        "La 6G pourrait arriver dès 2028 selon {entreprise}",
        "Tesla livre {nb} véhicules au premier trimestre",
        "L'IA générative représente un marché de {amount} milliards en 2026",
    ],
    'commerce': [
        "Le e-commerce mondial atteint {amount} trillions de dollars",
        "Amazon ouvre {nb} nouveaux centres logistiques en Europe",
        "Alibaba affiche une croissance de {pct}% au dernier trimestre",
        "Le commerce transfrontalier progresse de {pct}% en 2026",
        "Les PME investissent massivement dans la digitalisation",
        "Le retail physique se réinvente avec {technologie}",
        "Les marketplaces représentent {pct}% du e-commerce mondial",
        "La livraison en {nb} heures devient la norme",
        "Le social commerce explose avec {amount} milliards de transactions",
        "Les paiements digitaux progressent de {pct}% en un an",
    ]
}

# Générer des contenus réalistes
def generate_content(category, title):
    base_content = f"""<p>{title}</p>

<p>Cette évolution majeure marque un tournant pour le secteur. Les analystes s'accordent à dire que cette tendance devrait se poursuivre dans les mois à venir.</p>

<p><strong>Contexte économique</strong></p>

<p>Dans un contexte de reprise post-pandémique, les investisseurs manifestent un regain d'intérêt pour ce segment. Les fondamentaux économiques restent solides malgré les incertitudes géopolitiques.</p>

<p><strong>Impact sur les marchés</strong></p>

<p>Cette annonce a immédiatement été saluée par les marchés financiers. Les principales bourses ont réagi positivement à cette nouvelle, reflétant l'optimisme des investisseurs.</p>

<p><strong>Perspectives</strong></p>

<p>Les experts prévoient une consolidation de cette tendance au cours du deuxième trimestre. Plusieurs facteurs structurels soutiennent cette dynamique positive.</p>

<p><strong>Réactions des acteurs du marché</strong></p>

<p>Les principaux acteurs du secteur ont accueilli favorablement cette évolution. Plusieurs entreprises ont d'ores et déjà annoncé des plans d'investissement pour capitaliser sur cette opportunité.</p>"""
    
    return base_content

# Charger articles existants
with open('/app/backend/data/articles.json', 'r') as f:
    articles = json.load(f)

# Compter articles par catégorie
from collections import Counter
categories_count = Counter([a['category'] for a in articles if a.get('is_published')])

# Créer articles
new_articles = []
article_id = 10000

for category, templates in article_templates.items():
    current_count = categories_count.get(category, 0)
    needed = 15 - current_count
    
    if needed > 0:
        print(f"Création de {needed} articles pour {category}...")
        
        for i in range(needed):
            # Choisir un template
            template = templates[i % len(templates)]
            
            # Remplacer les variables
            title = template.format(
                pct=round(random.uniform(1.5, 8.5), 1),
                amount=random.randint(5, 500),
                nb=random.randint(3, 50),
                price=random.randint(2000, 90000),
                sujet=random.choice(['les réseaux sociaux', 'le numérique', 'la tech', 'la finance']),
                domaine=random.choice(['santé', 'énergie', 'défense', 'éducation']),
                pays=random.choice(['la Russie', 'la Chine', 'la Corée du Nord']),
                entreprise=random.choice(['Google', 'Apple', 'Microsoft', 'Meta']),
                secteur=random.choice(['la tech', 'les énergies', 'la santé', "l'automobile"]),
                ressource=random.choice(['pétrole', 'gaz', 'lithium', 'cobalt']),
                mise_a_jour=random.choice(['Prague', 'Dencun', 'Shapella']),
                nouvelle_fonctionnalité=random.choice(['le staking', 'les NFT', 'le trading P2P']),
                nouveau_produit=random.choice(['Copilot Pro', 'Azure AI', 'Office 365 AI']),
                concurrent=random.choice(['OpenAI', 'Google', 'Meta']),
                montant=random.randint(10, 100),
                technologie=random.choice(['la réalité augmentée', "l'IA", 'les robots', 'la 5G'])
            )
            
            # Générer dates étalées
            days_ago = random.randint(1, 20)
            pub_date = datetime.utcnow() - timedelta(days=days_ago)
            
            if days_ago == 0:
                timestamp = "Il y a quelques heures"
            elif days_ago == 1:
                timestamp = "Il y a 1 jour"
            elif days_ago < 7:
                timestamp = f"Il y a {days_ago} jours"
            else:
                weeks = days_ago // 7
                timestamp = f"Il y a {weeks} semaine{'s' if weeks > 1 else ''}"
            
            article = {
                "id": f"article-{category}-{article_id}",
                "news_api_id": article_id,
                "title": title,
                "excerpt": f"{title[:120]}...",
                "content": generate_content(category, title),
                "image": f"https://images.unsplash.com/photo-{random.choice(['1504711434969', '1518546305927', '1454165804606', '1526304640581', '1579532537598'])}?w=1200&h=800&fit=crop",
                "url": f"https://charge-preview.preview.emergentagent.com/article/article-{category}-{article_id}",
                "source": random.choice(['Reuters', 'Bloomberg', 'Financial Times', 'Le Figaro', 'Les Échos']),
                "category": category,
                "publishedAt": pub_date.isoformat(),
                "readTime": f"{random.randint(3, 7)} min",
                "timestamp": timestamp,
                "is_published": True,
                "protected": False,
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat()
            }
            
            new_articles.append(article)
            article_id += 1

# Ajouter à la liste
articles.extend(new_articles)

# Sauvegarder
with open('/app/backend/data/articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"\n✅ {len(new_articles)} articles créés!")
print(f"📊 Total articles: {len(articles)}")

# Nouvelle distribution
categories_count = Counter([a['category'] for a in articles if a.get('is_published')])
print(f"\n📊 Nouvelle distribution:")
for cat, count in sorted(categories_count.items()):
    print(f"   {cat:15s}: {count:2d} articles")
