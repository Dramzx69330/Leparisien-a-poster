import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Navigation from './components/Navigation';
import ArticleCard from './components/ArticleCard';
import Sidebar from './components/Sidebar';
import SubscriptionBanner from './components/SubscriptionBanner';
import SearchModal from './components/SearchModal';
import MobileMenu from './components/MobileMenu';
import { newsAPI } from './services/api';
import { getCategoryForAPI } from './utils/categoryMapper';
import './App.css';

function App() {
  const [activeCategory, setActiveCategory] = useState('À la une');
  const [showBanner, setShowBanner] = useState(true);
  const [searchOpen, setSearchOpen] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';
    // Load initial articles
    fetchArticles();
  }, []);

  const fetchArticles = async (category = null) => {
    try {
      setLoading(true);
      setError(null);
      
      const apiCategory = getCategoryForAPI(category || activeCategory);
      const result = await newsAPI.getTopHeadlines(apiCategory, 1, 20);
      
      if (result.articles && result.articles.length > 0) {
        setArticles(result.articles);
      } else {
        setError("Aucun article disponible pour le moment.");
      }
    } catch (err) {
      console.error('Error fetching articles:', err);
      setError("Erreur lors du chargement des articles. Veuillez réessayer.");
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryChange = (category) => {
    setActiveCategory(category);
    fetchArticles(category);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleLogoClick = () => {
    setActiveCategory('À la une');
    fetchArticles(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <Header 
        onMenuClick={() => setMenuOpen(true)}
        onSearchClick={() => setSearchOpen(true)}
        onLogoClick={handleLogoClick}
      />

      {/* Navigation */}
      <Navigation 
        activeCategory={activeCategory}
        onCategoryChange={handleCategoryChange}
      />

      {/* Main Content */}
      <main className="max-w-[1400px] mx-auto px-4 py-8">
        {loading ? (
          <div className="flex items-center justify-center py-20">
            <div className="text-center">
              <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-[#009EE2]"></div>
              <p className="mt-4 text-gray-600">Chargement des actualités...</p>
            </div>
          </div>
        ) : error ? (
          <div className="flex items-center justify-center py-20">
            <div className="text-center">
              <p className="text-red-600 font-semibold">{error}</p>
              <button 
                onClick={() => fetchArticles()}
                className="mt-4 px-6 py-2 bg-[#009EE2] text-white rounded hover:bg-[#0088CC] transition-colors"
              >
                Réessayer
              </button>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Articles Grid */}
            <div className="lg:col-span-2">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Featured Article */}
                {articles[0] && (
                  <div className="md:col-span-2">
                    <ArticleCard article={articles[0]} size="large" />
                  </div>
                )}

                {/* Related articles below featured */}
                {articles.length > 2 && (
                  <div className="md:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-4 py-4 border-y border-gray-200">
                    {articles.slice(1, 3).map((article) => (
                      <div key={article.id} className="flex gap-3 hover:bg-white p-3 rounded transition-colors cursor-pointer group">
                        <div className="flex-1">
                          {article.source && (
                            <span className="inline-block px-2 py-0.5 rounded text-xs font-bold mb-2 bg-gray-100 text-gray-800">
                              {article.source}
                            </span>
                          )}
                          <h3 className="font-bold text-sm text-gray-900 group-hover:text-[#009EE2] transition-colors line-clamp-3">
                            {article.title}
                          </h3>
                        </div>
                        {article.image && (
                          <img 
                            src={article.image} 
                            alt="" 
                            className="w-24 h-24 object-cover rounded flex-shrink-0"
                            onError={(e) => {
                              e.target.style.display = 'none';
                            }}
                          />
                        )}
                      </div>
                    ))}
                  </div>
                )}

                {/* Grid articles */}
                {articles.slice(3).map((article) => (
                  <ArticleCard key={article.id} article={article} size="medium" />
                ))}
              </div>

              {/* Load More */}
              {articles.length >= 10 && (
                <div className="mt-8 text-center">
                  <button 
                    onClick={() => fetchArticles()}
                    className="px-8 py-3 bg-white border-2 border-gray-300 rounded font-semibold text-gray-700 hover:border-[#009EE2] hover:text-[#009EE2] transition-all"
                  >
                    Voir plus d'articles
                  </button>
                </div>
              )}
            </div>

            {/* Sidebar */}
            <div className="lg:col-span-1">
              <div className="sticky top-32">
                <Sidebar />
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Subscription Banner */}
      {showBanner && (
        <SubscriptionBanner onClose={() => setShowBanner(false)} />
      )}

      {/* Search Modal */}
      <SearchModal isOpen={searchOpen} onClose={() => setSearchOpen(false)} />

      {/* Mobile Menu */}
      <MobileMenu isOpen={menuOpen} onClose={() => setMenuOpen(false)} />
    </div>
  );
}

export default App;