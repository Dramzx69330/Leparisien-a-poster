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
      
      // Charger le contenu complet si l'article a une URL ET:
      // - soit le contenu est court (< 500 chars)
      // - soit le contenu est tronqué (contient "[+X chars]")
      const isTruncated = parsedArticle.content && /\[\+\d+\s*chars?\]/.test(parsedArticle.content);
      const isShort = parsedArticle.content && parsedArticle.content.length < 500;
      
      if (parsedArticle.url && (isShort || isTruncated)) {
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

      <main className="max-w-4xl mx-auto px-3 sm:px-4 py-4 sm:py-8">
        {/* Bouton retour */}
        <button
          onClick={() => navigate(-1)}
          className="flex items-center gap-2 text-gray-600 hover:text-[#009EE2] transition-colors mb-4 sm:mb-6 p-2"
        >
          <ArrowLeft size={20} />
          <span className="font-medium text-sm sm:text-base">Retour</span>
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

          <div className="p-4 sm:p-6 md:p-8">
            {/* Métadonnées */}
            <div className="flex flex-wrap items-center gap-2 sm:gap-4 text-xs sm:text-sm mb-4 sm:mb-6 pb-3 sm:pb-4 border-b border-gray-100">
              {article.source && (
                <span className="inline-flex items-center px-2 sm:px-3 py-1 bg-[#009EE2] text-white font-semibold rounded-full text-xs">
                  {article.source}
                </span>
              )}
              {article.publishedAt && (
                <div className="flex items-center gap-1 sm:gap-1.5 text-gray-600">
                  <Calendar size={14} className="sm:w-4 sm:h-4" />
                  <span className="text-xs sm:text-sm">{formatDate(article.publishedAt)}</span>
                </div>
              )}
              {article.readTime && (
                <div className="flex items-center gap-1 sm:gap-1.5 text-gray-600">
                  <Clock size={14} className="sm:w-4 sm:h-4" />
                  <span className="text-xs sm:text-sm">{article.readTime} de lecture</span>
                </div>
              )}
            </div>

            {/* Titre */}
            <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-gray-900 mb-4 sm:mb-6 leading-tight">
              {article.title}
            </h1>

            {/* Extrait avec style */}
            {article.excerpt && (
              <div className="bg-gray-50 border-l-4 border-[#009EE2] p-4 sm:p-6 rounded-r-lg mb-6 sm:mb-8">
                <p className="text-base sm:text-xl text-gray-700 leading-relaxed italic">
                  {article.excerpt}
                </p>
              </div>
            )}

            {/* Contenu */}
            {loadingFullContent ? (
              <div className="flex items-center justify-center py-8 sm:py-12">
                <div className="text-center">
                  <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-[#009EE2] mb-3"></div>
                  <p className="text-gray-600 text-sm sm:text-base">Chargement du contenu complet...</p>
                </div>
              </div>
            ) : article.content ? (
              <div className="prose prose-sm sm:prose-lg max-w-none mb-6 sm:mb-8 article-content">
                <style>{`
                  .article-content .intro {
                    font-size: 1rem;
                    line-height: 1.8;
                    color: #374151;
                    margin-bottom: 1.5rem;
                  }
                  @media (min-width: 640px) {
                    .article-content .intro {
                      font-size: 1.125rem;
                    }
                  }
                  .article-content .author {
                    font-size: 0.875rem;
                    color: #6b7280;
                    margin-bottom: 1.5rem;
                    padding-bottom: 1rem;
                    border-bottom: 1px solid #e5e7eb;
                  }
                  @media (min-width: 640px) {
                    .article-content .author {
                      font-size: 0.95rem;
                      margin-bottom: 2rem;
                    }
                  }
                  .article-content .question {
                    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
                    border-left: 4px solid #009EE2;
                    padding: 0.75rem 1rem;
                    margin: 1.5rem 0 0.75rem 0;
                    border-radius: 0 8px 8px 0;
                    font-size: 0.95rem;
                    font-weight: 600;
                    color: #0369a1;
                  }
                  @media (min-width: 640px) {
                    .article-content .question {
                      padding: 1rem 1.5rem;
                      margin: 2rem 0 1rem 0;
                      font-size: 1.05rem;
                    }
                  }
                  .article-content .question .journalist {
                    color: #009EE2;
                    font-weight: 700;
                    margin-right: 0.5rem;
                  }
                  .article-content .answer {
                    font-size: 0.95rem;
                    line-height: 1.7;
                    color: #1f2937;
                    margin-bottom: 0.75rem;
                  }
                  @media (min-width: 640px) {
                    .article-content .answer {
                      font-size: 1.05rem;
                      line-height: 1.8;
                    }
                  }
                  .article-content .answer strong {
                    color: #111827;
                    font-weight: 600;
                  }
                  .article-content .answer em {
                    color: #6b7280;
                    font-style: italic;
                  }
                  .article-content .conclusion {
                    color: #6b7280;
                    font-size: 0.95rem;
                    margin-top: 2rem;
                    font-style: italic;
                  }
                  .article-content .about {
                    background: #f3f4f6;
                    padding: 1.5rem;
                    margin-top: 2rem;
                    border-radius: 8px;
                    font-size: 0.95rem;
                    color: #4b5563;
                    line-height: 1.6;
                  }
                  .article-content .about strong {
                    color: #111827;
                    display: block;
                    margin-bottom: 0.5rem;
                  }
                `}</style>
                <div dangerouslySetInnerHTML={{ __html: article.content }} />
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