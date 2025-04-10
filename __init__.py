from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')#Comm

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)

@app.route('/decrypt/<message>')
def decrypt(message):
    try:
        key = session.get('key')
        if not key:
            return "Clé manquante dans la session. Veuillez d'abord chiffrer quelque chose.", 400
        f = Fernet(key)
        decrypted_message = f.decrypt(message.encode()).decode()
        return f"Texte déchiffré : {decrypted_message}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}", 500
def get_fernet_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

@app.route('/encrypt_custom/<key>/<message>')
def encrypt_custom(key, message):
    try:
        fernet_key = get_fernet_key(key)
        f = Fernet(fernet_key)
        encrypted = f.encrypt(message.encode()).decode()
        return f"Texte chiffré avec clé perso : {encrypted}"
    except Exception as e:
        return f"Erreur de chiffrement : {str(e)}"

@app.route('/decrypt_custom/<key>/<message>')
def decrypt_custom(key, message):
    try:
        fernet_key = get_fernet_key(key)
        f = Fernet(fernet_key)
        decrypted = f.decrypt(message.encode()).decode()
        return f"Texte déchiffré avec clé perso : {decrypted}"
    except Exception as e:
        return f"Erreur de déchiffrement : {str(e)}"

# Lancement de l'app Flask
if __name__ == "__main__":
    app.run(debug=True)

