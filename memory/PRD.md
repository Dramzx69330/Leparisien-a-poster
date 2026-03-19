# PRD - Portail Économique Mondial (Style Le Parisien)

## Description du projet
Clone du site Le Parisien transformé en portail d'actualités économiques mondiales. L'application affiche des articles économiques par région (Europe, Asie, etc.) et par thème (Crypto, Marchés, etc.).

## Architecture technique

### Frontend (React)
- **Framework:** React avec React Router
- **Styling:** Tailwind CSS + Shadcn UI
- **État:** SessionStorage pour les articles consultés
- **Fichiers clés:**
  - `/app/frontend/src/App.js` - Page principale
  - `/app/frontend/src/pages/ArticleDetail.jsx` - Détail article avec rendu HTML
  - `/app/frontend/src/components/` - Header, Navigation, ArticleCard, etc.

### Backend (FastAPI)
- **Framework:** FastAPI (Python)
- **Base de données:** MongoDB (Motor async driver)
- **Services:**
  - `news_service.py` - Intégration NewsAPI
  - `scraper_service.py` - Web scraping (BeautifulSoup)
  - `auto_publisher.py` - Publication automatique (1 article/2h)

### Base de données (MongoDB)
- **Collection `articles`:**
  - `id`, `title`, `excerpt`, `content` (HTML), `source`, `author`
  - `url`, `imageUrl`, `publishedAt`, `category`
  - `status` ('unpublished', 'scheduled', 'published')
  - `scheduled_for`, `actual_published_at`, `created_at`, `updated_at`

## Fonctionnalités implémentées

### ✅ Complétées
1. **Clone UI Le Parisien** - Interface fidèle au site original
2. **Pivot économique** - Catégories régionales et thématiques
3. **Intégration NewsAPI** - Récupération d'articles économiques
4. **Web scraping** - Contenu complet des articles
5. **Système de publication** - Auto-publication toutes les 2h
6. **Articles personnalisés:**
   - Article professionnel "Elias Benguezzou"
   - Interview premium "SayKee" avec formatage Q&A HTML
7. **Navigation catégories** - Depuis l'article et l'accueil
8. **Articles similaires** - Section en bas de chaque article
9. **Partage d'article** - Bouton copier le lien

### 📅 Mise à jour - 19 Mars 2026
- **Formatage Q&A professionnel:** L'article SayKee utilise maintenant du HTML avec CSS inline pour distinguer clairement les questions (fond bleu, bordure) des réponses (texte noir)
- **Rendu HTML sécurisé:** `ArticleDetail.jsx` utilise `dangerouslySetInnerHTML` avec des styles CSS définis

## APIs clés

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/articles/published` | GET | Articles publiés (pagination, catégorie) |
| `/api/news/scrape-article` | POST | Scrape contenu article externe |
| `/api/articles/fetch-and-save` | POST | Import NewsAPI → MongoDB |
| `/api/articles/stats` | GET | Statistiques publication |

## Intégrations tierces
- **NewsAPI.org** - Source d'articles (clé API dans `/app/backend/.env`)

## Structure des fichiers
```
/app
├── backend/
│   ├── server.py (FastAPI main)
│   ├── models/article.py
│   ├── routers/articles_router.py, news_router.py
│   ├── services/auto_publisher.py, scraper_service.py
│   └── update_saykee_final_version.py (script mise à jour article)
├── frontend/
│   ├── src/App.js
│   ├── src/pages/ArticleDetail.jsx
│   └── src/components/
└── memory/PRD.md
```

## Backlog (P2)
- [ ] Corriger warnings ESLint (hooks dependencies dans App.js, SearchModal.jsx)
- [ ] Interface admin pour gestion articles
- [ ] Système de commentaires
- [ ] Newsletter/abonnements

## Notes techniques
- Le contenu des articles peut contenir du HTML (classes: `.question`, `.answer`, `.intro`, `.conclusion`)
- Le frontend rend le HTML avec `dangerouslySetInnerHTML` - contenu contrôlé uniquement
