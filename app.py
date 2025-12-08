# app.py 
import os 
import getpass # Pour cacher la clé API en console 
from core_ai import GeminiClient 
import user_manager as um 

# --- Constantes et Initialisation --- 
THEMES = ["Fonctions", "Listes", "Dictionnaires", "POO", "Fichiers et Exceptions"] 
NIVEAUX = ["Débutant", "Intermédiaire", "Avancé"]

# Variables d'état globales (mieux gérées par la POO, mais simple pour la CLI)
utilisateur_courant = None 
gemini_client = None
model='gemini-2.5-flash'
api-key=input('Entrez votre clé API Gemini :') #sera demandé au moment du lancement du module

def afficher_menu(): 
    """Affiche le menu principal de l'application.""" 
    if utilisateur_courant: #si un utilisateur courant a été renseigné, par défaut None
        data = um.charger_utilisateurs() #appel de la fonction charger_utilisateur du module user_manager pour afficher ses infos
        score = data[utilisateur_courant]['score'] 
        print(f"\n--- Menu principal (Utilisateur : {utilisateur_courant.capitalize()} | Score: {score}) ---") 
    else: 
        print("\n--- Menu principal ---") #par défaut, on affiche pas d'infos

    print("1. Choisir/Créer un profil") 
    print("2. Générer un nouvel exercice") 
    print("3. Quitter") 
    return input("Entrez votre choix (1-3) : ")

def choisir_utilisateur(): 
    """Permet de choisir ou créer un profil utilisateur."""
    #J'ai besoin du nom, je demande au user
    utilisateur_courant=input("Entrée votre nom utilisateur").strip()

    # Vérification basique : éviter les entrées vides
    if not utilisateur_courant:
        print("Le nom d'utilisateur ne peut pas être vide.")
        return None

     #j'appelle la fonction creer_ou_charger_utilisateur du module user_manager
    return um.creer_ou_charger_utilisateur(utilisateur_courant)


def lancer_exercice(): 
    """Gère le processus complet de génération, soumission et évaluation de l'exercice."""
    #j'instancie ma classe GeminiClient du module core_ai sur la variable gemini_client avec en paramètre la clé API
    # j'appelle la fonction generer_exercice du module core_ai: j'ai besoin d'un thème et d'un niveau
    #je récupére une consigne et un résultat, j'affiche seulement la consigne
    #je demande la réponse du user
    #j'envoie cette réponse, la consigne et la réponse attendue à la fonction evaluer_code du module core_ai
    #je récupère le score, le commentaire et la solution attendue et j'affiche
    #j'envoie le nom, score et la consigne à la fonction mettre_a_jour_score(nom, points, details_exo) du module user_manager
    #je sauvegarde grâce à la fonction


def main(): 
    """Fonction principale de l'application."""
    #première fonction: afficher_menu ==> ça va (retourner un chiffre=choix du menu)
    #je dois utiliser ce chiffre pour déterminer quelle fonction utiliser
    #   option 1: appel de la fonction choisir_utilisateur
    #   option 2: appel de la fonction lancer_utilisateur
    #   option 3: sortir de la fonction main



if __name__ == "__main__": 
    main()     # Appel de main = début du pprogramme
