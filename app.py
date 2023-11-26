from flask import Flask
app = Flask(__name)

@app.route('/')
def hello_world():
  return "Hello, World!"
