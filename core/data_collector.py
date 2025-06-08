import requests
import json
import os
from datetime import datetime
from database.models import Bet
from app import db

def load_api_key():
    # Load API key from secret.txt file
    with open('secret.txt', 'r') as file:
        return file.read().strip()

def fetch_odds():
    # Construct the request URL using your API key
    api_key = load_api_key()
    url = f"https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&apiKey={api_key}"

    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Ensure the instance/json directory exists for storing snapshots
        os.makedirs("instance/json", exist_ok=True)
        filename = f"instance/json/odds_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        # Write full JSON response to a timestamped file for debugging/history
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        # Parse odds and insert relevant entries into the database
        for event in data:
            teams = event.get("teams", [])
            bookmakers = event.get("bookmakers", [])
            if len(teams) < 2 or not bookmakers:
                continue

            for bm in bookmakers:
                for market in bm.get("markets", []):
                    if market.get("key") != "h2h":
                        continue

                    for outcome in market.get("outcomes", []):
                        team = outcome.get("name")
                        odds = outcome.get("price")

                        if team and odds is not None:
                            # Create Bet instance and add to session
                            bet = Bet(team=team, odds=odds, timestamp=datetime.utcnow())
                            db.session.add(bet)

        # Commit all collected bets to the database
        db.session.commit()

        return data
    except Exception as e:
        from monitoring.logger import log_error
        log_error(f"Error fetching odds: {e}")
        return []
