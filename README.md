# Industrialisation d'un Pipeline NLP de Classification de Tickets Support (MLOps)

**Auteur :** Karima Chami
**Date :** 14 Février 2026
**Contexte :** Projet de certification RNCP Développeur.se en IA

---

## 📋 Description du Projet

Ce projet vise à automatiser la classification des tickets de support IT reçus par email. L'objectif est de remplacer une catégorisation manuelle coûteuse et hétérogène par un pipeline NLP batch robuste, industrialisé selon les principes **MLOps**.

Le projet couvre l'ensemble du cycle de vie : du traitement des données textuelles à l'entraînement du modèle, en passant par le stockage vectoriel, le monitoring de la dérive des données et l'orchestration sur Kubernetes.

### 🎯 Objectifs
1.  **Automatiser** la classification des tickets.
2.  **Améliorer** le routage et la priorisation des tickets.
3.  **Garantir** la stabilité du modèle face à l'évolution des usages (Monitoring).

---

## 🛠️ Architecture Technique & Pipeline

Le projet est entièrement containerisé.

### 🏗️ Stack Technique
* **NLP & Modélisation :** Python, Hugging Face Transformers, scikit-learn.
* **Base de Données Vectorielle :** ChromaDB.
* **Monitoring ML :** Evidently AI.
* **Infrastructure & Orchestration :** Docker, Kubernetes (Minikube).
* **Monitoring Infra :** Prometheus, Grafana, cAdvisor, Node Exporter.
* **CI/CD :** GitHub Actions.

### 🔄 Étapes du Pipeline (Batch)
1.  **Ingestion & Prétraitement :** Nettoyage des textes (sujet + corps du mail), tokenisation, suppression des stopwords.
2.  **Embedding :** Génération de représentations sémantiques via Hugging Face et stockage dans ChromaDB.
3.  **Classification :** Entraînement et inférence d'un modèle de classification supervisée.
4.  **Monitoring :** Analyse de la dérive des données (Data Drift) et des prédictions via Evidently AI.

---

## 📂 Structure du Répertoire

```text
├── data/                 # Données brutes et traitées
├── models/               # Modèles entraînés (scikit-learn)
├── notebooks/            # Analyse exploratoire (EDA)
├── src/                  # Scripts sources (preprocessing, training, inference)
├── monitoring/           # Configuration Prometheus/Grafana & Rapports Evidently
├── k8s/                  # Manifestes Kubernetes (Jobs, CronJobs)
├── Dockerfile            # Dockerfile du pipeline
├── docker-compose.yml    # Orchestration du monitoring
├── .github/workflows/    # CI/CD GitHub Actions
└── README.md




