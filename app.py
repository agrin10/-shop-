from flask import Flask, render_template
from src import app 
from src import db


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

from src.product import urls


if __name__ == "__main__":
    
    app.run(debug=True)
    db.create_all()
   
        
    
