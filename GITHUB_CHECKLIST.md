# Checklist GitHub - Clone Le Parisien

## ✅ Fichiers Essentiels

### Backend
- [x] `/backend/data/articles.json` - 136 articles (254KB)
- [x] `/backend/data/README.md` - Documentation articles
- [x] `/backend/services/file_article_service.py` - Service articles
- [x] `/backend/services/file_auto_publisher.py` - Publication auto
- [x] `/backend/routers/articles_file_router.py` - API articles
- [x] `/backend/server.py` - Serveur FastAPI
- [x] `/backend/requirements.txt` - Dépendances Python

### Frontend
- [x] `/frontend/src/` - Code source React
- [x] `/frontend/public/` - Assets publics
- [x] `/frontend/package.json` - Dépendances Node
- [x] `/frontend/.env` - Variables d'environnement (template)

### Documentation
- [x] `/README.md` - Documentation principale
- [x] `/setup.sh` - Script d'installation
- [x] `/.gitignore` - Fichiers à ignorer

## 📊 Contenu

### Articles
- [x] 136 articles publiés
- [x] 15 articles minimum par catégorie
- [x] Images réelles (Unsplash + Pexels)
- [x] Contenu complet et varié
- [x] Dates étalées sur 20 jours

### Catégories (15 articles chacune)
- [x] Europe
- [x] Amérique
- [x] Asie
- [x] Afrique
- [x] Moyen-Orient
- [x] Marchés
- [x] Crypto
- [x] Tech & Innovation
- [x] Commerce International

### Article Protégé
- [x] "Portrait d'un jeune entrepreneur : « Internet a changé les règles »"
- [x] Flag `protected: true` dans JSON
- [x] Contenu complet interview

## 🔧 Fonctionnalités

### Backend
- [x] API REST complète
- [x] Publication automatique (toutes les 2h)
- [x] Recherche dans articles
- [x] Filtrage par catégorie
- [x] Statistiques

### Frontend
- [x] Interface responsive
- [x] Navigation par catégorie
- [x] Recherche avancée
- [x] Page détail article
- [x] Optimisation mobile

## 🎨 Design

- [x] Logo Le Parisien
- [x] Couleurs officielles (#009EE2, #FFC300)
- [x] Typographie cohérente
- [x] Layout responsive
- [x] Images professionnelles

## 📱 Mobile

- [x] Header adaptatif
- [x] Grille responsive
- [x] Sidebar cachée mobile
- [x] Zones tactiles optimisées
- [x] Tailles de texte adaptatives

## 🔒 Sécurité

- [x] Variables d'environnement
- [x] Pas de clés en dur
- [x] CORS configuré
- [x] Input sanitization

## 📦 Déploiement

- [x] Compatible Heroku
- [x] Compatible Railway
- [x] Compatible Vercel (frontend)
- [x] Compatible Render
- [x] Documentation déploiement

## ✅ Tests de Vérification

### Avant Push GitHub

```bash
# 1. Vérifier que articles.json existe
ls -lh backend/data/articles.json

# 2. Vérifier le contenu
cat backend/data/articles.json | python3 -m json.tool | head -50

# 3. Compter les articles
cat backend/data/articles.json | python3 -c "import json, sys; data=json.load(sys.stdin); print(f'{len(data)} articles')"

# 4. Vérifier les catégories
cat backend/data/articles.json | python3 -c "import json, sys; from collections import Counter; data=json.load(sys.stdin); cats=Counter([a['category'] for a in data]); [print(f'{k}: {v}') for k,v in sorted(cats.items())]"

# 5. Vérifier l'article protégé
cat backend/data/articles.json | python3 -c "import json, sys; data=json.load(sys.stdin); protected=[a for a in data if a.get('protected')]; print(f'{len(protected)} article(s) protégé(s)'); [print(a['title']) for a in protected]"
```

### Résultats Attendus

```
✅ backend/data/articles.json: 254KB
✅ 136 articles au total
✅ 15 articles par catégorie
✅ 1 article protégé: "Portrait d'un jeune entrepreneur..."
✅ 18 images uniques
```

## 🚀 Commandes Git

```bash
# 1. Vérifier les fichiers à commiter
git status

# 2. Ajouter tous les fichiers
git add .

# 3. Vérifier que articles.json est inclus
git status | grep articles.json

# 4. Commit
git commit -m "Clone Le Parisien - 136 articles avec images réelles"

# 5. Push
git push origin main
```

## 📝 Notes Importantes

### À INCLURE sur GitHub
- ✅ `/backend/data/articles.json` - **ESSENTIEL**
- ✅ `/backend/data/README.md`
- ✅ Tous les fichiers `.py`
- ✅ `README.md`
- ✅ `requirements.txt` et `package.json`

### À EXCLURE sur GitHub
- ❌ `*.env` (sauf templates)
- ❌ `node_modules/`
- ❌ `__pycache__/`
- ❌ `.venv/`
- ❌ `build/`

### Variables d'environnement

Créer des templates `.env.example`:

**backend/.env.example:**
```env
MONGO_URL=mongodb://localhost:27017
NEWS_API_KEY=your_key_here
NEWS_API_BASE_URL=https://newsapi.org/v2
```

**frontend/.env.example:**
```env
REACT_APP_BACKEND_URL=http://localhost:8001/api
WDS_SOCKET_PORT=443
ENABLE_HEALTH_CHECK=false
```

## ✅ Checklist Finale

Avant de pusher sur GitHub, vérifier:

- [ ] `articles.json` contient 136 articles
- [ ] Article protégé présent avec `protected: true`
- [ ] README.md à jour
- [ ] .gitignore ne bloque PAS `backend/data/`
- [ ] setup.sh est exécutable
- [ ] requirements.txt à jour
- [ ] package.json à jour
- [ ] Pas de clés API en dur
- [ ] Code commenté et propre

## 🎉 Prêt pour GitHub!

Une fois tous les checks validés, le projet est prêt à être poussé sur GitHub.

**Taille estimée du repo:** ~5-10MB (incluant node_modules exclu)
**Taille articles.json:** 254KB
**Total articles:** 136
**Images:** 18 uniques (URLs externes)
