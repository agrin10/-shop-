from src import app
from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.exceptions import HTTPException
from .controller import retrieve_product_controller , add_product
from src import db
import uuid
from .model import Product



# getting the product data as json file
@app.route('/products', methods=['GET'])
def show_product():
    if request.method == 'GET':
        data= retrieve_product_controller()
        return render_template('product.html', product_data=data)
    else:
        return "Invalid method. Only GET is supported for this route."

# adding the product to the database
@app.route('/add', methods=['POST', 'GET'])
def adding_product():
    if request.method == 'POST':
        product_name = add_product()
        return product_name
    else:
        return render_template('add_product.html')

# # 404 error page
# @app.errorhandler(Exception)
# def notfound(e):
#     code = 404
#     if isinstance(e, HTTPException):
#         code = e.code
#     return render_template('404.html', error=e), code
