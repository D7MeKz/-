import os, sys
import json 
import datetime

from flask import request,Response, jsonify
from flask_restx import Resource

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from models import ProductModel
from db.init_db import rdb

class Product(Resource):
    
    # 상품 정보 조회 
    def get(self, product_id):
        question = ProductModel.query.get(product_id)
        return question
        
    def patch(self,product_id):
        pass
    
    def delete(self, product_id):
        pass


# 사용자로부터 title, author, price, address, content을 얻는다.  
class MakeProduct(Resource):
    def post(self):
        body = request.get_json() 
        obj = json.loads(json.dumps(body))
        p = ProductModel(title=obj['title'], author=obj['author'],
            price=obj['price'],address=obj['address'], content=obj['content'],
            created_date= datetime.datetime.now(), modified_date=datetime.datetime.now(),
            status=False, user_id=obj['user_id'])
        
        rdb.session.add(p)
        rdb.session.commit()
        return {"status" : "check"}


         
        
        
        
        
