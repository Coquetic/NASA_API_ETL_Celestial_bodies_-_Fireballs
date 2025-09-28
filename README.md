# 🚀 NASA ETL – Fireballs & CAD

Ce projet est un **ETL (Extract, Transform, Load)** pour récupérer, transformer et visualiser les données publiques de la NASA sur :  
- **Fireballs** (bolides dans l’atmosphère terrestre)  
- **Close-Approach Data (CAD)** des astéroïdes  

Il combine un **backend FastAPI** pour le traitement et un **frontend Vue.js** pour la visualisation des données.

---

## 📂 Structure du projet

ML/ # Exemples et notebooks (optionnel)
backend/ # API FastAPI
└── main/
└── main.py # point d'entrée
frontend/ # interface Vue.js
└── ... # fichiers Vue et assets

---

## ⚡ Lancement du projet

### Backend (FastAPI)
1. Se placer dans le dossier backend :  
```bash
cd backend
```bash

2.Lancer l'API :
```bash
uvicorn main.main:app --reload
```

3.L’API sera disponible sur : http://127.0.0.1:8000

---

### Frontend (Vue.js)

1.Activer Node.js v20 :
```bash
nvm use 20
```

2.Installer les dépendances si ce n’est pas déjà fait :
```bash
npm install
```

3.Lancer le frontend :
```bash
npm run dev
```

4.L’interface sera accessible sur : http://localhost:5173 (port par défaut Vite)

---

##📊 Sources de données
###Fireballs

API officielle : NASA Fireball API

Fournit des informations sur les bolides détectés dans l’atmosphère terrestre (énergie, vitesse, altitude, localisation…).

###Close-Approach Data (CAD)

API officielle : NASA CAD API

Contient les données sur les astéroïdes et comètes proches de la Terre (distance, diamètre estimé, vitesse…).

##🛠 Technologies utilisées

###Backend : Python, FastAPI, Pandas, Requests

###Frontend : Vue.js, TailwindCSS, Vite

###Versioning Node : NVM pour gérer la version 20

###ETL & Data : API NASA, transformation et stockage local

##💡 Fonctionnalités

1.Extraction automatisée des données NASA Fireballs & CAD
2.Transformation et nettoyage des données
3.API pour accéder aux données traitées
4.Visualisation interactive via frontend (cartes, graphiques, tableaux)

##📚 Références

Documentation Fireball API
Documentation CAD API
FastAPI
Vue.js
