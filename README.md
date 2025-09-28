# 🚀 NASA ETL – Fireballs & CAD

Ce projet est un **ETL (Extract, Transform, Load)** pour récupérer, transformer et visualiser les données publiques de la NASA sur :  
- **Fireballs** (bolides dans l’atmosphère terrestre)  
- **Close-Approach Data (CAD)** des astéroïdes  

Il combine un **backend FastAPI** pour le traitement et un **frontend Vue.js** pour la visualisation des données.

---

## 📂 Structure du projet

NASA_API_ETL_Celestial_bodies_-_Fireballs/
├── README.md                # Documentation principale
├── requirements.txt          # Dépendances Python (Backend)
│
├── main/
│   └── main.py               # Point d'entrée FastAPI
│
├── app/                      # Backend (API & ETL)
│   ├── api/                  # Routes/API FastAPI
│   │   ├── fireballs.py
│   │   └── cad.py
│   ├── controller/           # Logique métier
│   ├── etl/                  # Scripts d'extraction/chargement des données NASA
│   ├── model/                # Modèles de données (ORM)
│   ├── schemas/              # Schémas Pydantic (validation)
│   ├── service/              # Services externes (API, DB)
│   └── utils/                # Configurations & outils (logger, etc.)
│
├── frontend/                 # Interface utilisateur (Vue.js)
│   ├── index.html
│   ├── package.json          # Dépendances du frontend
│   ├── vite.config.js
│   ├── public/               # Assets statiques
│   └── src/                  # Code Vue.js
│       ├── App.vue           # Composant racine
│       ├── main.js           # Point d'entrée
│       ├── components/       # Composants UI (Dashboard, Graphiques…)
│       ├── pages/            # Pages principales (Home, Fireballs, CAD)
│       ├── router/           # Routing Vue
│       └── store/            # State management
│
└── scripts/                  # Outils / scripts ponctuels
    ├── seed_database.py
    └── clean_data.py

---

## ⚡ Lancement du projet

### Backend (FastAPI)
1. Se placer dans le dossier backend :  
```bash
cd backend
```

2. Lancer l'API :
```bash
uvicorn main.main:app --reload
```

3. L’API sera disponible sur : http://127.0.0.1:8000

---

### Frontend (Vue.js)

1. Activer Node.js v20 :
```bash
nvm use 20
```

2. Installer les dépendances si ce n’est pas déjà fait :
```bash
npm install
```

3. Lancer le frontend :
```bash
npm run dev
```

4. L’interface sera accessible sur : http://localhost:5173 (port par défaut Vite)

---

## 📊 Sources de données
### Fireballs

API officielle : NASA Fireball API

Fournit des informations sur les bolides détectés dans l’atmosphère terrestre (énergie, vitesse, altitude, localisation…).

### Close-Approach Data (CAD)

API officielle : NASA CAD API

Contient les données sur les astéroïdes et comètes proches de la Terre (distance, diamètre estimé, vitesse…).

## 🛠 Technologies utilisées

### Backend : Python, FastAPI, Pandas, Requests

### Frontend : Vue.js, TailwindCSS, Vite

### Versioning Node : NVM pour gérer la version 20

### ETL & Data : API NASA, transformation et stockage local

## 💡 Fonctionnalités

1. Extraction automatisée des données NASA Fireballs & CAD
2. Transformation et nettoyage des données
3. API pour accéder aux données traitées
4. Visualisation interactive via frontend (cartes, graphiques, tableaux)

## 📚 Références

Documentation Fireball API
Documentation CAD API
FastAPI
Vue.js
