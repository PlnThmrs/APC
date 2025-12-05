# user_manager.py 
import json 
import os 
FICHIER_UTILISATEURS = 'users.json' 
def charger_utilisateurs(): 
    """Charge les données des utilisateurs depuis users.json.""" 
    try: 
        if not os.path.exists(FICHIER_UTILISATEURS): 
            return {"users": []} 
        with open(FICHIER_UTILISATEURS, 'r', encoding='utf-8') as f: 
            return json.load(f) 

    except json.JSONDecodeError: 
        print("[ERREUR FICHIER] Fichier users.json corrompu. Retourne des données vides.") 
        return {"users": []} 
    except Exception as e: 
        print(f"[ERREUR] Erreur de chargement des utilisateurs : {e}") 
        return {"users": []}
    
    
def sauvegarder_utilisateurs(data):
    """Sauvegarde les données des utilisateurs dans users.json."""
    try:
        # Ouverture du fichier en écriture (écrase l'ancien contenu)
        with open(FICHIER_UTILISATEURS, 'w', encoding='utf-8') as f:
            # Conversion du dictionnaire Python en JSON formaté
            json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        # Affichage d'une erreur si la sauvegarde échoue
        print(f"[ERREUR] Impossible de sauvegarder les utilisateurs : {e}")

def creer_ou_charger_utilisateur(nom): 
    """Crée un nouvel utilisateur s'il n'existe pas ou retourne ses données."""
    data = charger_utilisateurs()

    # Vérifier si l'utilisateur existe déjà
    for user in data["users"]:
        if user.get("nom") == nom:
            print("Utilisateur" ,nom," déjà existant.")
            return user

    # Sinon, créer un nouvel utilisateur
    nouvel_utilisateur = {
        "nom": nom,
        "score": 0,
        "historique": []
    }
    data["users"].append(nouvel_utilisateur)
    sauvegarder_utilisateurs(data)
    print("Nouvel utilisateur",nom,"créé.")
    return nouvel_utilisateur


def mettre_a_jour_score(nom, points, details_exo): 
    """Met à jour le score et l'historique d'un utilisateur."""
    data = charger_utilisateurs()
    for user in data["users"]:
        if user.get("nom") == nom:
            user["score"] += points
            user["historique"].append({"points": points, "details": details_exo})
            sauvegarder_utilisateurs(data)     # Sauvegarde après modification
            print("Score mis à jour pour",nom)
            return user
    print("Utilisateur",nom,"introuvable.")
    return None

creer_ou_charger_utilisateur("magalie")
mettre_a_jour_score("magalie",10,[10, "python"])



