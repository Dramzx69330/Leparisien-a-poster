# Système de Gestion des Articles

## 📁 Stockage

Tous les articles sont stockés dans le fichier `/backend/data/articles.json`.

**Avantages:**
- ✅ Pas besoin de base de données
- ✅ Facile à versionner sur GitHub
- ✅ Portable (tout est dans le code)
- ✅ Facile à backup et restaurer

## 🔄 Publication Automatique

Le système publie automatiquement **1 article toutes les 2 heures**.

**Fonctionnement:**
1. Les articles non publiés sont dans `articles.json` avec `is_published: false`
2. Toutes les 2h, le système passe 1 article à `is_published: true`
3. Les articles publiés apparaissent immédiatement sur le site

**Configuration:** Voir `/backend/services/file_auto_publisher.py`

## 🔒 Article Protégé

L'article **"Portrait d'un jeune entrepreneur : « Internet a changé les règles »"** est protégé:
- Flag `protected: true` dans le fichier JSON
- Ne sera jamais modifié automatiquement
- Ne sera jamais supprimé

## 📊 Structure d'un Article

```json
{
  "id": "unique-id",
  "title": "Titre de l'article",
  "excerpt": "Résumé court",
  "content": "<html>Contenu complet</html>",
  "image": "URL de l'image",
  "url": "URL source",
  "source": "Le Parisien",
  "category": "economie",
  "publishedAt": "2026-03-12T08:30:00",
  "timestamp": "Il y a 7 jours",
  "is_published": true,
  "protected": false,
  "created_at": "2026-03-12T08:30:00",
  "updated_at": "2026-03-12T08:30:00"
}
```

## 🚀 Déploiement

### Sur GitHub

Tous les fichiers nécessaires sont dans le repo:
```
/app/
├── backend/
│   ├── data/
│   │   └── articles.json       ← Articles stockés ici
│   ├── services/
│   │   ├── file_article_service.py
│   │   └── file_auto_publisher.py
│   └── routers/
│       └── articles_file_router.py
└── frontend/
```

### Installation

1. Cloner le repo
2. Installer les dépendances:
   ```bash
   cd backend && pip install -r requirements.txt
   cd frontend && yarn install
   ```
3. Les articles sont déjà dans `/backend/data/articles.json`
4. Démarrer l'app - la publication automatique démarre automatiquement

## 🛠️ Gestion des Articles

### Ajouter des articles

Modifier `/backend/data/articles.json` directement ou utiliser l'API:

```python
from services.file_article_service import file_article_service

article = {
    "id": "mon-article",
    "title": "Mon titre",
    "content": "Mon contenu",
    # ... autres champs
}

file_article_service.add_article(article)
```

### Modifier un article

```python
file_article_service.update_article("mon-article", {
    "title": "Nouveau titre"
})
```

### Supprimer un article

```python
file_article_service.delete_article("mon-article")
```

**Note:** Les articles protégés ne peuvent pas être modifiés ou supprimés.

## 📈 Statistiques

API: `GET /api/articles/stats`

Retourne:
```json
{
  "status": "ok",
  "published": 14,
  "unpublished": 18,
  "scheduled": 0,
  "total": 32
}
```

## 🔍 Recherche

API: `GET /api/news/search?q=entrepreneur`

Recherche dans tous les articles publiés (titre, excerpt, contenu).

## ⚙️ Configuration

### Intervalle de publication

Modifier dans `/backend/services/file_auto_publisher.py`:
```python
FileAutoPublisher(interval_hours=2.0)  # Changez 2.0 à votre convenance
```

### Protéger un article

Dans `articles.json`, ajouter:
```json
{
  "id": "mon-article",
  "protected": true,
  "permanent": true
}
```
