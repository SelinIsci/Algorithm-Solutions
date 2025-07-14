def fuel_price(litres, price_per_litre):
    discount = min((litres // 2) * 0.05, 0.25)
    total_cost = litres * (price_per_litre - discount)
    return round(total_cost, 2)
