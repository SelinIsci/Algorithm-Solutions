import math


def calculate_tip(amount, rating):
    rating = rating.lower()

    rates = {
        "terrible": 0,
        "poor": 0.05,
        "good": 0.10,
        "great": 0.15,
        "excellent": 0.20,
    }

    if rating in rates:
        return math.ceil(amount * rates[rating])
    else:
        return "Rating not recognised"
