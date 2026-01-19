from pydantic import BaseModel
from datetime import datetime

class MarketMetric(BaseModel):
    asset_id: str
    timestamp: datetime
    avg_price_usd: float
    total_volume_24h: float
    price_change: float | None

    model_config = {
        "from_attributes": True  # <- allows to send objects to SQLAlchemy
    }