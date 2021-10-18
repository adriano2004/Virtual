from flask import Flask, render_template

app = Flask(__name__, template_folder='./template')


@app.route('/pag2.html')
def raiz():
    return render_template('pag2.html')

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/')
def status():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
