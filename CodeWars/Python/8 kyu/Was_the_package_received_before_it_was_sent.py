def was_package_received_yesterday(tz_from, tz_to, start, duration):
    start_utc = start - tz_from
    delivery_utc = start_utc + duration
    delivery_local = delivery_utc + tz_to
    return delivery_local < 0
