from flask import Flask
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '나는 나는 나는  정말로 정말로  집으로 집으로 집으로 집으로 가고 싶습니다.'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)
    return result

