import React, { useState } from 'react';
import { Menu, Newspaper, User, Search } from 'lucide-react';
import { Button } from './ui/button';

const Header = ({ onMenuClick, onSearchClick, onLogoClick }) => {
  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-[1400px] mx-auto px-3 sm:px-4">
        <div className="flex items-center justify-between h-14 sm:h-16">
          {/* Left section */}
          <div className="flex items-center gap-2 sm:gap-6">
            <button
              onClick={onMenuClick}
              className="flex items-center gap-1 sm:gap-2 text-gray-700 hover:text-gray-900 transition-colors p-2"
            >
              <Menu size={20} />
              <span className="text-xs sm:text-sm font-medium hidden sm:inline">Menu</span>
            </button>
          </div>

          {/* Center - Logo */}
          <div className="absolute left-1/2 transform -translate-x-1/2">
            <button 
              onClick={onLogoClick}
              className="block cursor-pointer hover:opacity-80 transition-opacity"
            >
              <img 
                src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Le_Parisien_-_logo_2016.png" 
                alt="Le Parisien" 
                className="h-8 sm:h-10 md:h-12 w-auto"
              />
            </button>
          </div>

          {/* Right section */}
          <div className="flex items-center gap-1 sm:gap-2 md:gap-3">
            {/* Search button - always visible */}
            <Button
              variant="ghost"
              size="sm"
              className="text-gray-700 hover:text-gray-900 p-2"
              onClick={onSearchClick}
            >
              <Search size={18} />
              <span className="ml-1 hidden md:inline text-sm">Rechercher</span>
            </Button>
            
            {/* Desktop only buttons */}
            <Button
              variant="outline"
              size="sm"
              className="hidden md:flex items-center gap-2 border-gray-300"
            >
              <Newspaper size={18} />
              <span>Journal</span>
            </Button>
            <Button
              variant="outline"
              size="sm"
              className="hidden lg:flex items-center gap-2 border-gray-300"
            >
              <User size={18} />
              <span>Se connecter</span>
            </Button>
            
            {/* Subscribe button - responsive */}
            <Button
              size="sm"
              className="bg-[#FFC300] hover:bg-[#E6B000] text-gray-900 font-semibold px-3 sm:px-4 md:px-6 text-xs sm:text-sm"
            >
              <span className="hidden sm:inline">S'abonner</span>
              <span className="sm:hidden">Abo</span>
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;