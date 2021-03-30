from flask import Flask, render_template,url_for,request,flash


app = Flask(__name__)

@app.route("/")
def top():
    return render_template(("index.html"))

@app.route("/hankei")
def hankei():
    return render_template("hankei.html")

@app.route("/kekka",methods=['POST'])
def kekka():
    hankei=request.form.get("hankei")
    ensyu=(int(hankei)+int(hankei)) * 3.14
    menseki=(int(hankei)*int(hankei)) * 3.14

    return render_template("kekka.html",ensyu=ensyu,menseki=menseki)

@app.route("/kyuuryou")
def kyuuryou():
    return render_template("kyuuryou.html")

@app.route("/result",methods=['POST'])
def result():
    kyuuryou=request.form.get("kyuuryou")
    time=request.form.get("time")
    kyuuryou2=int(kyuuryou)*int(time)
    return render_template("result.html",kyuuryou=kyuuryou2)


if __name__ == "__main__":
    app.run(debug=True)