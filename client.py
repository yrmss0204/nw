# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩
import socket
#접속 서버 정보
info = ("127.0.0.1",9999)
#TCP 소켓 생성
s = socket.socket()
#서버 접속
s.connect(info) #9999가 info에 저장되서 접속
#데이터 전송
s.send("hello server\n")
#데이터 수신 및 출력
print s.recv(1024) #수신
#접속 종료
s.close()