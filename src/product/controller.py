from flask import Flask, jsonify , request ,session , redirect  , url_for,send_from_directory
from src.product.model import Product
from src import db
import uuid
from src.product import urls
from werkzeug.utils import secure_filename
import os
from src import app
import imghdr


def retrieve_product_controller():
    response = []
    products_data_controller = Product.query.all()
    for product_data in products_data_controller:
        response.append(product_data.toDict())
    return {"data": response}

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
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new_product = Product(id=str(uuid.uuid4()), title=title, price=price, image_path=filename)
                db.session.add(new_product)
                db.session.commit()
                return redirect(url_for('show_product'))
        return 'No file uploaded', 400
    



def updat_product(product_id):
    if request.is_json:
        product = Product.query.get(product_id)
        if not product:
            return {"message": "Product not found"}, 404

        data = request.json
        product.title = data.get('title')
        product.price = data.get('price')
        product.image = data.get('image')

        db.session.commit()
        return jsonify({"message": "Product updated successfully"})
    else:
        return {"message": "Invalid request format, requires JSON data"}, 400
    


def delete_product(product_id):
    if request.is_json: 
        product = Product.query.get(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"})
    else:
        return {"message": "Unsupported Media Type"}, 415

        
    

    



