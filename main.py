# -*- coding: utf-8 -*-

from scraper import scrape_leboncoin, scrape_reverb
from emailer import send_email

def job():
    guitars_leboncoin = scrape_leboncoin()
    guitars_reverb = scrape_reverb()
    guitars = guitars_leboncoin + guitars_reverb
    print("Guitars found:", guitars)  # Ajoute ceci pour vérifier les résultats
    send_email(guitars)

if __name__ == "__main__":
    job()
