# Le Parisien Clone - API Contracts

## Backend Implementation Plan

### 1. API Endpoints

#### GET /api/news/top-headlines
Récupère les articles à la une en français
- **Query Parameters:**
  - `category` (optional): Catégorie d'actualités (business, entertainment, health, science, sports, technology)
  - `page` (optional): Numéro de page (default: 1)
  - `pageSize` (optional): Nombre d'articles par page (default: 20)
- **Response:**
```json
{
  "articles": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "url": "string",
      "urlToImage": "string",
      "publishedAt": "string",
      "source": { "name": "string" },
      "category": "string"
    }
  ],
  "totalResults": "number"
}
```

#### GET /api/news/search
Recherche d'articles par mot-clé
- **Query Parameters:**
  - `q`: Mot-clé de recherche (required)
  - `page` (optional): Numéro de page
  - `pageSize` (optional): Nombre de résultats
- **Response:** Same structure as top-headlines

#### GET /api/news/category/:category
Récupère les articles par catégorie spécifique
- **Path Parameters:**
  - `category`: Catégorie (international, economie, societe, sports, culture)
- **Response:** Same structure as top-headlines

### 2. Data Mapping

#### Mock Data → Real API Data
Current mock fields will be replaced with NewsAPI data:
- `mockArticles.title` → `newsapi.title`
- `mockArticles.excerpt` → `newsapi.description`
- `mockArticles.image` → `newsapi.urlToImage`
- `mockArticles.timestamp` → Calculated from `newsapi.publishedAt`
- `mockArticles.category` → Derived from request category or source

### 3. Frontend Integration Changes

#### Files to Update:
1. **App.js**
   - Add API calls to fetch real articles
   - Replace `mockArticles` with API response
   - Add loading states and error handling
   - Implement category filtering with API calls

2. **SearchModal.jsx**
   - Connect search input to `/api/news/search` endpoint
   - Display real search results

3. **Remove Mock Data**
   - Keep `mockData.js` structure but fetch from API instead

### 4. Backend Implementation Details

#### Environment Variables (.env):
- `NEWS_API_KEY`: 13eeeaebcc1d4c5e9216ec4ebfccc6c6
- `NEWS_API_BASE_URL`: https://newsapi.org/v2

#### Dependencies to Add:
- `httpx` or use existing `requests` for API calls
- Cache mechanism (optional) to avoid rate limits

#### Error Handling:
- API rate limit handling (100 requests/day on free plan)
- Fallback to cached data if API fails
- User-friendly error messages

### 5. Category Mapping

Le Parisien Categories → NewsAPI Categories:
- "À la une" → top-headlines (general)
- "International" → category=general, international sources
- "Économie" → category=business
- "Société" → category=general
- "Sports" → category=sports
- "Culture" → category=entertainment
- "En continu" → Everything endpoint with recency sort

### 6. Implementation Order

1. ✅ Frontend with mock data created
2. ⏳ Backend API endpoints creation
3. ⏳ NewsAPI integration
4. ⏳ Frontend API integration
5. ⏳ Error handling and loading states
6. ⏳ Testing complete flow
