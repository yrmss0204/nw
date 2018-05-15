# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩
import socket
import threading

def handler(conn, address):
    while True :                                      #여러 사용자를 동시에 돌아가면서 처리할수 있도록 쓰레드를 씀
        try:
        #클라이언트가 전송한 데이터 수신                 #accept=필요한 배인지 구분. 근데 우선 다 받아드림
            data =conn.recv(1024)                     #클라이언트가 소켓을 갖고 있다
        except:
            print"Excetion!!"
            if not data:
            #데이터를 보내지 않은 클라이언트 연결 종료
                conn.close()
                break
                                                      #소켓 오브젝트= 이 배를 보낼지 들일지
        print"address %s send data %s" % \
        ( address[0], data)
                                                      #서버는 클라이먼트를 하나만 받아드리는 것이 아니다.여려명 받는다.
        #수신 데이터를 클라이언트에 전송
        conn.send(data)                               #cmd에서 python server.py를 키고 새창 열어 python client.py를 열라
#서버 정보
info =("0.0.0.0",9999)
#소켓 생성
s = socket.socket()
#9999번 포트 바인딩
s.bind(info)
#바인딩 포트 리스닝
s.listen(5)  #한 5개 정도 지켜볼께 라는 뜻                
                              #서버는 마냥 기다린다 항상(나한테 올때까지).
                              #서버란 먼가를 제공한다는 뜻이니까.
                              #서버는 켜있는데 바인드가 없음 서버에 접근 불가.
                              #서버는 딱히 기능은 없어도, 켜노면 필요할때 일을 잘 해준다.
                              #IP(만같은 존재)랑 포드(항구같은 존제)
                              #바인드는 항구를 만들고 항구의 문을 열어주는 역활
                              #9999=수만은 항구중에 하나 항구의 번호
                              #listen= 항구에 뭐가 오면 (송신,수신되는걸) 지켜본다.
while True :
    #접속요청 승인                                     
    (conn,address) = s.accept()                       #accept가 되면 쓰레드(thread)를 기다린다,뭐가 들어오면 쓰레드를 또 만든다
    print "[+] new connection from %s(%d)" % (address[0],address[1])
    th = threading.Thread(target=handler, args=(conn,address))
    th.start()                                        #여기까지가 멀티싱 기반에 PCP 소켓 쓰레딩 코드