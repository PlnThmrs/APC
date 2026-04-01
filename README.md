# APC

## Name
APC: Assitant Pédagogique Collaboratif

## Description
En tant que client, j'ai besoin d'une solution logicielle qui automatise la création, grâce à une IA générative, d'exercices personnalisés et offre un feedback immédiat et qualitatif à mes étudiants. L'outil doit faciliter la montée en compétence des élèves sur les pratiques modernes de développement logiciel.
Le but de ce projet est de concevoir et d'implémenter un Assistant Pédagogique Collaboratif (APC), une application en ligne de commande (CLI) capable de générer des exercices de programmation Python, d'évaluer le code soumis par les élèves et de fournir un retour détaillé, tout cela grâce à l'intelligence de l'API Gemini.
Ce projet synthétise l'ensemble des 10 thèmes abordés dans la série d'exercices, en y ajoutant des outils professionnels essentiels : Git (pour la collaboration et le versionnement) et (Docker pour la portabilité de l'environnement).
Objectifs Pédagogiques Clés :
•	POO (Thème 8) : Structurer l'application autour de classes (GeminiClient, UserManager).
•	Données/Fichiers (Thèmes 4, 5, 7) : Utiliser des dictionnaires pour le stockage et la sérialisation (json) des données utilisateur.
•	Logique/Contrôle (Thèmes 3, 6) : Implémenter des fonctions pour le menu et la logique métier, avec gestion d'exceptions.
•	IA Intégrée : Utiliser l'API Gemini pour des tâches complexes (génération d'énoncés, évaluation de code).
•	Git Avancé : Collaboration, branches de fonctionnalités, rebase ou merge, Pull Requests (PR).
•	Conteneurisation : Dockerfile et utilisation de variables d'environnement.

## Installation
Prérequis : avoir une clé API Gemini
Pour utiliser le projet, lancer l'image Docker

## Utilisation
Objectifs Fonctionnels
1.	Personnalisation Pédagogique : Permettre à l'élève de choisir un thème (Fonctions, POO, etc.) et un niveau (Débutant, Avancé).
2.	Évaluation Objective : Fournir une note chiffrée (sur 10) et un feedback constructif basé sur le code soumis par l'élève.
3.	Suivi des Progrès : Maintenir un historique des scores et des exercices réussis pour chaque utilisateur.

## Support
Contact me on Github @PlnThmrs

## Authors and acknowledgment
Thank you to FD1125 @M2i

## Project status
Premier projet qui utilisait Python et Gitlab, je l'ai migré sur Github pour garder une trace. Il n'y aura pas de développement supplémentaire pour le moment
