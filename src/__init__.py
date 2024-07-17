from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()



def creat_app():
    app = Flask(__name__,  template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mysecretpassword@localhost:5432/shop.db"

    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = creat_app()
