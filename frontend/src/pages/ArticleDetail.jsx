import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, Clock, Calendar, ExternalLink, Share2 } from 'lucide-react';
import { Button } from '../components/ui/button';
import Header from '../components/Header';
import Navigation from '../components/Navigation';

const ArticleDetail = () => {
  const { articleId } = useParams();
  const navigate = useNavigate();
  const [article, setArticle] = useState(null);
  const [copySuccess, setCopySuccess] = useState(false);
  const [loadingFullContent, setLoadingFullContent] = useState(false);
  const [similarArticles, setSimilarArticles] = useState([]);
  const [loadingSimilar, setLoadingSimilar] = useState(true);

  useEffect(() => {
    // Récupérer l'article depuis le sessionStorage
    const storedArticle = sessionStorage.getItem(`article_${articleId}`);
    if (storedArticle) {
      const parsedArticle = JSON.parse(storedArticle);
      setArticle(parsedArticle);
      
      // Charger le contenu complet si l'article a une URL
      if (parsedArticle.url && parsedArticle.content && parsedArticle.content.length < 500) {
        loadFullContent(parsedArticle.url);
      }

      // Charger les articles similaires
      loadSimilarArticles(parsedArticle.category);
    }
  }, [articleId]);

  const handleCategoryClick = (category) => {
    // Navigate to homepage with selected category
    navigate('/', { state: { category } });
  };

  const handleLogoClick = () => {
    navigate('/');
  };

  const loadSimilarArticles = async (category) => {
    try {
      setLoadingSimilar(true);
      const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
      const response = await fetch(
        `${BACKEND_URL}/api/news/top-headlines?pageSize=4`
      );
      
      if (response.ok) {
        const data = await response.json();
        if (data.articles) {
          // Filtrer l'article actuel et prendre 3 articles
          const filtered = data.articles
            .filter(a => a.id.toString() !== articleId)
            .slice(0, 3);
          setSimilarArticles(filtered);
        }
      }
    } catch (error) {
      console.error('Error loading similar articles:', error);
    } finally {
      setLoadingSimilar(false);
    }
  };

  const loadFullContent = async (url) => {
    try {
      setLoadingFullContent(true);
      const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
      const response = await fetch(
        `${BACKEND_URL}/api/news/scrape-article?article_url=${encodeURIComponent(url)}`,
        { method: 'POST' }
      );
      
      if (response.ok) {
        const data = await response.json();
        if (data.content) {
          setArticle(prev => ({
            ...prev,
            content: data.content,
            fullContentLoaded: true
          }));
        }
      }
    } catch (error) {
      console.error('Error loading full content:', error);
    } finally {
      setLoadingFullContent(false);
    }
  };

  const handleCopyLink = () => {
    const url = window.location.href;
    
    // Créer un élément textarea temporaire
    const textarea = document.createElement('textarea');
    textarea.value = url;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    
    try {
      // Sélectionner et copier le texte
      textarea.select();
      textarea.setSelectionRange(0, 99999); // Pour mobile
      document.execCommand('copy');
      
      // Afficher le message de succès
      setCopySuccess(true);
      setTimeout(() => setCopySuccess(false), 3000);
    } catch (err) {
      console.error('Erreur lors de la copie:', err);
      alert(`Lien de l'article : ${url}`);
    } finally {
      // Nettoyer
      document.body.removeChild(textarea);
    }
  };

  if (!article) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Header 
          onMenuClick={() => {}}
          onSearchClick={() => {}}
          onLogoClick={() => navigate('/')}
        />
        <Navigation activeCategory="" onCategoryChange={() => {}} />
        <div className="max-w-4xl mx-auto px-4 py-20 text-center">
          <p className="text-gray-600">Article non trouvé</p>
          <Button onClick={() => navigate('/')} className="mt-4">
            Retour à l'accueil
          </Button>
        </div>
      </div>
    );
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', { 
      day: 'numeric', 
      month: 'long', 
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header 
        onMenuClick={() => {}}
        onSearchClick={() => {}}
        onLogoClick={handleLogoClick}
      />
      <Navigation activeCategory="" onCategoryChange={handleCategoryClick} />

      <main className="max-w-4xl mx-auto px-4 py-8">
        {/* Bouton retour */}
        <button
          onClick={() => navigate(-1)}
          className="flex items-center gap-2 text-gray-600 hover:text-[#009EE2] transition-colors mb-6"
        >
          <ArrowLeft size={20} />
          <span className="font-medium">Retour</span>
        </button>

        {/* Article */}
        <article className="bg-white rounded-lg shadow-sm overflow-hidden">
          {/* Image principale */}
          {article.image && (
            <div className="w-full aspect-[16/9] overflow-hidden bg-gray-200">
              <img
                src={article.image}
                alt={article.title}
                className="w-full h-full object-cover"
                onError={(e) => {
                  e.target.style.display = 'none';
                }}
              />
            </div>
          )}

          <div className="p-8">
            {/* Métadonnées */}
            <div className="flex items-center gap-4 text-sm mb-6 pb-4 border-b border-gray-100">
              {article.source && (
                <span className="inline-flex items-center px-3 py-1 bg-[#009EE2] text-white font-semibold rounded-full">
                  {article.source}
                </span>
              )}
              {article.publishedAt && (
                <div className="flex items-center gap-1.5 text-gray-600">
                  <Calendar size={16} />
                  <span>{formatDate(article.publishedAt)}</span>
                </div>
              )}
              {article.readTime && (
                <div className="flex items-center gap-1.5 text-gray-600">
                  <Clock size={16} />
                  <span>{article.readTime} de lecture</span>
                </div>
              )}
            </div>

            {/* Titre */}
            <h1 className="text-4xl font-bold text-gray-900 mb-6 leading-tight">
              {article.title}
            </h1>

            {/* Extrait avec style */}
            {article.excerpt && (
              <div className="bg-gray-50 border-l-4 border-[#009EE2] p-6 rounded-r-lg mb-8">
                <p className="text-xl text-gray-700 leading-relaxed italic">
                  {article.excerpt}
                </p>
              </div>
            )}

            {/* Contenu */}
            {loadingFullContent ? (
              <div className="flex items-center justify-center py-12">
                <div className="text-center">
                  <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-[#009EE2] mb-3"></div>
                  <p className="text-gray-600">Chargement du contenu complet...</p>
                </div>
              </div>
            ) : article.content ? (
              <div className="prose prose-lg max-w-none mb-8">
                {/* Split content into paragraphs and format nicely */}
                {article.content.split('\n\n').map((paragraph, index) => {
                  // Skip empty paragraphs
                  if (!paragraph.trim()) return null;
                  
                  // Check if it's a heading (starts with capital letters and is short)
                  const isHeading = paragraph.length < 100 && /^[A-ZÀ-Ü]/.test(paragraph);
                  
                  return isHeading ? (
                    <h3 key={index} className="text-2xl font-bold text-gray-900 mt-8 mb-4 border-l-4 border-[#009EE2] pl-4">
                      {paragraph}
                    </h3>
                  ) : (
                    <p key={index} className="text-gray-700 leading-relaxed mb-6 text-justify">
                      {paragraph}
                    </p>
                  );
                })}
              </div>
            ) : null}

            {/* Note sur l'extrait */}
            {article.fullContentLoaded && (
              <div className="bg-gradient-to-r from-green-50 to-emerald-50 border-l-4 border-green-500 p-5 mb-8 rounded-r-lg shadow-sm">
                <div className="flex items-start gap-3">
                  <svg className="w-6 h-6 text-green-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <div>
                    <p className="text-sm font-semibold text-green-800">
                      Contenu complet chargé
                    </p>
                    <p className="text-xs text-green-700 mt-1">
                      Article intégral provenant de {article.source}
                    </p>
                  </div>
                </div>
              </div>
            )}

            {/* Actions */}
            <div className="flex items-center justify-between pt-6 border-t-2 border-gray-100 mt-8">
              <button
                onClick={handleCopyLink}
                className={`flex items-center gap-2 px-5 py-2.5 rounded-lg font-medium transition-all shadow-sm ${
                  copySuccess 
                    ? 'bg-green-500 text-white hover:bg-green-600' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                {copySuccess ? (
                  <>
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span>Lien copié !</span>
                  </>
                ) : (
                  <>
                    <Share2 size={18} />
                    <span>Partager l'article</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </article>

        {/* Section articles similaires */}
        <div className="mt-12">
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Articles similaires</h2>
          {loadingSimilar ? (
            <div className="bg-white rounded-lg p-6 text-center text-gray-500">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-[#009EE2] mb-3"></div>
              <p>Chargement des articles similaires...</p>
            </div>
          ) : similarArticles.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {similarArticles.map((similarArticle) => (
                <div
                  key={similarArticle.id}
                  onClick={() => {
                    // Sauvegarder l'article et naviguer
                    sessionStorage.setItem(`article_${similarArticle.id}`, JSON.stringify(similarArticle));
                    navigate(`/article/${similarArticle.id}`);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }}
                  className="bg-white rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow cursor-pointer group"
                >
                  {similarArticle.image && (
                    <div className="aspect-[16/10] overflow-hidden">
                      <img
                        src={similarArticle.image}
                        alt={similarArticle.title}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                        onError={(e) => {
                          e.target.style.display = 'none';
                        }}
                      />
                    </div>
                  )}
                  <div className="p-4">
                    {similarArticle.source && (
                      <span className="text-xs font-semibold text-[#009EE2]">
                        {similarArticle.source}
                      </span>
                    )}
                    <h3 className="font-bold text-gray-900 mt-2 line-clamp-3 group-hover:text-[#009EE2] transition-colors">
                      {similarArticle.title}
                    </h3>
                    {similarArticle.timestamp && (
                      <p className="text-xs text-gray-500 mt-2">{similarArticle.timestamp}</p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="bg-white rounded-lg p-6 text-center text-gray-500">
              <p>Aucun article similaire disponible</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default ArticleDetail;