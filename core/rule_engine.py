def filter_profitable_bets(bets, threshold=0.1):
    # Filter bets with expected value above a defined threshold
    return [b for b in bets if b['expected_value'] > threshold]