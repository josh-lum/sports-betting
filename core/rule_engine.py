from .data_collector import get_draftkings_data
from .odds_calculator import is_value_bet

def suggest_bets():
    games = get_draftkings_data()
    suggestions = []

    for game in games:
        if is_value_bet(game):
            suggestions.append(game)

    return suggestions
