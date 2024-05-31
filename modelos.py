from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from bd.basededatos import Base

class Item(Base):
    __tablename__  = "items"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    recomendado = Column(Boolean, index=True)