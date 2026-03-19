// Map Le Parisien categories to NewsAPI categories
export const categoryMapper = {
  'À la une': null, // general headlines
  'En continu': 'recent',
  'International': null,
  'Économie': 'economie',
  'Société': null,
  'Sports': 'sports',
  'Culture': 'culture',
  'Paris & Île-de-France': null,
  'Faits divers': null,
  'Municipales 2026': null,
  'Étudiant': null,
  'Vidéos': null,
  "Guide d'achat": null,
  'Jardin': null
};

export const getCategoryForAPI = (categoryName) => {
  return categoryMapper[categoryName] || null;
};
