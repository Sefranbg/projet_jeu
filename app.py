from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Vérification du dossier static
if not os.path.exists('static'):
    print("Erreur : Le dossier 'static' n'existe pas. Veuillez créer ce dossier et y placer les images des drapeaux.")
if not os.path.exists('templates'):
    print("Erreur : Le dossier 'templates' n'existe pas. Veuillez créer ce dossier et y placer index.html et quiz.html.")

# Liste des combinaisons de pays et du pays correct
quiz_combinations = [
    {"countries": ["Finlande", "Espagne", "Luxembourg", "Suède"], "correct": "Espagne"},
    {"countries": ["Irlande", "Slovaquie", "Lituanie", "Estonie"], "correct": "Estonie"},
    {"countries": ["Finlande", "Luxembourg", "Roumanie", "Suède"], "correct": "Suède"},
    {"countries": ["Italie", "Bulgarie", "Belgique", "Hongrie"], "correct": "Belgique"},
    {"countries": ["Bulgarie", "Malte", "Autriche", "Slovaquie"], "correct": "Slovaquie"},
    {"countries": ["Pologne", "Grèce", "Roumanie", "Estonie"], "correct": "Grèce"},
    {"countries": ["Croatie", "Autriche", "Luxembourg", "Allemagne"], "correct": "Luxembourg"},
    {"countries": ["Lituanie", "Italie", "Hongrie", "Allemagne"], "correct": "Italie"},
    {"countries": ["Belgique", "Portugal", "Slovaquie", "Lituanie"], "correct": "Lituanie"},
    {"countries": ["Finlande", "Hongrie", "Pologne", "Estonie"], "correct": "Pologne"},
    {"countries": ["Irlande", "Roumanie", "Espagne", "Estonie"], "correct": "Roumanie"},
    {"countries": ["Roumanie", "Bulgarie", "Allemagne", "Portugal"], "correct": "Bulgarie"},
    {"countries": ["Grèce", "Malte", "Lituanie", "France"], "correct": "Malte"},
    {"countries": ["Tchéquie", "Estonie", "Croatie", "Roumanie"], "correct": "Tchéquie"},
    {"countries": ["Irlande", "Malte", "Roumanie", "Chypre"], "correct": "Irlande"},
    {"countries": ["Autriche", "Portugal", "Roumanie", "Malte"], "correct": "Portugal"},
    {"countries": ["Chypre", "Slovaquie", "Italie", "Finlande"], "correct": "Chypre"},
    {"countries": ["Belgique", "Malte", "Finlande", "Autriche"], "correct": "Autriche"},
    {"countries": ["Espagne", "Luxembourg", "Suède", "Croatie"], "correct": "Croatie"},
    {"countries": ["Pays-Bas", "Slovénie", "Bulgarie", "Pologne"], "correct": "Slovénie"},
    {"countries": ["Hongrie", "Tchéquie", "Espagne", "Grèce"], "correct": "Hongrie"},
    {"countries": ["Malte", "Pays-Bas", "Irlande", "Espagne"], "correct": "Pays-Bas"},
    {"countries": ["Lituanie", "Espagne", "Lettonie", "Danemark"], "correct": "Lettonie"},
    {"countries": ["Allemagne", "Italie", "Chypre", "Danemark"], "correct": "Danemark"},
    {"countries": ["France", "Danemark", "Hongrie", "Finlande"], "correct": "Finlande"},
    {"countries": ["Allemagne", "Suède", "Espagne", "Belgique"], "correct": "Allemagne"},
]

# Drapeaux associés aux pays
flags = {
    "Allemagne": "allemagne.png",
    "Autriche": "autriche.png",
    "Belgique": "belgique.png",
    "Bulgarie": "bulgarie.png",
    "Chypre": "chypre.png",
    "Croatie": "croatie.png",
    "Danemark": "danemark.png",
    "Espagne": "espagne.png",
    "Estonie": "estonie.png",
    "Finlande": "finlande.png",
    "France": "france.png",
    "Grèce": "grece.png",
    "Hongrie": "hongrie.png",
    "Irlande": "irlande.png",
    "Italie": "italie.png",
    "Lettonie": "lettonie.png",
    "Lituanie": "lituanie.png",
    "Luxembourg": "luxembourg.png",
    "Malte": "malte.png",
    "Pays-Bas": "pays-bas.png",
    "Pologne": "pologne.png",
    "Portugal": "portugal.png",
    "Tchéquie": "tchequie.png",
    "Roumanie": "roumanie.png",
    "Slovaquie": "slovaquie.png",
    "Slovénie": "slovenie.png",
    "Suède": "suede.png"
}

@app.route('/')
def index():
    print("Page d'accueil chargée")
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    print("Page de quiz chargée")
    selected_quiz = random.choice(quiz_combinations)
    countries = [{"name": country, "flag": flags[country]} for country in selected_quiz["countries"]]
    correct_country = selected_quiz["correct"]
    return render_template('quiz.html', countries=countries, correct_country=correct_country)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Utilise le port de Render ou 10000 par défaut
    print(f"Démarrage du serveur Flask sur http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
