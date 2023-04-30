import os, sys
import json 
import datetime

# * lib
from flask import request, jsonify, Blueprint, redirect
from flask_jwt_extended import jwt_required,get_jwt_identity
import requests
import sqlalchemy.exc

# * User defined
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from init.init_db import rdb
import utils.error.custom_error as error
from models import PaymentRefreshToken

# * Test이기 때문에 별도로 Client_id와 password는 고정. 
CLIENT_ID = '1d1099e6-8c17-4ac3-956c-2e9bd6039c19'
CLIENT_PASSWORD = 'e51b7de9-9647-4760-8707-e77e7a53bce6'
STATE_CODE = '12345678901234567890124456729112'
REDIRECT_URI = 'http://localhost:6000/payment/auth'
URI_BASE = 'https://testapi.openbanking.or.kr/oauth/2.0'

bp = Blueprint('payment', __name__, url_prefix='/payment')

@bp.route('/auth',methods=["POST"])
# @jwt_required()
def authorization():
    auth_url = f'https://testapi.openbanking.or.kr/oauth/2.0/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=login+inquiry+transfer&state={STATE_CODE}&auth_type=0&cellphone_cert_yn=Y&authorized_cert_yn=N'
    
    
    try:
        res = requests.get(auth_url)
        if res:
            return redirect(res.url)
        if res.status_code == 200:
            res_json = res.text
            print(res_json)
            req_data = {
                'code':res_json['code'],
                'client_id':CLIENT_ID,
                'client_secret':CLIENT_PASSWORD,
                'redirect_uri':REDIRECT_URI,
                'grant_type':'authorization_code'
            }

            # Token 발급
            token_res = requests.post(f'{URI_BASE}/token',data=json.loads(req_data))
            if token_res.status_code == 200:
 
                token_json = token_res.json()
                print(token_json)
               #  user_id = get_jwt_identity()
                
                # Refresh token DB에 저장 
                # refresh_session = PaymentRefreshToken(token=token_json['refresh_token'],user_id=user_id)
                # rdb.session.add(refresh_session)
                # rdb.commit()
                
                return jsonify({"status_code" : 200, "message":"Success"}), 200 
            
            else:
                return jsonify({'message':'Token Generation Error'}), 404
        else:
            return jsonify({'message':'Authorization Error'}), 404
    except requests.exceptions.Timeout as e:
        print("Timeout Error : ", e)
    except requests.exceptions.ConnectionError as e:
        print("Error Connecting : ", e)
    except requests.exceptions.HTTPError as e:
        print("Http Error : ", e)
    except requests.exceptions.RequestException as e:
        print("AnyException : ", e)

def get_token():
    pass