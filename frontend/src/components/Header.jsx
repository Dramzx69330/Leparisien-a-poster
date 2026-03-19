import React, { useState } from 'react';
import { Menu, Newspaper, User, Search } from 'lucide-react';
import { Button } from './ui/button';

const Header = ({ onMenuClick, onSearchClick }) => {
  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-[1400px] mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Left section */}
          <div className="flex items-center gap-6">
            <button
              onClick={onMenuClick}
              className="flex items-center gap-2 text-gray-700 hover:text-gray-900 transition-colors"
            >
              <Menu size={20} />
              <span className="text-sm font-medium">Menu</span>
            </button>
          </div>

          {/* Center - Logo */}
          <div className="absolute left-1/2 transform -translate-x-1/2">
            <div className="bg-[#009EE2] px-8 py-2 rounded">
              <h1 className="text-white text-2xl font-bold tracking-wide">le Parisien</h1>
            </div>
          </div>

          {/* Right section */}
          <div className="flex items-center gap-3">
            <Button
              variant="ghost"
              size="sm"
              className="text-gray-700 hover:text-gray-900"
              onClick={onSearchClick}
            >
              <Search size={18} className="mr-1" />
              Rechercher
            </Button>
            <Button
              variant="outline"
              size="sm"
              className="flex items-center gap-2 border-gray-300"
            >
              <Newspaper size={18} />
              <span>Journal</span>
            </Button>
            <Button
              variant="outline"
              size="sm"
              className="flex items-center gap-2 border-gray-300"
            >
              <User size={18} />
              <span>Se connecter</span>
            </Button>
            <Button
              size="sm"
              className="bg-[#FFC300] hover:bg-[#E6B000] text-gray-900 font-semibold px-6"
            >
              S'abonner
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;