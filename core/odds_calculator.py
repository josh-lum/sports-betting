def calculate_expected_value(probability, odds):
    # Calculate expected value: (prob * payout) - (1 - prob)
    return (probability * odds) - (1 - probability)