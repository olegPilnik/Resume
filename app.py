from flask import Flask  #  import Flask

app = Flask(__name__)    #  create instance class Flask


@app.route('/')
def hello():
    return 'Hello, World'

