import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name='First App')

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    return 'Hello' + name + '!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
