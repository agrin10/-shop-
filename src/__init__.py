from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()



def creat_app():
    app = Flask(__name__,  template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mysecretpassword@localhost:5432/shop"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png"]
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'src\static\images')



    db.init_app(app)
    migrate.init_app(app , db)

    return app


app = creat_app()   
app.app_context().push()