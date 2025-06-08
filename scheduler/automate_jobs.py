from apscheduler.schedulers.background import BackgroundScheduler
from core.data_collector import fetch_odds

def start():
    # Set up background scheduler to periodically fetch odds
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_odds, 'interval', minutes=30)
    scheduler.start()