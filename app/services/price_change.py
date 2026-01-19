def calculate_price_change(current: float, previous: float | None) -> float | None:
    if previous is None or previous <= 0:
        return None

    return ((current - previous) / previous) * 100
