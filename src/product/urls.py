from src import app
from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.exceptions import HTTPException
from .controller import retrieve_product_controller , add_product , updat_product , delete_product
from src import db
import uuid
from .model import Product
from flask import send_from_directory



# getting the product data as json file
@app.route('/products', methods=['GET'])
def show_product():
    if request.method == 'GET':
        data = retrieve_product_controller()
        page = request.args.get('page', 1, type=int)
        products = Product.query.paginate(page=page, per_page=6, error_out=False)
        return render_template('product.html', product_data=products, pagination=products)
    else:
        return "Invalid method. Only GET is supported for this route.", 405


    # if request.method == 'GET':
    #     data= retrieve_product_controller()
    #     page = request.args.get('page', 1, type=int)  # Default to page 1 if not specified
        # products = Product.query.paginate(page=page, per_page=4, error_out=False)

    #     return render_template('product.html', product_data=data , pagination=products)
    # else:
    #     return "Invalid method. Only GET is supported for this route."
# adding the product to the database
@app.route('/add', methods=['POST', 'GET'])
def adding_product():
    if request.method == 'POST':
        product_name = add_product()
        return product_name
    else:
        return render_template('add_product.html')
    

@app.route('/edit-product/<string:product_id>', methods=['PUT'])
def edit_product(product_id):

    if request.method == 'PUT':
        new_product_replaced = updat_product(product_id)
        return new_product_replaced
    elif request.method =='GET':
        return {"message" : "not allowed"}
    

@app.route('/delete-product/<string:product_id>', methods=['DELETE'])
def deleted_product(product_id):
    if request.method == 'DELETE':
        remove_product = delete_product(product_id)
        return remove_product
    elif request.method == 'GET':
        return {"message": "Method not allowed"}

# # 404 error page
# @app.errorhandler(Exception)
# def notfound(e):
#     code = 404
#     if isinstance(e, HTTPException):
#         code = e.code
#     return render_template('404.html', error=e), code
