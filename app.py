from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello flask & code deploy v2'


if __name__ == '__main__':
    app.run()
