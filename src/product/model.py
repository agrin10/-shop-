from src import db
from sqlalchemy import inspect
import uuid
import json


### required blog ==>>  https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flas

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String(225), primary_key=True, nullable=False, unique=True, default=str(uuid.uuid4()))
    title = db.Column(db.Text(255),nullable=True )
    price = db.Column(db.Integer() , nullable=True)

    def __reper__(self):
        return f'the product{self.title} and price is {self.price}'
    
    def toDict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    

