from flask import Flask, render_template
from __init__ import creat_app 
from __init__ import db
from product.model import Product


app = creat_app()

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

from product.urls import *

if __name__ == "__main__":
    app.run(debug=True)
    # db.create_all()
        
    
