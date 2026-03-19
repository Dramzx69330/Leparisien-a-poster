import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Clock, Circle } from 'lucide-react';

const ArticleCard = ({ article, size = 'default' }) => {
  const navigate = useNavigate();

  const getCategoryStyle = (color, tag) => {
    const styles = {
      red: 'bg-red-600 text-white',
      blue: 'bg-blue-600 text-white',
      cyan: 'bg-cyan-500 text-white',
      purple: 'bg-purple-600 text-white',
      orange: 'bg-orange-500 text-white',
      default: 'bg-gray-100 text-gray-800'
    };
    return styles[color] || styles.default;
  };

  const sizeClasses = {
    large: 'col-span-2 row-span-2',
    medium: 'col-span-1 row-span-1',
    default: 'col-span-1'
  };

  // Handle missing images
  const imageUrl = article.image || 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800&h=600&fit=crop';

  const handleClick = () => {
    // Stocker l'article dans sessionStorage pour la page de détails
    sessionStorage.setItem(`article_${article.id}`, JSON.stringify(article));
    // Naviguer vers la page de détails
    navigate(`/article/${article.id}`);
  };

  return (
    <article 
      className={`group cursor-pointer ${sizeClasses[size]}`}
      onClick={handleClick}
    >
      <div className="relative overflow-hidden rounded-sm">
        {/* Image */}
        <div className="relative aspect-[16/10] overflow-hidden bg-gray-200">
          <img
            src={imageUrl}
            alt={article.title}
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
            onError={(e) => {
              e.target.src = 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800&h=600&fit=crop';
            }}
          />
          {article.isLive && (
            <div className="absolute top-3 left-3 flex items-center gap-2 bg-red-600 text-white px-3 py-1 rounded text-xs font-bold">
              <Circle size={8} className="fill-white animate-pulse" />
              <span>DIRECT</span>
            </div>
          )}
          {article.categoryTag && (
            <div className={`absolute top-3 left-3 px-3 py-1 rounded text-xs font-bold ${getCategoryStyle(article.categoryColor, article.categoryTag)}`}>
              {article.categoryTag}
            </div>
          )}
        </div>

        {/* Content */}
        <div className="mt-3">
          {article.tag && (
            <div className="flex items-center gap-2 mb-2">
              <span className="text-xs font-semibold text-gray-500 uppercase tracking-wide">
                {article.tag}
              </span>
            </div>
          )}
          <h3 className={`font-bold text-gray-900 group-hover:text-[#009EE2] transition-colors line-clamp-3 ${
            size === 'large' ? 'text-xl sm:text-2xl leading-tight' : 'text-base sm:text-lg leading-snug'
          }`}>
            {article.title}
          </h3>
          {article.excerpt && size === 'large' && (
            <p className="mt-2 text-gray-600 text-sm sm:text-base line-clamp-2">
              {article.excerpt}
            </p>
          )}
          <div className="flex items-center gap-3 mt-3 text-xs text-gray-500">
            {article.source && (
              <span className="font-medium">{article.source}</span>
            )}
            {article.readTime && (
              <div className="flex items-center gap-1">
                <Clock size={14} />
                <span>{article.readTime}</span>
              </div>
            )}
            {article.timestamp && <span>{article.timestamp}</span>}
          </div>
        </div>
      </div>
    </article>
  );
};

export default ArticleCard;
