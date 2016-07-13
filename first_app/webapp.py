from flask import Flask, render_template

webapp = Flask(__name__)

@webapp.route('/')
def hello_world():
    return 'First App'

if __name__ == '__main__':
    webapp.run(host='0.0.0.0')
