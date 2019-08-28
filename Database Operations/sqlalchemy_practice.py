import pymysql
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:1234@localhost/test_python_mysql')
session = sessionmaker(bind=engine)()

Base = declarative_base()
class Customer(Base):

    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    address = Column(String)

    def __init__(self, username, address):
        self.username = username
        self.address = address


# customer = Customer("Rocky1", "123 NE road")
# session.add(customer)
# session.commit()

result = session.query(Customer).all()

for x in result:
    print(str(x.id)+", "+x.username+", "+x.address)
