# -*- coding: utf-8 -*-
# https://aiacademy.jp/media/?p=57 Python】Flaskとは？FlaskでWeb開発の基礎を学ぼう！
from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')
 
#app.run(port=12345, debug=True)
app.run(port=12345, debug=True)