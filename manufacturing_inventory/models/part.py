from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    unit = Column(String, nullable=False)  # kg, pcs, litre, etc.
    quantity = Column(Float, default=0.0)
    reorder_threshold = Column(Float, default=10.0)
    is_active = Column(Boolean, default=True)