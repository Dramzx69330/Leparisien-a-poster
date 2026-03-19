import React from 'react';
import { X } from 'lucide-react';
import { Button } from './ui/button';

const SubscriptionBanner = ({ onClose }) => {
  return (
    <div className="fixed bottom-0 left-0 right-0 bg-gradient-to-r from-blue-50 to-blue-100 border-t-2 border-blue-200 shadow-lg z-40 animate-in slide-in-from-bottom duration-300">
      <div className="max-w-[1400px] mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-8 h-8 bg-red-500 rounded-full flex items-center justify-center text-white font-bold text-sm">
              ⓘ
            </div>
            <p className="text-gray-900 font-medium">
              <span className="font-bold">Municipales 2026 :</span> 3,99€/mois pour voter bien informé
            </p>
          </div>
          <div className="flex items-center gap-3">
            <Button className="bg-[#FFC300] hover:bg-[#E6B000] text-gray-900 font-semibold px-8">
              S'abonner
            </Button>
            <button
              onClick={onClose}
              className="p-2 hover:bg-gray-200 rounded transition-colors"
            >
              <X size={20} className="text-gray-600" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SubscriptionBanner;