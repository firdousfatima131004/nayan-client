from sqlalchemy import Column , Integer , String,ForeignKey,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    quantity = Column(Integer, default=1)
    product = relationship('Product', back_populates='carts')
    user = relationship('User', back_populates='carts')
    
    
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    productname = Column(String, nullable=False)
    productDesc = Column(String, nullable=False)
    productPrice = Column(Float, nullable=False)
    img = Column(String, nullable=False)
    carts = relationship('Cart', back_populates='product')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(Integer , unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    carts = relationship('Cart', back_populates='user')

     

     
