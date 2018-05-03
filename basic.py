# -*- coding: utf8 -*-
# 문자 출력
print "python"

#변수 선언
msg = "hello python"
print msg
# 문자열 슬라이싱
print msg[1:3]
print msg[-3:]
print msg[:-2]
print msg[::-1]

#리스트
data = []
#리스트 자료 입력
data.append("hi")
data.append(123)
data.append(1.2)
#리스트 출력
print data
#리스트 데이터 제거
data.pop()
print data
data.pop()
print data
#리스트 요소 인덱스 검색
print data.index("hi")
#index 메소드 실패 시 에러 발생
#print data.index("hi222")

#사전(딕셔너리)
#{키 : 값}
#me가 키, you가 값
user ={}
user['me'] ={'age': 30, 'address':'daejoen'}
user['you'] ={'age': 22, 'address':'seoul'}
# 사전 출력
print user 
#사전 데이터 검색 키 활용
print user['me']
print"user keys:", user.keys()
print "me" in user.keys()

#제어
# if, if else, if elif else
num =4
if num >0:
    print "num > 0"

if num > 5:
    print "num < 5"
else:
    print "num < 5"

if num % 2 == 0:
    print "even"
elif num % 2 == 1:
    print "odd"
else:
    print "????"    

#함수
def addition(numbers):
    result = () #이 안에서만 참조하고 값을 갖어올수 있다, 밖엔선 갖어올수 없다.
    for number in numbers:
        result += number
    return result

    #data = [1,2,3]
    #print addition(data)



def help():
      print "id ---------print user id"
      print "pwd --------print ip adress"
      print "quit ------exit program"
        
help()   





#라이브러리 불러오기
import os
import platform
import subprocess
#무한 루프 (자주쓰는 패턴)
#while True:
#    cmd = raw_input()
#    if cmd == 'id':
#       if platform.system() == 'Windows':
#           print os.environ.get('USERNAME')
#       else:
#           print os.getenv('USER')  
#   elif cmd =='pwd':
#        print os.getcwd()
#   elif cmd == 'quit': #끝내려고 quit 쓴거다
#       print "bye~"
#       pass
#       break
#   elif cmd == 'ip':
#       if platform.system() == 'Windows':
#           buf = subprocess.check_output('ipconfig')
#           index = buf.find("IPv4")
#           newline = buf[index:].find("\n")
           #print index, newline
#           ipline = buf[index:index+newline]#시작 위치부터 얼마나 더 읽을꺼냐 라는 뜻
#           ip = ipline.split(':')
#           print ip[1].strip()#공백 불필효한 공백을 없에는것
#       else:
#           buf = subprocess.check_output('ifconfig')
#           target ='addr:'
#           index = buf.find(target) + len(target)
#           space = buf[index:].find('  ')
#           print index, space
#           print buf[index:index +space]

#   else:
#       help()


# urlib2 사용
import urllib2
import re
urllib2url = 'https://box.cdpython.com/ezen/'
req =urllib2.Request(urllib2)
res = urllib2.urlopen(req)
html = res.read()
#print html
#re 모듈(정규표현식)을 사용한 패턴 매칭
#파이썬에서만 제공하는 문자
ipaddress, port = re.findall(r"\d+\.\d+\.\d+\.\d+\/\d+",html)[0].split('/')
print "ip",ipaddress, "port",port