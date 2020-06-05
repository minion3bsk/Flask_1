#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"


#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("index.html")

#/show」へアクセスがあった場合に、「show.html」を返す
@app.route("/show")
def show():
    return render_template("show.html")    


#おまじない
if __name__ == "__main__":
    app.run(debug=True)