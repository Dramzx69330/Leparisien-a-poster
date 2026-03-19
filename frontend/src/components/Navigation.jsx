import React, { useState } from 'react';
import { ChevronDown, AlertCircle } from 'lucide-react';
import { categories } from '../mockData';

const Navigation = ({ activeCategory, onCategoryChange }) => {
  const [hoveredCategory, setHoveredCategory] = useState(null);

  return (
    <nav className="bg-white border-b border-gray-200 sticky top-16 z-40">
      <div className="max-w-[1400px] mx-auto px-4">
        <div className="flex items-center gap-1 overflow-x-auto scrollbar-hide py-3">
          {categories.map((category, index) => (
            <button
              key={index}
              onClick={() => onCategoryChange(category.name)}
              onMouseEnter={() => setHoveredCategory(category.name)}
              onMouseLeave={() => setHoveredCategory(null)}
              className={`flex items-center gap-1 px-3 py-2 text-sm font-medium whitespace-nowrap rounded transition-all ${
                activeCategory === category.name
                  ? 'text-[#009EE2] bg-blue-50'
                  : 'text-gray-700 hover:text-[#009EE2] hover:bg-gray-50'
              }`}
            >
              {category.hasIcon && (
                <AlertCircle size={16} className="text-red-500" />
              )}
              <span>{category.name}</span>
              {category.hasDropdown && (
                <ChevronDown size={16} className="ml-1" />
              )}
            </button>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Navigation;