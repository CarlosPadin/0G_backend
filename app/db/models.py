from datetime import datetime
from sqlalchemy import Float, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class MarketMetric(Base):
    __tablename__ = "market_metrics"

    id: Mapped[int] = mapped_column(primary_key=True)
    asset_id: Mapped[str] = mapped_column(String, index=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    avg_price_usd: Mapped[float] = mapped_column(Float)
    total_volume_24h: Mapped[float] = mapped_column(Float)
    price_change: Mapped[float | None] = mapped_column(Float, nullable=True)
