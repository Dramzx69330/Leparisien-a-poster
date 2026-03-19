# Système de Publication Automatique d'Articles

## Vue d'ensemble
Le système sauvegarde les articles dans MongoDB et les publie automatiquement à raison de **1 article toutes les 2 heures**.

## Architecture

### Base de données MongoDB
- Collection: `articles`
- Champs principaux:
  - `is_published`: Article publié ou non
  - `scheduled_publish_at`: Date de publication programmée
  - `actual_published_at`: Date effective de publication
  - `created_at`: Date de sauvegarde

### Composants

1. **ArticleScheduler** (`/backend/services/article_scheduler.py`)
   - Sauvegarde les articles dans MongoDB
   - Gère la programmation des publications
   - Récupère les articles publiés

2. **AutoPublisher** (`/backend/services/auto_publisher.py`)
   - Tâche de fond qui s'exécute toutes les 2 heures
   - Publie les articles programmés
   - Programme automatiquement le prochain article

3. **Articles Router** (`/backend/routers/articles_router.py`)
   - API pour gérer les articles

## API Endpoints

### POST /api/articles/fetch-and-save
Récupère des articles depuis NewsAPI et les sauvegarde en base de données.
```bash
curl -X POST "http://localhost:8001/api/articles/fetch-and-save?category=crypto&count=50"
```

### GET /api/articles/published
Récupère les articles publiés depuis la base de données.
```bash
curl "http://localhost:8001/api/articles/published?category=crypto&page=1&pageSize=20"
```

### POST /api/articles/schedule-next
Programme manuellement le prochain article pour publication dans 2 heures.
```bash
curl -X POST "http://localhost:8001/api/articles/schedule-next"
```

### POST /api/articles/publish-scheduled
Publie manuellement tous les articles programmés.
```bash
curl -X POST "http://localhost:8001/api/articles/publish-scheduled"
```

### GET /api/articles/stats
Obtient les statistiques sur les articles.
```bash
curl "http://localhost:8001/api/articles/stats"
```

## Workflow

1. **Récupération et sauvegarde**
   ```bash
   # Récupérer 50 articles crypto
   curl -X POST "http://localhost:8001/api/articles/fetch-and-save?category=crypto&count=50"
   
   # Récupérer 50 articles Europe
   curl -X POST "http://localhost:8001/api/articles/fetch-and-save?category=europe&count=50"
   ```

2. **Publication automatique**
   - Le système publie automatiquement 1 article toutes les 2 heures
   - Les articles sont publiés dans l'ordre d'ajout (FIFO)
   - Pas de suppression automatique

3. **Vérification**
   ```bash
   # Voir les statistiques
   curl "http://localhost:8001/api/articles/stats"
   ```

## Fonctionnalités

✅ **Sauvegarde permanente**: Les articles ne sont jamais supprimés
✅ **Publication automatique**: 1 article toutes les 2 heures
✅ **Multi-catégories**: Supporte toutes les catégories (Crypto, Europe, Asie, etc.)
✅ **Programmation**: Articles programmés à l'avance
✅ **Statistiques**: Suivi en temps réel du nombre d'articles

## Maintenance

### Ajouter plus d'articles
```bash
# Ajouter 100 articles de différentes catégories
curl -X POST "http://localhost:8001/api/articles/fetch-and-save?category=crypto&count=30"
curl -X POST "http://localhost:8001/api/articles/fetch-and-save?category=europe&count=30"
curl -X POST "http://localhost:8001/api/articles/fetch-and-save?category=tech&count=40"
```

### Modifier la fréquence de publication
Dans `/backend/services/auto_publisher.py`, ligne 8:
```python
def __init__(self, db, interval_seconds=7200):  # 7200 = 2 heures
```

Pour publier toutes les heures: `interval_seconds=3600`
Pour publier toutes les 30 minutes: `interval_seconds=1800`
Pour publier toutes les 3 heures: `interval_seconds=10800`

## Notes importantes

⚠️ **Pas de suppression automatique**: Les articles restent en base de données indéfiniment
⚠️ **Rechargement**: Le système se relance automatiquement au redémarrage du serveur
⚠️ **Ordre de publication**: Les articles les plus anciens sont publiés en premier (FIFO)
