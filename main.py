from flask import Flask, jsonify
import os
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
