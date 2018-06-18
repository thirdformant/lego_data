from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class Sets(Base):
    __tablename__ = "sets"
    set_num = Column(String(25), primary_key=True)
    name = Column(String(255))
    year = Column(Integer)
    theme_id = Column(Integer, ForeignKey("themes.id"))
    num_parts = Column(Integer)

class Themes(Base):
    __tablename__ = "themes"
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(255))
    parent_id = Column(Integer)

if __name__ == "__main__":
    engine = create_engine('sqlite:///data/db/lego_db_test.db')
    Base.metadata.create_all(engine)
