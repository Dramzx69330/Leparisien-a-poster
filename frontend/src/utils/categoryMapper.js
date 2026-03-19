// Map categories to economic news queries by region
export const categoryMapper = {
  'À la une': 'economy OR finance OR business OR markets',
  'Europe': 'economy Europe OR finance Europe OR business Europe OR ECB OR euro',
  'Amérique': 'economy USA OR finance America OR business Americas OR Fed OR dollar OR Wall Street',
  'Asie': 'economy Asia OR finance Asia OR business China Japan India OR yen yuan',
  'Afrique': 'economy Africa OR finance Africa OR business Africa OR African development',
  'Moyen-Orient': 'economy Middle East OR finance Gulf OR oil OPEC OR Dubai',
  'Marchés': 'stock market OR trading OR shares OR equity OR commodities',
  'Crypto': 'cryptocurrency OR bitcoin OR blockchain OR ethereum OR crypto',
  'Tech & Innovation': 'technology business OR innovation economy OR startup OR fintech',
  'Commerce International': 'international trade OR export import OR tariffs OR WTO'
};

export const getCategoryForAPI = (categoryName) => {
  return categoryMapper[categoryName] || categoryMapper['À la une'];
};
