from flask import Flask, jsonify , request ,session , redirect  , url_for
from product.model import Product
from __init__ import db
import uuid
from product.urls import *
 
def retrive_product_controlle():
    response=[]
    products_data_controller= Product.query.all()
    for products_data in products_data_controller:
        response.append(products_data.toDict())
    return {"data":response}


def add_product():
    if request.is_json:
        data_pro = request.json 
        new_product = Product(id= uuid.uuid4() , title= data_pro['title'] , price=data_pro['price'])        
        db.session.add(new_product)
        db.session.commit()
        return jsonify(message = "Added new product datas successfully!")       
    else:
        title = request.form.get('name_pro')
        price = request.form.get('price_pro')
        new_product = Product(id=uuid.uuid4(), title=title, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('show_product'))
    
        



    
    
    



