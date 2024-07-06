from flask import Flask, render_template, jsonify,request
from werkzeug.exceptions import HTTPException
from controller import retrive_alert_controlle
import os

app =Flask(__name__)

@app.route('/')
@app.route('/homepage')
def index():
    return render_template('index.html')


@app.route('/products' , methods=['GET'])
def show_product():
    if request.method == 'GET':
        product_data=retrive_alert_controlle()
        return render_template('product.html' , product_data=product_data)
    else:
        return "not the vailed methode"



@app.errorhandler(Exception)
def notfound(e):
    code = 404
    if isinstance(e, HTTPException):
        code = e.code
    return render_template('404.html')



if __name__ == "__main__":
    app.run(debug=True)
