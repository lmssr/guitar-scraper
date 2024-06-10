from scraper import scrape_leboncoin, scrape_reverb
from emailer import send_email
import schedule
import time

def job():
    guitars_leboncoin = scrape_leboncoin()
    guitars_reverb = scrape_reverb()
    guitars = guitars_leboncoin + guitars_reverb
    send_email(guitars)

# Planification de l'exécution quotidienne du script
schedule.every().day.at("08:00").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
