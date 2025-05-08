from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from flask_cors import CORS

app =Flask(__name__)
CORS(app)
socket =SocketIO(app,cors_allowed_origins='*')
dots =[]
@app.route('/')
def index():
    return render_template('index.html')
@socket.on('draw')
def draw(coord):
    print(coord)
    dots.append(coord)
@socket.on('getdraw')
def get():
    emit('dots',dots)
if __name__ =="__main__":
    socket.run(app,debug=True,allow_unsafe_werkzeug=True)