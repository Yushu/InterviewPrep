from sqlalchemy import Column, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    product_name = Column(String, primary_key=True)
    product_licenses = Column(String)

class User(Base):
    __tablename__ = 'users'
    user_name = Column(String, primary_key=True)
    product_licenses = Column(String)

def main():
    engine = create_engine("mysql+mysqlconnector://test:@db/ri_db")
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    # Write your code here
    for name, fullname in s.query(User.user_name, User.product_licenses):
        print("User " +name+ ":")
        uname = fullname.split(",")
        for x,y in s.query(Product.product_name, Product.product_licenses):
            count = 0
            for i in y.split(","):
                if i in uname:
                    count = 1
            if count == 1:
                print('  '+x+": "+"true")
            else:
                print('  '+x+": "+"false")

    s.commit()
    s.close()

if __name__ == '__main__':
    main()
