export const mockArticles = [
  {
    id: 1,
    title: "Municipales 2026 : qui sont les candidats au second tour dans votre commune ?",
    category: "Municipales 2026",
    categoryColor: "blue",
    image: "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=800&h=600&fit=crop",
    excerpt: "Le Parisien a rassemblé dans un simulateur l'ensemble des prétendants en lice pour décrocher le siège de maire ce dimanche 22 mars.",
    readTime: "5 min",
    timestamp: "Il y a 2h",
    featured: true,
    tag: "En ce moment"
  },
  {
    id: 2,
    title: "Municipales 2026 : alliances, bascules, surprises... Les 80 villes à suivre au second tour",
    category: "Politique",
    categoryColor: "default",
    image: "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=600&h=400&fit=crop",
    excerpt: "Découvrez les enjeux majeurs de ce second tour des élections municipales.",
    readTime: "8 min",
    timestamp: "Il y a 3h",
    featured: false
  },
  {
    id: 3,
    title: "Municipales : retrait, fusion, maintien... Au second tour, Paris aura une triangulaire sous haute tension",
    category: "Paris",
    categoryColor: "cyan",
    categoryTag: "Récit",
    image: "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&h=400&fit=crop",
    excerpt: "Les tractations vont bon train dans la capitale pour le second tour.",
    readTime: "6 min",
    timestamp: "Il y a 4h",
    featured: false
  },
  {
    id: 4,
    title: "DIRECT. Municipales à Paris : Marine Le Pen appelle à «faire barrage» contre Emmanuel Grégoire",
    category: "Politique",
    categoryColor: "red",
    categoryTag: "Live",
    image: "https://images.unsplash.com/photo-1577415124269-fc1140ec2d9d?w=600&h=400&fit=crop",
    excerpt: "Suivez en direct les derniers développements de la campagne parisienne.",
    readTime: "Direct",
    timestamp: "En cours",
    featured: false,
    isLive: true
  },
  {
    id: 5,
    title: "Après le débat d'entre-deux tours à Paris, des proches de Rachida Dati encensent... Sophia Chikirou",
    category: "Politique",
    categoryColor: "default",
    image: "https://images.unsplash.com/photo-1591035897819-f4bdf739f446?w=600&h=400&fit=crop",
    excerpt: "Un moment inattendu lors du débat télévisé hier soir.",
    readTime: "4 min",
    timestamp: "Il y a 5h",
    featured: false
  },
  {
    id: 6,
    title: "Hausse des prix du gaz et des carburants : « Toute aide publique aura un coût très élevé pour les finances du pays »",
    category: "Économie",
    categoryColor: "default",
    categoryTag: "Interview",
    image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&h=400&fit=crop",
    excerpt: "Un économiste analyse les conséquences de la hausse des prix de l'énergie.",
    readTime: "8 min",
    timestamp: "Il y a 6h",
    featured: false
  },
  {
    id: 7,
    title: "« Projet dernière chance » : on (re) tombe amoureux de Ryan Gosling",
    category: "Culture",
    categoryColor: "purple",
    categoryTag: "Critique",
    image: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=600&h=400&fit=crop",
    excerpt: "Le nouvel film avec Ryan Gosling arrive en salles cette semaine.",
    readTime: "7 min",
    timestamp: "Il y a 7h",
    featured: false
  },
  {
    id: 8,
    title: "Municipales 2026 : 3 insultes, Arabe de service, diffamations »... guerre ouverte entre le PS et LFI dans une commune de l'Hérault",
    category: "Politique",
    categoryColor: "default",
    image: "https://images.unsplash.com/photo-1495573258723-2c7be7a646ce?w=600&h=400&fit=crop",
    excerpt: "Les tensions montent entre les différents partis de gauche.",
    readTime: "12 min",
    timestamp: "Il y a 8h",
    featured: false
  }
];

export const sidebarArticles = [
  {
    id: 101,
    title: "Hausse des prix du gaz et des carburants : « Toute aide publique aura un coût très élevé pour les finances du pays »",
    category: "Interview",
    categoryColor: "orange",
    readTime: "8 min",
    timestamp: "Il y a 6h"
  },
  {
    id: 102,
    title: "Municipales 2026 : 3 insultes, Arabe de service, diffamations »... guerre ouverte entre le PS et LFI dans une commune de l'Hérault",
    category: "Politique",
    categoryColor: "default",
    readTime: "12 min",
    timestamp: "Il y a 8h"
  },
  {
    id: 103,
    title: "À Vernon, on n'a pas oublié le manoir du collabo « Luchaire tué par les nazis » à Giverny",
    category: "Histoire",
    categoryColor: "default",
    readTime: "10 min",
    timestamp: "Il y a 9h"
  },
  {
    id: 104,
    title: "« Projet dernière chance » : on (re) tombe amoureux de Ryan Gosling",
    category: "Critique",
    categoryColor: "purple",
    readTime: "7 min",
    timestamp: "Il y a 7h"
  }
];

export const categories = [
  { name: "À la une", path: "/" },
  { name: "En continu", path: "/en-continu" },
  { name: "Paris & Île-de-France", path: "/paris", hasDropdown: true },
  { name: "Faits divers", path: "/faits-divers" },
  { name: "Municipales 2026", path: "/municipales-2026", hasIcon: true },
  { name: "International", path: "/international" },
  { name: "Économie", path: "/economie" },
  { name: "Société", path: "/societe" },
  { name: "Sports", path: "/sports" },
  { name: "Culture", path: "/culture" },
  { name: "Étudiant", path: "/etudiant" },
  { name: "Vidéos", path: "/videos" },
  { name: "Guide d'achat", path: "/guide-achat" },
  { name: "Jardin", path: "/jardin" }
];