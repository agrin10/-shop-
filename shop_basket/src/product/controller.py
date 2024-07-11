from flask import Flask, jsonify , request ,session
from product.model import Product
from __init__ import db
import uuid
 
def retrive_product_controlle():
    response=[]
    products_data_controller= Product.query.all()
    for products_data in products_data_controller:
        response.append(products_data.toDict())
    return jsonify(data=response) 


def add_product():

    data_pro = request.json 
    new_product = Product(id= uuid.uuid4() , title= data_pro['title'] , price=data_pro['price'])        
    db.session.add(new_product)
    db.session.commit()
    return jsonify(message = "Added new product datas successfully!")       

        



    
    
    



