from flask import Flask

app = Flask(__name__)

@app.route('/')
def vaso():
    a=6
    b=7
    s=a+b
    print(a+b)
    return "Привет <b>мир</b>"+str(s)+str(a)

@app.route('/test')
def vaso1():
    return "Тест"

app.run()
