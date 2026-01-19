
def calculate_metrics(markets: list[dict]):
    total_volume = 0.0
    weighted_price_sum = 0.0

    for m in markets:
        price = float(m["priceUsd"])
        volume = float(m["volumeUsd24Hr"])

        total_volume += volume
        weighted_price_sum += price * volume

    avg_price = (
        weighted_price_sum / total_volume
        if total_volume > 0
        else 0
    )

    return {
        "average_price_usd": avg_price,
        "total_volume_24h": total_volume,
    }
