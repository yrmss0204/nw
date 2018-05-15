# -*- coding: utf8 -*-
#import flask로 해버리면 삼만몇천개가 다 로딩된다
from flask import Flask, render_template, request #이렇게 쓰면 삼만몇천개 중에서 하나만 작동한다. 효율적이다.경제적이다.
import hashlib

app = Flask(__name__) #flask에 name이 인자에 들어가고. app이 반환값
users = {}            #딕셔너리

@app.route("/")    #@이가 붙어있음 /아무 주소도 쓰지않고 나한테 접근한 상태(예: naver만 쳤을때)
def hello():       #/에 접근하면 hello가 작동한다.
    return render_template("login.html")

@app.route("/name")  #주소창에 flask run을 쳐서 나오는 주소+/name을 쳤을때 작동http://127.0.0.1:5000/name
def name():
    return"taeyun"

@app.route("/login", methods=['GET','POST'])
def login():
    id +request.form['id']
    pw =request.form[ 'pw']
    if id in users:
        if users[id] == hashlib.sha1(pw).hexdigest():
           return "login ok"
        else:
           return "login fail"
    else:
        return "login fail"


@app.route("/join",methods=['GET','POST'])  #http://.../join으로 들어가면 GET으로 나오고
def join():                                 #......:5000/으로 들어가서 입력하고 join눌르면 POST!가 뜬다
    if request.method == 'POST':            #request는 클라이언트껄 요청을 처리해준다 
        id =request.form['id']              #form은 아이디랑 비번치는 곳
        pw = request.form['pw']              
        if id not in users :                #id값은 host안에서 갖어왔다
            users[id] = hashlib.sha1(pw).hexdigest()   #pw를 그냥 두지 않고 hecdigest화해서 너놓는거
        else:
            return "duplicate!!"
        return "join ok!"
    return render_template("join.html")

@app.route("/add") #이줄부터 및 3줄까지 꾀 자주 쓰인다
@app.route("/add/<int:num1>")
@app.route("/add/<int:num1>/<int:num2>")
def add(num1=None, num2=None):  #사용자가 잘못 입력했을때를 대비해 맞게 입력하는 법을 알려주는것.예외처리
    if num1 is None or num2 is None:
        return "/add/num1/num2"
    return str(num1 + num2) #str문자열로 바꿔주는것 .바꿔줘야한다. flask경우



