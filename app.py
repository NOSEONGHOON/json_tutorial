from flask import Flask, render_template, request, Response
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '나는 나는 나는  정말로 정말로  집으로 집으로 집으로 집으로 가고 싶습니다.'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)
    return result

@app.get('/count/')
def count():
    return render_template('count.html')

@app.post('/result/')
def result():
    user_input = request.form['userinput']
    word_dict = dict(Counter(user_input.split()))
    result = json.dumps(word_dict)
    return Response(result,
                    mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=count.json'})
