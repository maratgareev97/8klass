from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/test')
def vaso():
    a=6
    b=7
    s=a+b
    print(a+b)
    return "Привет <b>мир</b>"+str(s)+str(a)

@app.route('/variable/<vvv>---<mmm>')
def index1(vvv,mmm):
    mas=[]
    mas.append(vvv)
    mas.append(mmm)
    print(int(mas[0])+int(mas[1]))
    string=str(mas)
    return string+"   "+ str(int(mas[0])+int(mas[1]))

@app.route('/get/', methods=['GET'])
def index2():
    a=request.args.get('a')
    b=request.args.get('b')
    return a+" "+b

@app.route('/')
def index():
    a="Hello "
    b="world"
    res = requests.get("http://127.0.0.1:5000/get/?a={}&b={}".format(a,b))
    print(res.text)
    print(res)
    return "Привет" + res.text
app.run()
