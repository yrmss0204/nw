# -*- coding: utf8 -*-                           #한글 주석을 달려면 맨앞에 써야함

import time 
import threading
import multiprocessing

def yes(no):
    while True:
         print"yes"
         time.sleep(0.5)

def no(no):
        while True:
             print "no"
             time.sleep(0.5)

#t1 = threading.Thread(target = yes, args =(1,))   #1번 전달함
#t2 = threading.Thread(target = yes, args =(2,))   #2번 전달함  //여기까진 실행되진 않고 등록만 한거

#t1.start()
#t2.start()                                        #여기까지가 쓰레스를 두개 동시 실행 시키는 코드


if __name__ ==' __main__':                         #파이썬 자체가 컴파일이 되지 않기 때문에 써준것,이걸 넣어주지 않으면 나는 import가 아니고 독립 실행이다 라고 인식한다.
    p1 = multiprocessing.Process(target=yes, args=(1,))
    p2 = multiprocessing.Process(target=yes, args=(2,))
    p1.start()
    p2.start()
                                                   #동기작업을 해야한다.