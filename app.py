from flask import Flask, render_template,url_for,request,flash


app = Flask(__name__)

@app.route("/")
def top():
    return render_template(("index.html"))

@app.route("/hankei")
def hankei():
    return render_template("hankei.html")

@app.route("/kekka" methods=['POST'])
def kekka():
    hankei=repuest.form.get("hankei")
    ensyu=(haneki+hankei) * 3.14
    menseki=(hankei*hankei) * 3.14

    return render_template("kekka.html",ensyu=ensyu,menseki=menseki)


if __name__ == "__main__":
    app.run(debug=True)