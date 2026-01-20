from datetime import datetime
from sqlalchemy import Float, String, DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

# Values for metrics overview
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


# Values for table
class MarketExchanges(Base):
    __tablename__ = "market_overview"

    id: Mapped[int] = mapped_column(primary_key=True)

    exchange_id: Mapped[str] = mapped_column(String, index=True)
    base_id: Mapped[str] = mapped_column(String, index=True)
    quote_id: Mapped[str] = mapped_column(String, index=True)

    base_symbol: Mapped[str] = mapped_column(String)
    quote_symbol: Mapped[str] = mapped_column(String)

    price_usd: Mapped[float] = mapped_column(Float)
    volume_usd_24h: Mapped[float] = mapped_column(Float)
    volume_percent: Mapped[float] = mapped_column(Float)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

# Day Volumes
class MarketDailyVolume(Base):
    __tablename__ = "market_daily_volume"

    id: Mapped[int] = mapped_column(primary_key=True)
    volume_usd_24h: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )