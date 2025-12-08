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
#la clé API est appelé dans la fonction main ultérieurment, pas besoin de la commander à cet endroit
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
    print("Génération d'un exercice")
 
    themes = {
        "1": "Fonctions",
        "2": "Listes",
        "3": "Dictionnaires",
        "4": "POO",
        "5": "Fichiers et Exceptions",
    }
 
    print("Choisissez un thème :")
    for numero, nom in themes:
        print(f"{numero}. {nom}")
 
    choix_theme = input("Votre choix (1-5) : ")
 
    if choix_theme not in themes:
        print("Choix de thème invalide.")
 
    niveaux = {
        "1": "Débutant",
        "2": "Intermédiaire",
        "3": "Avancé",
    }
 
    print("Choisissez un niveau :")
    for numero, nom in niveaux:
        print(f"{numero}, {nom}")
 
    choix_niveau = input("Votre choix (1-3) : ")
 
    print(f"Génération d'un exercice niveau {niveaux[choix_niveau]} sur : {themes[choix_theme]}")
    """Gère le processus complet de génération, soumission et évaluation de l'exercice."""
    gemini_client=GeminiClient(api_key,model) #j'instancie ma classe GeminiClient du module core_ai sur la variable gemini_client avec en paramètre la clé API
    reponse=gemini_client.generer_exercice(themes[choix_theme],niveaux[choix_niveau]) # j'appelle la fonction generer_exercice du module core_ai: j'ai besoin d'un thème et d'un niveau
    consigne=reponse.get('consigne','Consigne non disponible') #pour récupérer la consigne
    solution=reponse.get('solution','Solution non disponible') #pour récupérer la solution
    print(consigne) #je récupére une consigne et une solution, j'affiche seulement la consigne
    code_eleve=input("Entrez votre réponse :") #je demande la réponse du user
    evaluation=gemini_client.evaluer_code(code_eleve, consigne, solution) #j'envoie cette réponse, la consigne et la réponse attendue à la fonction evaluer_code du module core_ai
    points_eleve=evaluation.get('score','score non disponible')
    commentaire=evaluation.get('evaluation','Evaluation non disponible')
    print(points_eleve,"/10")
    print(commentaire)
    print("Solution attendue :")
    print(solution) #je récupère le score, le commentaire et la solution attendue et j'affiche
    um.mettre_a_jour_score(utilisateur_courant, points_eleve, consigne) #j'envoie le nom, score et la consigne à la fonction mettre_a_jour_score(nom, points, details_exo) du module user_manager
    um.sauvegarder_utilisateurs(data) #je sauvegarde grâce à la fonction

def main(): 
    """Fonction principale de l'application."""
    api_key=""
    while api_key=="":
        api_key=input('Entrez votre clé API Gemini :') #clé API Gemini demandé 
    while True: #pour relancer systematiquement les choix tant que 
        choix=int(afficher_menu())#première fonction: afficher_menu ==> ça va (retourner un chiffre=choix du menu)
        #je dois utiliser ce chiffre pour déterminer quelle fonction utiliser
        if choix==1:#   option 1: appel de la fonction choisir_utilisateur
            choisir_utilisateur()
        if choix==2: #option 2: appel de la fonction lancer_exercice
            lancer_exercice() 
        if choix==3: #   option 3: sortir de la fonction main
            print("Merci d'avoir joué")
            break #je casse la boucle initiale, le jeu est finie"

if __name__ == "__main__": 
    main()     # Appel de main = début du pprogramme
