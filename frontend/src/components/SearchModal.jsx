import React, { useState, useEffect } from 'react';
import { Search, X, Clock } from 'lucide-react';
import { Dialog, DialogContent, DialogHeader } from './ui/dialog';
import { Input } from './ui/input';
import { Button } from './ui/button';
import { newsAPI } from '../services/api';

const SearchModal = ({ isOpen, onClose }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [searching, setSearching] = useState(false);

  useEffect(() => {
    if (searchQuery.length > 2) {
      const delaySearch = setTimeout(() => {
        handleSearch();
      }, 500);
      return () => clearTimeout(delaySearch);
    } else {
      setSearchResults([]);
    }
  }, [searchQuery]);

  const handleSearch = async () => {
    if (searchQuery.length < 3) return;

    try {
      setSearching(true);
      const result = await newsAPI.searchArticles(searchQuery, 1, 10);
      if (result.articles) {
        setSearchResults(result.articles);
      }
    } catch (error) {
      console.error('Search error:', error);
    } finally {
      setSearching(false);
    }
  };

  const handlePopularSearch = (term) => {
    setSearchQuery(term);
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-3xl max-h-[80vh] overflow-hidden flex flex-col">
        <DialogHeader>
          <div className="flex items-center gap-3 pb-4 border-b">
            <Search size={24} className="text-gray-400" />
            <Input
              type="text"
              placeholder="Rechercher un article, un thème..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="border-0 text-lg focus-visible:ring-0 focus-visible:ring-offset-0"
              autoFocus
            />
          </div>
        </DialogHeader>
        <div className="py-6 overflow-y-auto flex-1">
          {searching ? (
            <div className="text-center py-8">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-[#009EE2]"></div>
              <p className="mt-2 text-gray-500">Recherche en cours...</p>
            </div>
          ) : searchResults.length > 0 ? (
            <div className="space-y-4">
              <h3 className="font-semibold text-gray-900">Résultats de recherche</h3>
              <div className="space-y-3">
                {searchResults.map((article) => (
                  <div 
                    key={article.id}
                    className="flex gap-3 p-3 hover:bg-gray-50 rounded cursor-pointer group transition-colors"
                  >
                    {article.image && (
                      <img 
                        src={article.image} 
                        alt="" 
                        className="w-20 h-20 object-cover rounded flex-shrink-0"
                        onError={(e) => {
                          e.target.style.display = 'none';
                        }}
                      />
                    )}
                    <div className="flex-1 min-w-0">
                      <h4 className="font-semibold text-sm text-gray-900 group-hover:text-[#009EE2] transition-colors line-clamp-2">
                        {article.title}
                      </h4>
                      {article.excerpt && (
                        <p className="text-xs text-gray-600 mt-1 line-clamp-2">{article.excerpt}</p>
                      )}
                      <div className="flex items-center gap-2 mt-2 text-xs text-gray-500">
                        {article.source && <span>{article.source}</span>}
                        {article.timestamp && <span>• {article.timestamp}</span>}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ) : searchQuery.length > 2 ? (
            <div className="text-center text-gray-500 py-8">
              <p>Aucun résultat trouvé pour "{searchQuery}"</p>
            </div>
          ) : (
            <div className="space-y-4">
              <h3 className="font-semibold text-gray-900">Recherches populaires</h3>
              <div className="flex flex-wrap gap-2">
                {['Bitcoin', 'Wall Street', 'Fed', 'BCE', 'Pétrole', 'Or', 'Trading', 'Inflation', 'Bourse'].map((term) => (
                  <Button
                    key={term}
                    variant="outline"
                    size="sm"
                    onClick={() => handlePopularSearch(term)}
                    className="rounded-full"
                  >
                    {term}
                  </Button>
                ))}
              </div>
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default SearchModal;