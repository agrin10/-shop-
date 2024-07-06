from main import app
from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException
from .controller import retrive_alert_controlle

@app.route('/products' , methods=['GET'])
def show_product():
    if request.method == 'GET':
        product_data=retrive_alert_controlle()
        return render_template('product.html' , product_data=product_data)
    else:
        return "Invalid method. Only GET is supported for this route."



@app.errorhandler(Exception)
def notfound(e):
    code = 404
    if isinstance(e, HTTPException):
        code = e.code
    return render_template('404.html', error=e), code

