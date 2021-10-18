from flask import Flask

app = Flask(__name__)


@app.route('/home')
def raiz():
    return '<h1>1º Página</h1>'


@app.route('/status')
def status():
    return '<h2>2º Página</h2>'


app.run()
