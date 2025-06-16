import requests
from bs4 import BeautifulSoup
import smtplib
import os

def check_rdv():
    url = "https://algeria.blsspainvisa.com/appointment.php"  # À adapter si le vrai lien est différent
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        if "No appointment" in soup.text or "Aucun rendez-vous" in soup.text:
            print("Pas de rendez-vous pour l’instant.")
        else:
            send_email("⚠️ Un rendez-vous BLS Oran2 semble disponible !")

    except Exception as e:
        print(f"Erreur lors de la requête : {e}")

def send_email(message):
    sender = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASSWORD"]
    receiver = os.environ["EMAIL_USER"]

    subject = "Notification BLS"
    body = f"{message}\n\nLien : https://algeria.blsspainvisa.com/appointment.php"
    msg = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg)

if __name__ == "__main__":
    check_rdv()
