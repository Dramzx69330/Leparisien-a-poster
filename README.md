# Clone Le Parisien - Actualités Économiques

Un clone du site Le Parisien spécialisé dans l'actualité économique et financière.

## 🚀 Fonctionnalités

### Articles
- ✅ **136 articles** publiés couvrant 9 catégories
- ✅ **15 articles minimum par catégorie**
- ✅ Contenu complet et images professionnelles
- ✅ Stockés en fichier JSON (pas de base de données nécessaire)

### Catégories
- Europe (15 articles)
- Amérique (15 articles)  
- Asie (15 articles)
- Afrique (15 articles)
- Moyen-Orient (15 articles)
- Marchés (15 articles)
- Crypto (15 articles)
- Tech & Innovation (15 articles)
- Commerce International (15 articles)

### Publication Automatique
- 🔄 Publication automatique toutes les 2 heures
- 📅 Système de queue pour articles en attente
- 🔒 Articles protégés ne sont jamais modifiés

### Interface
- 📱 **Optimisée mobile** - Responsive design
- 🔍 **Recherche avancée** - Recherche dans tous les articles
- 📰 **Navigation par catégorie** - Filtrage facile
- 🎨 **Design Le Parisien** - Logo et couleurs officiels

## 📁 Structure du Projet

```
/app/
├── backend/
│   ├── data/
│   │   ├── articles.json          ← 136 articles (254KB)
│   │   └── README.md              ← Documentation articles
│   ├── services/
│   │   ├── file_article_service.py    ← Gestion articles (fichiers)
│   │   ├── file_auto_publisher.py     ← Publication automatique
│   │   ├── news_service.py            ← Service NewsAPI
│   │   └── scraper_service.py         ← Scraping contenu
│   ├── routers/
│   │   ├── articles_file_router.py    ← API articles
│   │   └── news_router.py             ← API news & recherche
│   ├── server.py                  ← Serveur FastAPI
│   └── requirements.txt           ← Dépendances Python
├── frontend/
│   ├── src/
│   │   ├── components/           ← Composants React
│   │   ├── pages/                ← Pages (Home, ArticleDetail)
│   │   ├── services/             ← API client
│   │   └── App.js                ← Application principale
│   ├── public/
│   └── package.json              ← Dépendances Node.js
└── README.md                      ← Ce fichier
```

## 🛠️ Installation

### Prérequis
- Python 3.8+
- Node.js 16+
- Yarn

### 1. Cloner le repo
```bash
git clone <votre-repo>
cd app
```

### 2. Backend
```bash
cd backend
pip install -r requirements.txt
```

### 3. Frontend
```bash
cd frontend
yarn install
```

### 4. Variables d'environnement

**Backend** (`backend/.env`):
```env
MONGO_URL=mongodb://localhost:27017  # Optionnel (pour historique uniquement)
NEWS_API_KEY=votre_cle_newsapi      # Optionnel
NEWS_API_BASE_URL=https://newsapi.org/v2
```

**Frontend** (`frontend/.env`):
```env
REACT_APP_BACKEND_URL=http://localhost:8001/api
WDS_SOCKET_PORT=443
ENABLE_HEALTH_CHECK=false
```

## 🚀 Démarrage

### Développement

**Backend:**
```bash
cd backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

**Frontend:**
```bash
cd frontend
yarn start
```

### Production

Utiliser supervisor (fichiers de config inclus) ou:

```bash
# Backend
cd backend
uvicorn server:app --host 0.0.0.0 --port 8001

# Frontend
cd frontend
yarn build
serve -s build -p 3000
```

## 📊 Système d'Articles

### Stockage en Fichier JSON

Tous les articles sont dans **`/backend/data/articles.json`**:
- ✅ Pas besoin de MongoDB pour les articles
- ✅ Versionnable sur Git
- ✅ Portable et facile à déployer
- ✅ 254KB de données

### Structure d'un Article

```json
{
  "id": "unique-id",
  "title": "Titre de l'article",
  "excerpt": "Résumé",
  "content": "<html>Contenu complet</html>",
  "image": "URL de l'image Unsplash/Pexels",
  "url": "URL de l'article",
  "source": "Le Parisien / Reuters / Bloomberg",
  "category": "europe / amerique / asie / etc.",
  "publishedAt": "2026-03-12T08:30:00",
  "timestamp": "Il y a 7 jours",
  "readTime": "5 min",
  "is_published": true,
  "protected": false,
  "created_at": "2026-03-12T08:30:00",
  "updated_at": "2026-03-12T08:30:00"
}
```

### Publication Automatique

Le système publie automatiquement **1 article toutes les 2 heures**.

**Configuration** dans `/backend/services/file_auto_publisher.py`:
```python
FileAutoPublisher(interval_hours=2.0)  # Modifier ici
```

### Article Protégé

L'article **"Portrait d'un jeune entrepreneur : « Internet a changé les règles »"** est protégé:
- Flag `protected: true` dans le JSON
- Ne sera **jamais modifié** automatiquement
- Ne sera **jamais supprimé**

## 🎨 Optimisations Mobile

Le site est entièrement optimisé pour mobile:
- 📱 Header adaptatif (logo, boutons)
- 📊 Grille responsive
- 📰 Sidebar cachée sur mobile
- 👆 Zones tactiles optimisées
- ⚡ Chargement rapide

**Breakpoints:**
- Mobile: < 640px
- Tablet: ≥ 640px
- Desktop: ≥ 1024px

## 🔍 API Endpoints

### Articles

**GET** `/api/articles/published`
- Récupérer les articles publiés
- Query params: `category`, `page`, `pageSize`

**GET** `/api/articles/stats`
- Statistiques des articles

**GET** `/api/articles/{article_id}`
- Récupérer un article spécifique

### Recherche

**GET** `/api/news/search?q=keyword`
- Rechercher dans tous les articles publiés
- Recherche dans titre, excerpt, contenu

## 📝 Gestion des Articles

### Ajouter des Articles

1. **Modifier directement** `/backend/data/articles.json`
2. **Ou via API** (créer un endpoint si nécessaire)

### Protéger un Article

Dans `articles.json`:
```json
{
  "id": "mon-article",
  "protected": true,
  "permanent": true
}
```

### Publier/Dépublier

Changer le flag `is_published` dans le JSON.

## 🌐 Déploiement

### Heroku / Railway / Render

1. Push sur GitHub
2. Connecter le repo à la plateforme
3. Variables d'env configurées
4. Deploy automatique

### Vercel (Frontend uniquement)

```bash
cd frontend
vercel deploy
```

### Configuration Nginx (Production)

```nginx
# Backend
location /api {
    proxy_pass http://localhost:8001;
}

# Frontend
location / {
    root /path/to/frontend/build;
    try_files $uri /index.html;
}
```

## 📸 Images

Toutes les images proviennent de:
- **Unsplash** (18 images professionnelles)
- **Pexels** (2 images)

Thèmes: Business, Finance, Économie, Bourse, Actualités

## 🔒 Article Protégé

**"Portrait d'un jeune entrepreneur : « Internet a changé les règles »"**

Cet article est **protégé** et ne sera **jamais modifié**:
- Interview exclusive
- Contenu complet et structuré
- Format question-réponse professionnel
- Source: Le Parisien
- Date: 12 mars 2026

## 🛡️ Sécurité

- ✅ Pas de mots de passe en dur
- ✅ Variables d'environnement
- ✅ CORS configuré
- ✅ Rate limiting (FastAPI)
- ✅ Input sanitization

## 🧪 Tests

```bash
# Backend
cd backend
pytest

# Frontend  
cd frontend
yarn test
```

## 📄 Licence

Ce projet est un clone éducatif du Parisien.

## 👨‍💻 Auteur

Développé avec ❤️ en 2026

## 🎯 Prochaines Étapes

- [ ] Ajouter authentification utilisateur
- [ ] Système de commentaires
- [ ] Newsletter
- [ ] Mode sombre
- [ ] PWA (Progressive Web App)
- [ ] Analytics

## 🆘 Support

Pour toute question, ouvrir une issue sur GitHub.

---

**Note:** Les articles sont stockés en fichier JSON, pas besoin de base de données! 🎉
