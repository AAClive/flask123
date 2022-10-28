from flask import Flask, jsonify
import os
from flask import render_template
app = Flask(__name__)
import socket
x=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
x.bind(("192.168.15.180",5050))
@app.route('/')
def index():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
