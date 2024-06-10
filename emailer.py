# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(guitars):
    from_email = 'luc.mosser86@gmail.com'
    to_email = 'luc.mosser86@gmail.com'
    password = 'eihe rmpl nsdd uydp'  # Utilise ton mot de passe d'application ou ton mot de passe Gmail

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Guitares électriques gaucher trouvées'

    html = "<h1>Guitares électriques gaucher trouvées</h1>"
    for guitar in guitars:
        html += f"<p>{guitar['title']} - {guitar['price']} - <a href='{guitar['link']}'>Lien</a></p>"

    msg.attach(MIMEText(html, 'html'))

    try:
        print("Connexion au serveur SMTP...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        print("Connexion...")
        server.login(from_email, password)
        print("Envoi de l'email...")
        server.send_message(msg)
        server.quit()
        print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Échec de l'envoi de l'email: {e}")