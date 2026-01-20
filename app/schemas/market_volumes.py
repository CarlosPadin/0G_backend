from pydantic import BaseModel
from datetime import datetime

class DailyVolume(BaseModel):
    timestamp: datetime
    volume_usd_24h: float

    model_config = {"from_attributes": True}
