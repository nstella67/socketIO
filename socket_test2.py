from flask import Flask, render_template,request,session,jsonify
from flask_socketio import SocketIO, emit,disconnect
from flask_session import Session
import json
import os
from logging import log
import utils.common_util as common_util
from utils.common_util import respond
from api.events import MyServerNamespace

##############################
# socket_test.py
# Class Based Event Driven
# Dev. JJ PARK
##############################


######################
# APP Setting
######################
app = Flask(__name__)       # MAKING FLASK APP BY FILENAME
app.config['SECRET_KEY'] = 'secret!12345678'
app.debug = True   # or True
Session(app)        # 세션 할당

######################
# Socket Setting
######################
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
# socketio.init_app(app) 이 명령은 위 라인에서 app이 추가될 경우 생략가능

# socket에 namespace를 'MyServer'를 등록한다 (multiplexing이 가능해짐)
# 주의 : Namespace를 쓸 경우 client도 맞춰 주어야 한다. client 코드 : var socket = io.connect('http://' + document.domain + ':' + location.port + '/' + 'MyServer');
socketio.on_namespace(MyServerNamespace('/MyServer'))

# socket run은 아래와 같이 실행
if __name__ == '__main__':
    socketio.run(app)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/send')         # html 파일을 로딩한다.
# def send():
#     return render_template('send.html')
#
# @app.route('/receive')
# def receive():
#     return "I got signal and call"

@app.route('/order_insert')
def order_process(_code):

    if _code == 00 :
        print('00')
    elif _code == 10:
        print('10')
    elif _code == 20:
        print('20')
    elif _code == 30:
        print('30')
    elif _code == 40:
        print('40')
    elif _code == 50:
        print('50')
    elif _code == 60:
        print('60')
        pass

    # [참고] 공유 기사가 콜을 잡았을때 공유가 된 오더사, 공유 기사가 속한 agency에 기사가 콜을 잡고 운행할때 이후만 띄워준다

# order_id로 order_data를 얻어온다.
def get_order_data(order_id) :

    # STATUS를 업데이트 못하도록 락을 건다.

    # DB로 부터 자료를 뽑아온다.
    order_data = dict()
    order_data['ORDER_ID'] = "1232"
    order_data['AGENCY_ID'] = "384"
    order_data['CUST_ID'] = "3736"
    order_data['ORDER_DT'] = "Tue, 01 Nov 2022 14:27:38 GMT"

    return order_data

def send_order_to_web(_order_data) :

    # order_data에서 얻어진 agency_idx를 통해,agency에 소속된 manager_id를 얻어낸다

    # dynamo db에서 소속된 manager_id를 통해 접속된 sid list를 알아낸다

    # 주문 정보를 sid list로 emit 한다.
    #send_emit("order",_order_data,sid_list)
    pass

def send_order_to_mobile(_order_data):

    # 오더 정보를 기준으로 기사에게 보낼 범위를 알아낸다.
    driver_list = get_driver_list(_order_data)

    # dynamo db에서 driver sid list를 알아낸다.


    # 주문 정보를 sid list로 emit 한다.

    # send_emit("order",order_data,sid_list)
    pass

def send_emit(_event,_data,_to): # to는 idx 리스트
    for i in _to:
        socketio.emit(_event,_data, _to[i])


# order_data를 가지고
def get_driver_list(_order_data) :

    driver_list=[]

    #거리 위치 알고리즘에 의해 list를 구한다.

    return driver_list      # driver idx list