from flask import session,request
from flask_socketio import emit, join_room, leave_room, Namespace
import utils.config as def_config
import boto3
import jwt
import datetime
from flask_session import Session
import json
import os
from logging import log
import utils.common_util as common_util
from utils.common_util import respond

table_name = def_config.DYNAMODB_TABLE_NAME
region_name = def_config.DYNAMODB_REGION_NAME
aws_access_key_id = def_config.DYNAMODB_ACCESS_KEY_ID
aws_secret_access_key = def_config.DYNAMODB_SECRET_ACCESS_KEY

dynamodb = boto3.resource('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
table = dynamodb.Table(table_name)

agency_id = 1111
agency_name = "너구리대리운전"
access_token = "abcd2222"
refresh_token = "efgh"


payload = {
    "agency_id": agency_id,
    "agency_name": agency_name,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # 테스트를 위해 매우 짧은 시간으로 세팅함.
}

key = def_config.JWT_SECRET_KEY
access_token = jwt.encode(payload, key, algorithm='HS256')




# Class Based Namespace
class MyServerNamespace(Namespace):     # NameSpace를 넣어준다.

    # def __init__(self, sio, namespace, *args, **kwargs):
    #     super(Namespace, self).__init__(namespace)
    #
    #     # self.sio = sio
    #     # self.logger = sio.logger

    def on_connect(self):           # 예약어
        print(str)
        print('on_connect!!')
        print("%s connected" % (request.sid))  # Namespace 방식에서 쓸때는 request.sid 형태로 써야함
        session['sid'] = request.sid
        sid=request.sid
        print('session_id: %s' % (session.get('sid')))

        # agency_id와 sid를 매핑한다.
        response = table.put_item(
            Item={
                'agency_id': agency_id,
                'access_token': access_token,
                'refresh_token': refresh_token,
                'sid': sid
            }
        )

    def on_authorize(self,data):
        print(dic_auth['JWT_TOKEN'])
        if check_auth(dic_auth['JWT_TOKEN']):
            try:
                #app.logger.info("New websocket client connected")
                emit("authorize", respond(1000, "정상", {'USER_ID': 'qwert'}))  # Type은 dict 형태이다.
                return True
            except Exception as e:
                #app.logger.info(e, "New websocket client failed to connect")
                emit("authorize", respond(1100, e, {'USER_ID': 'qwert'}))
                #disconnect()
                return False
        else:
            emit("authorize", respond(1100, "사용자 인증에 문제가 있습니다", ""))
            #app.logger.info("New websocket client failed to connect")
            #disconnect()

    def on_disconnect(self):        # 예약어
        print('on_disconnect!!')
        print("%s disconnected" % (request.sid))  # Namespace 방식에서 쓸때는 request.sid 형태로 써야함
        pass

    def on_message(self, data):             # Custom Event
        print('on_message!!!')
        print(data)
        #room = session.get('room')
        #emit('message', {'msg': session.get('name') + ':' + data['msg']}, room=room)
        print('session_id: %s' % (session.get('sid')))

    def on_joined(self, data):              # 클라이언트로부터 이벤트 joined를 받음 
        print('on_joined!!',data)
        room = session.get('room')
        join_room(room)
        emit('status', {'msg': session.get('name') + '님이 입장하셨습니다'}, room=room)

    def on_left(self, data):
        print('on_left!!!')
        room = session.get('room')
        leave_room(room)
        emit('status', {'msg': session.get('name') + '님이 퇴장하셨습니다'}, room=room)


# jwt가 유효한지 확인한다.(코딩 필요)
def check_auth(jwt_token):

    if jwt_token == "abcd1234":
        try:

            #app.logger.info("JWT is OK")
            return True
        except Exception:
            #app.logger.info("JWT Exception")
            return False
    else:
        #app.logger.info("JWT is not OK")
        return False

# 데코레이터는 사용하지 않는다.
# # 데코레이터 함수 기반 Namespace
# def socketio_init(socketio):
#
#     @socketio.on('connect')
#     def connect(auth):
#         print("connected!!")
#
#     @socketio.on('joined', namespace='/chat')
#     def joined(message):
#         room = session.get('room')
#         join_room(room)
#         emit('status', {'msg': session.get('name') + '님이 입장하셨습니다'}, room=room)
#
#
#     @socketio.on('text', namespace='/chat')
#     def text(message):
#         room = session.get('room')
#         emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
#
#
#     @socketio.on('left', namespace='/chat')
#     def left(message):
#         room = session.get('room')
#         leave_room(room)
#         emit('status', {'msg': session.get('name') + '님이 퇴장하셨습니다'}, room=room)