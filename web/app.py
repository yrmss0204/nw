# -*- coding: utf8 -*-
#g를 쓰면 별도로 할필요 없음. 
#redirect 로그인이 됬는지 않됬는지 돌려보내는 역활. 
#session을 사용해 로그인을 유지시켰다.

#escape는 화면에 출력할때, 보안적으로, 예를 들어 id를 이상한 코드처럼 가입을 했다면
# 싸이트의 취약점을 잡기 위해 그 코드가 실행될수 있겠끔 한것.
# 즉 id가 id로만 쓰이는 것만 아니라, 그 코드가 실행될수 있기 때문에 그런 행위를 예방하는 것이다.

#hash이걸로 비밀번호를 만들으면 안전하다. 다른 값을 입력하면 다른 데이터로 생각하기에 다릇게 실행된다.
#무결성을 검증할때 사용 곧 데이터의 정확성과 일관성을 유지하고 보증하는 기능이 있어서 보안에 좋음. 
#왜냐면 Hash는 한비트만 바뀌어도 달라진다. 데이터를 변조했다 확인하는 방법이 되는 것.
#이미 검증된 알고리즘의 hash로 길이가 길면 길수록 보안에 좋다.

from flask import Flask, render_template, request, g, redirect, session, escape 
import hashlib
import sqlite3

DATABASE = 'database.db'                    #파일명을 적어줌

app = Flask(__name__)                       #app이라는 이름으로 flask에 접근.
app.secret_key = 'f9788743275934yrsdkhfkh'  #데이터를 암호화를 하기위해 키를 넣었다.키가 있어야 암호화 할수있다.
                                            #안그럼incoding이 된다.
                                            #부호화(符號化)나 인코딩(encoding)은 정보의 형태나 형식을 변환하는 처리나 처리 방식이다.
                                            #문자 인코딩(文字-, 영어: character encoding)은 문자들의 집합을 부호화하는 방법이다.
      





def get_db():                                       #데이터베이스를 갖어오는 애 
    db = getattr(g, '_database', None) 
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)#g._database로 이름을 정하고 connection(데이터베이스에 접속(곧 웹서버개발))을 맷다
                                                    # 이 모든걸db로 짧게 이름을 지음
                                                    #connection은 느린 효과가 있다. 사용자가 많아지면 이걸 잘 관리할수 있는 법을 알아보라.
    return db 






@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database',None)
    if db is not None:
        db.close()




def query_db(query, args=(), one=False, modify=False):  #query는 select만 설정이 되있다.
                                                        #로그인은 데이터를 추가 하는 것이기 때문에 commit을 해야함.
    cur = get_db().execute(query, args)                 #먼가를 실행하는데, query를 보냄. 그래서 결과물을 가져옴.
    if modify:
        try:
            get_db().commit()                           #commit을 잘 하면 true를 반환, 아니면false를 반환
            cur.close()
        except:
            return False
        return True
    rv = cur.fetchall()                                 #fetchall는 먼가를 가져오는 애. 갖어온 데이터를 그냥 돌려주는 것. 그냥 돌려줄수 있고, 하나만 돌려줄 수 있음. 
                                                        #여러개 데이터를 갖어올때는 두가지 상황이 다 필료함.반복문을 통해서 갖어옴.
                                                        #근데 갖어올때 끊어서 갖어오는게 좋다.(100개면 100개),안 그럼 DB에서 데이터 갖아오는 속도가 느려져서 페이지 이동이 느림.
    cur.close()
    return (rv[0] if rv else None) if one else rv       #두번째if기준에서 one이 있음 앞에를 실행, 근데 







@app.route("/logout", methods=['GET','POST'])
def logout():
    session.pop('id',None)                              #id를 pop, 뺀 다는 뜻
    return redirect('/login')







@app.route("/")                                         #"/"은 index라고 읽음.
def hello():
    if 'id' in session :                                #이곳에 들어오면 로그인 페이지로 들어갈수 있음.
        return u'Logged is as 로그인됨 %s <a href="/logout">logout</a>' % escape(session['id'])       
    return render_template("login.html")







@app.route("/name")  
def name():
    return"sangrim"
    







@app.route("/login", methods=['GET','POST'])                                     
def login():
    if request.method == 'POST':                                                 #post로 사용자를 전송
        id = request.form['id'].strip()
        pw = hashlib.sha1(request.form['pw'].strip()).hexdigest()                #비번을 hesh로 바꿔서 pw에 저장
        sql = "select * from user where id= '%s' and password='%s'" % (id,pw)    #정상인지 아닌지 sql로 동작
        if query_db(sql, one=True):                                                 #존재를 하는지 않하는지 query에 보냄
            #로그인이 성공한 경우
            session['id'] = id                                                   #로그인이 성공하면 아이디를 세션에 저장
            return redirect("/")
        else:
            #로그인이 실패한 경우
            return "<script>alert('login fail');history.back(-1);</script>"     #실패면 뒷페이지 곧 로그인페이지로 돌아감
    if 'id' in session:                                                         #로그인이 잘된 경우, index로 보냄
        return redirect("/")

    return render_template("login.html")










@app.route("/join",methods=['GET','POST'])  
def join():                                 
    if request.method == 'POST':             
        id =request.form['id'].strip()             
        pw = hashlib.sha1(request.form['pw'].strip()).hexdigest()

        sql= "select * from user where id='%s'" % id # 이 3줄은 중복 가입을 막는 법 #이 id가 이미 존재하는지 검증하는 것
        if query_db(sql, one=True):                     #이미 되어있음 query에 보내고 ,
            return "<script>alert('join fail');history.back(-1);</script>" #뒤 화면으로 돌려보냄

        sql = "insert into user(id, password) values('%s','%s')" % (id, pw)
        query_db(sql, modify=True)              
        return redirect("/login")

    if 'id' in session:
        return redirect("/")

    return render_template("join.html")





