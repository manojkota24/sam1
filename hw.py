from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return 'hello this is manoj'
app.run(host='127.0.0.1',port=8080,debug=True)
