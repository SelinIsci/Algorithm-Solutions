import math


def movie(card, ticket, perc):
    n = 0
    cost_b = card
    cost_a = 0
    next_ticket_price = ticket * perc

    while math.ceil(cost_b) >= cost_a:
        n += 1
        cost_a = ticket * n
        cost_b += next_ticket_price
        next_ticket_price *= perc
    return n
