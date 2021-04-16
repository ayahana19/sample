# -*- coding: utf-8 -*-
# https://aiacademy.jp/media/?p=57 Python】Flaskとは？FlaskでWeb開発の基礎を学ぼう！


# Flaskの簡単な使い方 https://qiita.com/zaburo/items/5091041a5afb2a7dffc8

# 麻雀アプリで使うflask https://qiita.com/kph7mgb/items/cd7bdcc0fbc58e31ffb6

# flaskのディレクトリがあるフォルダに置かないとダメ！！！
# ファイルを実行する前に、コマンドプロンプトのカレントディレクトリをcd flask を入力して変更しておく
# あとは、mahjang.pyを実行してから、下記のアドレスにアクセスするとwebファイルが出来ている

# ファイルを実行してから、http://localhost:8080/  にアクセスするとweb上で表示される
# コマンドプロンプトにアクセスすべきアドが表示される > http://127.0.0.1:8080/ ので、そこへ行くと、14枚の配牌が
# ランダムに表示される。だだし、配牌画像ファイルをC:\Users\Rosa\flask\static\pic に置かないとダメ




from flask import Flask
import random

app = Flask(__name__)


# 麻雀牌のクラス
class Tile:
    def __init__(self, kind, value, pic):
        self.kind = kind  # 麻雀牌の種類（萬子・筒子・索子・四風牌・三元牌）
        self.value = value  # 麻雀牌の値（1~9 東南西北白発中）
        self.pic = pic  #画像ファイル名

    def create_img_tag(self):
        return f'<img src=/static/pic/{self.pic}>'

#山牌
yamahai = [
          Tile('manzu', '1', 'manzu_1.png')
        , Tile('manzu', '1', 'manzu_1.png')
        , Tile('manzu', '1', 'manzu_1.png')
        , Tile('manzu', '1', 'manzu_1.png')
        , Tile('manzu', '2', 'manzu_2.png')
        , Tile('manzu', '2', 'manzu_2.png')
        , Tile('manzu', '2', 'manzu_2.png')
        , Tile('manzu', '2', 'manzu_2.png')
        , Tile('manzu', '3', 'manzu_3.png')
        , Tile('manzu', '3', 'manzu_3.png')
        , Tile('manzu', '3', 'manzu_3.png')
        , Tile('manzu', '3', 'manzu_3.png')
        , Tile('manzu', '4', 'manzu_4.png')
        , Tile('manzu', '4', 'manzu_4.png')
        , Tile('manzu', '4', 'manzu_4.png')
        , Tile('manzu', '4', 'manzu_4.png')
        , Tile('manzu', '5', 'manzu_5.png')
        , Tile('manzu', '5', 'manzu_5.png')
        , Tile('manzu', '5', 'manzu_5_dra.png') #萬子の五の赤ドラ
        , Tile('manzu', '5', 'manzu_5.png')
        , Tile('manzu', '6', 'manzu_6.png')
        , Tile('manzu', '6', 'manzu_6.png')
        , Tile('manzu', '6', 'manzu_6.png')
        , Tile('manzu', '6', 'manzu_6.png')
        , Tile('manzu', '7', 'manzu_7.png')
        , Tile('manzu', '7', 'manzu_7.png')
        , Tile('manzu', '7', 'manzu_7.png')
        , Tile('manzu', '7', 'manzu_7.png')
        , Tile('manzu', '8', 'manzu_8.png')
        , Tile('manzu', '8', 'manzu_8.png')
        , Tile('manzu', '8', 'manzu_8.png')
        , Tile('manzu', '8', 'manzu_8.png')
        , Tile('manzu', '9', 'manzu_9.png')
        , Tile('manzu', '9', 'manzu_9.png')
        , Tile('manzu', '9', 'manzu_9.png')
        , Tile('manzu', '9', 'manzu_9.png')
        , Tile('pinzu', '1', 'pinzu_1.png')
        , Tile('pinzu', '1', 'pinzu_1.png')
        , Tile('pinzu', '1', 'pinzu_1.png')
        , Tile('pinzu', '1', 'pinzu_1.png')
        , Tile('pinzu', '2', 'pinzu_2.png')
        , Tile('pinzu', '2', 'pinzu_2.png')
        , Tile('pinzu', '2', 'pinzu_2.png')
        , Tile('pinzu', '2', 'pinzu_2.png')
        , Tile('pinzu', '3', 'pinzu_3.png')
        , Tile('pinzu', '3', 'pinzu_3.png')
        , Tile('pinzu', '3', 'pinzu_3.png')
        , Tile('pinzu', '3', 'pinzu_3.png')
        , Tile('pinzu', '4', 'pinzu_4.png')
        , Tile('pinzu', '4', 'pinzu_4.png')
        , Tile('pinzu', '4', 'pinzu_4.png')
        , Tile('pinzu', '4', 'pinzu_4.png')
        , Tile('pinzu', '5', 'pinzu_5.png')
        , Tile('pinzu', '5', 'pinzu_5_dra.png') #筒子の5の赤ドラ
        , Tile('pinzu', '5', 'pinzu_5.png')
        , Tile('pinzu', '5', 'pinzu_5.png')
        , Tile('pinzu', '6', 'pinzu_6.png')
        , Tile('pinzu', '6', 'pinzu_6.png')
        , Tile('pinzu', '6', 'pinzu_6.png')
        , Tile('pinzu', '6', 'pinzu_6.png')
        , Tile('pinzu', '7', 'pinzu_7.png')
        , Tile('pinzu', '7', 'pinzu_7.png')
        , Tile('pinzu', '7', 'pinzu_7.png')
        , Tile('pinzu', '7', 'pinzu_7.png')
        , Tile('pinzu', '8', 'pinzu_8.png')
        , Tile('pinzu', '8', 'pinzu_8.png')
        , Tile('pinzu', '8', 'pinzu_8.png')
        , Tile('pinzu', '8', 'pinzu_8.png')
        , Tile('pinzu', '9', 'pinzu_9.png')
        , Tile('pinzu', '9', 'pinzu_9.png')
        , Tile('pinzu', '9', 'pinzu_9.png')
        , Tile('pinzu', '9', 'pinzu_9.png')
        , Tile('souzu', '1', 'souzu_1.png')
        , Tile('souzu', '1', 'souzu_1.png')
        , Tile('souzu', '1', 'souzu_1.png')
        , Tile('souzu', '1', 'souzu_1.png')
        , Tile('souzu', '2', 'souzu_2.png')
        , Tile('souzu', '2', 'souzu_2.png')
        , Tile('souzu', '2', 'souzu_2.png')
        , Tile('souzu', '2', 'souzu_2.png')
        , Tile('souzu', '3', 'souzu_3.png')
        , Tile('souzu', '3', 'souzu_3.png')
        , Tile('souzu', '3', 'souzu_3.png')
        , Tile('souzu', '3', 'souzu_3.png')
        , Tile('souzu', '4', 'souzu_4.png')
        , Tile('souzu', '4', 'souzu_4.png')
        , Tile('souzu', '4', 'souzu_4.png')
        , Tile('souzu', '4', 'souzu_4.png')
        , Tile('souzu', '5', 'souzu_5.png')
        , Tile('souzu', '5', 'souzu_5.png')
        , Tile('souzu', '5', 'souzu_5.png')
        , Tile('souzu', '5', 'souzu_5_dra.png') #索子の5の赤ドラ
        , Tile('souzu', '6', 'souzu_6.png')
        , Tile('souzu', '6', 'souzu_6.png')
        , Tile('souzu', '6', 'souzu_6.png')
        , Tile('souzu', '6', 'souzu_6.png')
        , Tile('souzu', '7', 'souzu_7.png')
        , Tile('souzu', '7', 'souzu_7.png')
        , Tile('souzu', '7', 'souzu_7.png')
        , Tile('souzu', '7', 'souzu_7.png')
        , Tile('souzu', '8', 'souzu_8.png')
        , Tile('souzu', '8', 'souzu_8.png')
        , Tile('souzu', '8', 'souzu_8.png')
        , Tile('souzu', '8', 'souzu_8.png')
        , Tile('souzu', '9', 'souzu_9.png')
        , Tile('souzu', '9', 'souzu_9.png')
        , Tile('souzu', '9', 'souzu_9.png')
        , Tile('souzu', '9', 'souzu_9.png')
        , Tile('sufonpai', '1', 'sufonpai_1.png') # 風牌の東
        , Tile('sufonpai', '1', 'sufonpai_1.png') 
        , Tile('sufonpai', '1', 'sufonpai_1.png') 
        , Tile('sufonpai', '1', 'sufonpai_1.png') 
        , Tile('sufonpai', '2', 'sufonpai_2.png') # 風牌の南
        , Tile('sufonpai', '2', 'sufonpai_2.png')
        , Tile('sufonpai', '2', 'sufonpai_2.png')
        , Tile('sufonpai', '2', 'sufonpai_2.png')
        , Tile('sufonpai', '3', 'sufonpai_3.png')
        , Tile('sufonpai', '3', 'sufonpai_3.png') # 風牌の西
        , Tile('sufonpai', '3', 'sufonpai_3.png')
        , Tile('sufonpai', '3', 'sufonpai_3.png')
        , Tile('sufonpai', '4', 'sufonpai_4.png') # 風牌の北
        , Tile('sufonpai', '4', 'sufonpai_4.png')
        , Tile('sufonpai', '4', 'sufonpai_4.png')
        , Tile('sufonpai', '4', 'sufonpai_4.png')
        , Tile('sangenpai', '1', 'sangenpai_1.png') # 三元牌の白
        , Tile('sangenpai', '1', 'sangenpai_1.png')
        , Tile('sangenpai', '1', 'sangenpai_1.png')
        , Tile('sangenpai', '1', 'sangenpai_1.png')
        , Tile('sangenpai', '2', 'sangenpai_2.png') # 三元牌の發
        , Tile('sangenpai', '2', 'sangenpai_2.png')
        , Tile('sangenpai', '2', 'sangenpai_2.png')
        , Tile('sangenpai', '2', 'sangenpai_2.png')
        , Tile('sangenpai', '3', 'sangenpai_3.png') # 三元牌の中
        , Tile('sangenpai', '3', 'sangenpai_3.png')
        , Tile('sangenpai', '3', 'sangenpai_3.png')
        , Tile('sangenpai', '3', 'sangenpai_3.png')
    ]
random.shuffle(yamahai)

@app.route('/')
def main():

    img_tags = ''
    for i in range(14):
        tile = yamahai.pop(0)  #山牌から一つ取り出す
        img_tags = img_tags + tile.create_img_tag()#画像出力用のHTMLタグ作成

    return img_tags


if __name__ == '__main__': # https://aiacademy.jp/media/?p=57
    #app.run(port=12345)
    app.run(port=8080)