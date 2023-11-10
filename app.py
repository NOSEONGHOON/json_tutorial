
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '안녕? 반가워! 내 이름은 노성훈이야!!'

