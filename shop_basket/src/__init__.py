from flask import Flask

def creat_app():
    app = Flask(__name__,  template_folder='templates')

    app.config['EXPLAIN_TEMPLATE_LOADING'] = True


    return app