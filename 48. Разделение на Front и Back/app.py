from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    f = open('goods.txt', 'r+', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)

@app.route('/add/', methods=["post"])
def add():
    good = request.form["good"]
    f = open('goods.txt', 'a+', encoding='utf-8')
    f.write(good+"\n")
    f.close()
    return """
        <h1>Инвентар пополнен</h1>
        <a href="/">Home</a>
    """

if __name__ == '__main__':
    app.debug = True
    app.run()