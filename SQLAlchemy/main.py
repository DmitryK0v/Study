from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///webinar.db', echo=True)
base = declarative_base()


class User(base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return '<User(name="{}", fullname="{}">'.format(self.name, self.fullname)


base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()