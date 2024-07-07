from main import app
from flask import Flask, render_template, request , jsonify
from werkzeug.exceptions import HTTPException
from .controller import retrive_product_controlle , add_product
from db import products_data
import uuid


@app.route('/products', methods=['GET'])
def show_product():
    if request.method == 'GET':
        product_data = retrive_product_controlle()
        # link_product = show_product()
        return render_template('product.html', product_data=product_data)
    else:
        return "Invalid method. Only GET is supported for this route."


@app.route('/add', methods=['POST', 'GET'])
def adding_product():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            add_new={                
                "title": data['title'],
                "price": data['price'],            
            }
            products_data.append(add_new)
            return jsonify(data=products_data)
        else:      
            product_recieved= add_product(request)
            return product_recieved

    else: 
        return render_template('add_product.html')
    
    


# @app.errorhandler(Exception)
# def notfound(e):
#     code = 404
#     if isinstance(e, HTTPException):
#         code = e.code
#     return render_template('404.html', error=e), code
