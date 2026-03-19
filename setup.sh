#!/bin/bash

echo "🚀 Démarrage du Clone Le Parisien"
echo ""

# Vérifier si dans le bon dossier
if [ ! -f "README.md" ]; then
    echo "❌ Erreur: Lancez ce script depuis le dossier /app"
    exit 1
fi

echo "📦 Installation des dépendances..."
echo ""

# Backend
echo "🐍 Backend (Python)..."
cd backend
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -q -r requirements.txt
cd ..
echo "✅ Backend installé"

# Frontend
echo "⚛️  Frontend (React)..."
cd frontend
yarn install --silent
cd ..
echo "✅ Frontend installé"

echo ""
echo "✅ Installation terminée!"
echo ""
echo "🎯 Pour démarrer:"
echo ""
echo "Backend:  cd backend && source venv/bin/activate && uvicorn server:app --host 0.0.0.0 --port 8001"
echo "Frontend: cd frontend && yarn start"
echo ""
echo "📊 136 articles prêts à l'emploi!"
echo "🔒 Article protégé: Portrait d'un jeune entrepreneur"
echo ""
