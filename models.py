from sqlalchemy import Integer,String,Column,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('sqlite:///db.db')
Base=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)

    def __repr__(self):
        return f"name={self.name} email={self.email}"
