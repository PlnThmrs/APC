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
        retourne un fichier JSON "response" avec 2 champs : 'consigne' et 'solution
        pour récupérer les données:
        objetGemini=GeminiClient() #instancier un objet GeminiClient
        reponse=objetGemini.generer_exercice(theme,niveau) #récupérer le fichier dans une variable
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
            # La réponse est directement une chaîne JSON grâce à response_mime_type return json.loads(response.text)
        except json.JSONDecodeError: 
            print("[ERREUR FICHIER] Fichier users.json corrompu. Retourne des données vides.") 
            return {} 
        except Exception as e: 
            print(f"[ERREUR] Erreur de chargement des utilisateurs : {e}") 
            return {}
    def evaluer_code(self, code_eleve, consigne, solution_attendue):
        """Génère le score de l'utilisateur entre 0 et 10 en fonction de la pertinence de sa réponse et par rapport à la consigne et la solution attendue
        retourne un fichier JSON "response" avec  champs JSON: 'score','evalutation'
        pour récupérer les données:
        objetGemini=GeminiClient() #instancier un objet GeminiClient
        reponse=objetGemini.evaluer_code(code_eleve, consigne, solution_attendue) #récupérer le fichier dans une variable
        reponse.get('score','score non disponible') #pour récupérer le score
        reponse.get('evaluation','Evaluation non disponible') #pour récupérer l'évaluation'"""
        prompt = f"""Voici la consigne de l'exercice:{consigne} et voici la solution attendue: {solution_attendue}. Voici la réponse de l'élève: {code_eleve}. Génère un score entre 0 et 10 par rapport à la pertinence de sa réponse (0 étant un échec et 10 une réussite totale), ainsi qu'un bref commentaire sur la pertinence de sa réponse. La sortie doit être STRICTEMENT au format JSON, sans aucun préambule textuel ni balisage Markdown (ex: ```json). Le JSON doit contenir deux clés : 'score' (le score de l'élève) et 'evaluation' (le commentaire sur la pertinence de la réponse de l'élève à l'exercice). """
        if code_eleve=="":
            print("Es-tu sûr d'avoir transmis ta réponse ? ")
        else:
            try: 
                response = self.client.models.generate_content( 
                        model=self.model, 
                        contents=prompt, 
                        config={"response_mime_type": "application/json"} 
                )
                return json.loads(response.text)
                # La réponse est directement une chaîne JSON grâce à response_mime_type return json.loads(response.text)
            except json.JSONDecodeError: 
                print("[ERREUR FICHIER] Fichier users.json corrompu. Retourne des données vides.") 
                return {} 
            except Exception as e: 
                print(f"[ERREUR] Erreur de chargement des utilisateurs : {e}") 
                return {}
objetGemini=GeminiClient() #instancier un objet GeminiClient
consigne="Écrivez une fonction Python nommée `saluer_utilisateur` qui prend un argument : `nom` (une chaîne de caractères). Cette fonction doit retourner une chaîne de caractères qui dit 'Bonjour, [nom] !'.\n\nAprès avoir défini la fonction, appelez-la avec la valeur 'Sophie' et affichez le message retourné par la fonction."
solution_attendue='def saluer_utilisateur(nom):\n    """\n    Prend un nom en argument et retourne un message de salutation.\n    """\n    message = "Bonjour, " + nom + " !"\n    return message\n\n# Appel de la fonction et affichage du résultat\nnom_utilisateur = "Sophie"\nmessage_salutation = saluer_utilisateur(nom_utilisateur)\nprint(message_salutation)\n\n# Résultat attendu : Bonjour, Sophie !'
code_eleve='def saluer_utilisateur(nom):\n    print("Bonjour ",nom)\n\n# Appel de la fonction\nnom_utilisateur = "Bob"\nsaluer_utilisateur(nom_utilisateur)\n# Résultat attendu : Bonjour Bob'
reponse=objetGemini.evaluer_code(code_eleve, consigne, solution_attendue) #récupérer le fichier dans une variable
print(reponse.get('score','Score non disponible')) #pour récupérer le score
print(reponse.get('evaluation','Evaluation non disponible'))