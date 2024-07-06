from flask import Flask, render_template
from product.controller import retrive_alert_controlle
from __init__ import creat_app

app = creat_app()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

from product.urls import *

if __name__ == "__main__":
    app.run(debug=True)
