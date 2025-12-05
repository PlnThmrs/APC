# core_ai.py 
import os 
import json 
from google import genai 
from google.genai import errors

class GeminiClient :
    """Gère toutes les interactions avec l'API Gemini"""
    def __init__(self, api_key="AIzaSyA-NKOz4d_VEnXYrP3TrKBadEYonDma5-0"): 
        """Initialise le client Gemini.""" 
        if not api_key: 
            raise ValueError("La clé API Gemini est manquante.") 
    # Le client la clé passée ou la variable d'environnement GEMINI_API_KEY 
        self.client = genai.Client(api_key=api_key) 
        self.model = 'gemini-2.5-flash' # Modèle rapide et efficace pour les tâches textuelles 
    def generer_exercice(self, theme, niveau): 
        """Génère une consigne et une solution attendue en JSON.
        retourne un fichier response.txt avec 2 champs JSON: 'consigne' et 'solution
        pour récupérer les données:
        objetGemini=GeminiClient() #instancier un objet GeminiClient
        reponse=test.generer_exercice(theme,niveau) #récupérer le fichier dans une variable
        reponse.get('consigne','Consigne non disponible') #pour récupérer la consigne
        reponse.get('solution','Solution non disponible') #pour récupérer la solution""" 
        prompt = f""" Génère un exercice de programmation Python de niveau {niveau} sur le thème '{theme}'. La sortie doit être STRICTEMENT au format JSON, sans aucun préambule textuel ni balisage Markdown (ex: ```json). Le JSON doit contenir deux clés : 'consigne' (le texte de l'exercice) et 'solution' (le code Python attendu). """
        try: 
            response = self.client.models.generate_content( 
                    model=self.model, 
                    contents=prompt, 
                    config={"response_mime_type": "application/json"} 
            )
            return json.loads(response.text)
            # La réponse est directement une chaîne JSON grâce à response_mime_type return json.loads(response.txt)
        except json.JSONDecodeError: 
            print("[ERREUR FICHIER] Fichier users.json corrompu. Retourne des données vides.") 
            return {} 
        except Exception as e: 
            print(f"[ERREUR] Erreur de chargement des utilisateurs : {e}") 
            return {}
    def evaluer_code(self, code_eleve, consigne, solution_attendue):
        """Sauvegarde les données des utilisateurs dans users.json."""