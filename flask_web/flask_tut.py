from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!!!"

@app.route('/krishna')
def krishna():
    return "Hello, krishna"
app.run()


