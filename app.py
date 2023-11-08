from flask import Flask, render_template,session,request
from flask_socketio import SocketIO, emit,send

from api.routes import main as main_blueprint
from api.events import ChatNamespace
from api.events import socketio_init

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
#app.config['DEBUG'] = True
socketio = SocketIO(app)

#app.register_blueprint(main_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    print("connected")

    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)

#
# #socketio.on_namespace(ChatNamespace('/chat'))       # 이벤트 등록하기(namespace handler)
# #socketio_init(socketio)
#
# @socketio.on('connect')
# def connect(auth):
#     print('Client connected')
#     #emit('my response', {'data': 'Connected'})
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
#
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')
#
#
# if __name__ == '__main__':
#     socketio.run(app)
#
#


# def socketio_init(socketio):
#     @socketio.on('testSocket',namespace='/test')
#     def testEvent(message):
#         tsession = session.get('test')
#         print('received message'+str(message))
#         retMessage = { 'msg' : "hello response" }
#         emit('test',retMessage,callback=tsession)
#
#     @socketio.on('connect')
#     def test_connect(auth):
#         print('Client connected')
#         emit('my response', {'data': 'Connected'})
#
#     @socketio.on('disconnect')
#     def test_disconnect():
#         print('Client disconnected')
#
# @app.route('/chat')
# def chatting():
#     return render_template('chat.html')
#
# @socketio.event
# def my_event(message):
#     emit('my response', {'data': 'got it!'})
#
#
# @socketio.on("message")
# def request(message):
#     print("message : " + message)
#     to_client = dict()
#     if message == 'new_connect':
#         to_client['message'] = "welcome tester"
#         to_client['type'] = 'connect'
#     else:
#         to_client['message'] = message
#         to_client['type'] = 'normal'
#     socketio.send(to_client, broadcast = True)


