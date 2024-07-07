from flask import Flask, jsonify , request ,session
from db import products_data
import uuid



def retrive_product_controlle():
    response=[]
    products_data_controller= products_data
    for product in products_data_controller:
        response.append(dict(product))
    return jsonify(data=response)


def add_product(request):

    request_data=request.json
    new_product = {
        "id":str(uuid.uuid4()),
        "title": request_data.get("name_pro"),
        "price":request_data.get("price_pro"),
        # "imageUrl":str(request_data.get("imageurl")),

    }
    
    products_data.append(new_product)
    return jsonify(data=products_data)

    

    
    

    
   

        

        



    
    
    



