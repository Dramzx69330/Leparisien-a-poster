import React, { useState, useEffect } from 'react';
import { Clock } from 'lucide-react';
import { Button } from './ui/button';
import { newsAPI } from '../services/api';

const Sidebar = () => {
  const [sidebarArticles, setSidebarArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRecentNews();
  }, []);

  const fetchRecentNews = async () => {
    try {
      setLoading(true);
      const result = await newsAPI.getRecentNews(1, 5);
      if (result.articles) {
        setSidebarArticles(result.articles);
      }
    } catch (error) {
      console.error('Error fetching sidebar news:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <aside className="space-y-6">
      {/* En continu section */}
      <div className="bg-white rounded-lg overflow-hidden border border-gray-200">
        <div className="bg-[#009EE2] text-white px-4 py-3">
          <h2 className="font-bold text-lg">En continu</h2>
        </div>
        <div className="divide-y divide-gray-200">
          {loading ? (
            <div className="p-8 text-center">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-[#009EE2]"></div>
            </div>
          ) : sidebarArticles.length > 0 ? (
            sidebarArticles.map((article) => (
              <article key={article.id} className="p-4 hover:bg-gray-50 cursor-pointer transition-colors group">
                <div className="flex items-start gap-2 mb-2">
                  {article.source && (
                    <span className="px-2 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800">
                      {article.source}
                    </span>
                  )}
                </div>
                <h3 className="font-semibold text-sm text-gray-900 group-hover:text-[#009EE2] transition-colors line-clamp-3 leading-snug">
                  {article.title}
                </h3>
                <div className="flex items-center gap-2 mt-2 text-xs text-gray-500">
                  <Clock size={12} />
                  <span>{article.readTime || '5 min'}</span>
                  {article.timestamp && <span>• {article.timestamp}</span>}
                </div>
              </article>
            ))
          ) : (
            <div className="p-4 text-center text-gray-500">
              Aucun article récent disponible
            </div>
          )}
        </div>
        <div className="p-4 border-t border-gray-200">
          <Button 
            className="w-full bg-[#009EE2] hover:bg-[#0088CC] text-white"
            onClick={fetchRecentNews}
          >
            Actualiser l'info
          </Button>
        </div>
      </div>

      {/* Municipales 2026 Alert */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 overflow-hidden">
        <div className="p-4">
          <div className="flex items-start gap-3">
            <img
              src="https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=100&h=100&fit=crop"
              alt="Municipales 2026"
              className="w-16 h-16 rounded object-cover"
            />
            <div className="flex-1">
              <span className="text-xs font-semibold text-blue-600 uppercase">Municipales 2026</span>
              <h3 className="font-bold text-sm text-gray-900 mt-1 leading-snug">
                S'inscrire aux alertes résultats des élections pour votre ville
              </h3>
              <Button size="sm" variant="link" className="text-blue-600 px-0 mt-1">
                S'inscrire
              </Button>
            </div>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;