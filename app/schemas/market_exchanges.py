from pydantic import BaseModel

class MarketExchanges(BaseModel):
    exchange_id: str
    base_id: str
    base_symbol: str
    quote_id: str
    quote_symbol: str
    price_usd: float
    volume_usd_24h: float
    volume_percent: float
    price_change: float | None

    model_config = {
        "from_attributes": True  # <- allows to send objects to SQLAlchemy
    }
