import React, { useState } from 'react';
import { Menu as MenuIcon, X, ChevronRight } from 'lucide-react';
import { Sheet, SheetContent, SheetHeader, SheetTitle } from './ui/sheet';
import { categories } from '../mockData';

const MobileMenu = ({ isOpen, onClose }) => {
  return (
    <Sheet open={isOpen} onOpenChange={onClose}>
      <SheetContent side="left" className="w-80 p-0">
        <SheetHeader className="border-b px-6 py-4">
          <SheetTitle className="text-left">Menu</SheetTitle>
        </SheetHeader>
        <div className="overflow-y-auto h-full pb-20">
          <nav className="py-4">
            {categories.map((category, index) => (
              <button
                key={index}
                className="w-full flex items-center justify-between px-6 py-3 text-left hover:bg-gray-50 transition-colors group"
              >
                <span className="text-gray-900 font-medium group-hover:text-[#009EE2] transition-colors">
                  {category.name}
                </span>
                {category.hasDropdown && (
                  <ChevronRight size={18} className="text-gray-400 group-hover:text-[#009EE2] transition-colors" />
                )}
              </button>
            ))}
          </nav>
          <div className="border-t mt-4 pt-4 px-6 space-y-3">
            <button className="w-full py-2 text-left text-gray-700 hover:text-[#009EE2] font-medium transition-colors">
              Se connecter
            </button>
            <button className="w-full py-3 bg-[#FFC300] hover:bg-[#E6B000] text-gray-900 font-semibold rounded transition-colors">
              S'abonner
            </button>
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
};

export default MobileMenu;