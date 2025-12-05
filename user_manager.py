# user_manager.py 
import json 
import os 
FICHIER_UTILISATEURS = 'users.json' 
def charger_utilisateurs(): 
    """Charge les données des utilisateurs depuis users.json.""" 
    try: 
        if not os.path.exists(FICHIER_UTILISATEURS): 
            return {} 
        with open(FICHIER_UTILISATEURS, 'r', encoding='utf-8') as f: 
            return json.load(f) 

    except json.JSONDecodeError: 
        print("[ERREUR FICHIER] Fichier users.json corrompu. Retourne des données vides.") 
        return {} 
    except Exception as e: 
        print(f"[ERREUR] Erreur de chargement des utilisateurs : {e}") 
        return {}
def sauvegarder_utilisateurs(data): 
    """Sauvegarde les données des utilisateurs dans users.json."""
    print("sauvegarde utilsateur")


def creer_ou_charger_utilisateur(nom): 
    """Crée un nouvel utilisateur s'il n'existe pas ou retourne ses données."""
    print("nouveau utilsateur")

def mettre_a_jour_score(nom, points, details_exo): 
    """Met à jour le score et l'historique d'un utilisateur."""
    print("mise à jour utilsateur")
#appel de la fonction
charger_utilisateurs()
