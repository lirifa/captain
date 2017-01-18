#!/usr/bin/python
# coding:utf-8

import os
import sys
import time 
import socket

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def checkport(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print '\033[1;32mCAPTAIN >>> %d is start\033[0m' % port
        return True
    except:
        print '\033[1;31mCAPTAIN >>> %d is stop\033[0m' % port
        return False
def usage():
    print "\033[1;33mUsage: %s {start|stop|status}\033[0m" %sys.argv[0]

if __name__ == "__main__":
    prodir = cur_file_dir()
    os.chdir(prodir)
    try:
        way = sys.argv[1]
        if way == "start":
            print "\033[5;1;36mCAPTAIN >>> service starting...\033[0m"
            os.system("nohup python manage.py runserver 0.0.0.0:1226 >> nohup.out 2>&1 &")
            time.sleep(3)
            checkport("172.24.55.1",1226)
        elif way == "stop":
            print "\033[5;1;36mCAPTAIN >>> service stoping...\033[0m"
            os.system("kill -9 `ps -ef | grep manage.py | awk '{print $2}'`")
            time.sleep(3)
            checkport("172.24.55.1",1226)
        elif way == "status":
            print "\033[5;1;36mCAPTAIN >>> checking  service status...\033[0m"
            checkport("172.24.55.1",1226)
        else:
            usage()
    except:
        usage()
