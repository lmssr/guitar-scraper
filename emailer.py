import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(guitars):
    from_email = 'dailyguitars.com'
    to_email = 'luc.mosser86@gmail.com'
    password = 'ton_mot_de_passe'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Guitares électriques gaucher trouvées'

    html = "<h1>Guitares électriques gaucher trouvées</h1>"
    for guitar in guitars:
        html += f"<p>{guitar['title']} - {guitar['price']} - <a href='{guitar['link']}'>Lien</a></p>"

    msg.attach(MIMEText(html, 'html'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()
