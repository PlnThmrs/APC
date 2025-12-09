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
    if nom in data:
            print(f"Utilisateur {nom} déjà existant.")
            return data[nom]

    # Sinon, créer un nouvel utilisateur
    data[nom] = {'score':0,'historique':[]}
    sauvegarder_utilisateurs(data)
    print(f"Nouvel utilisateur {nom} créé.")
    return data[nom]

def mettre_a_jour_score(nom, note, niveau, theme): 
    """Met à jour le score et l'historique d'un utilisateur."""
    data = charger_utilisateurs()
    if nom in data:
        data[nom]['score'] += (note*10)
        data[nom]['historique'].append({"theme": theme, "niveau":niveau, "note": note})
        sauvegarder_utilisateurs(data) #Sauvegarde après modification
        print("Score mis à jour pour",nom)
        return data[nom]
    else:
        print(f"Utilisateur {nom} introuvable.")
        return None