from flask import Flask, jsonify
from db import products_data
import uuid

def retrive_alert_controlle():
    response=[]
    products_data_controller= products_data
    for product in products_data_controller:
        response.append(dict(product))
    return jsonify(data=response)