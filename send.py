import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x=0
server_address = ('10.78.18.43', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
while x==0:
    #sock.connect(server_address)
    sock.send('field0')
    test = open('test.txt','a+')
    field0 = sock.recv(16)
    test.write('%s\n' % field0)
    print >>sys.stderr, 'received "%s"' % field0
    time.sleep(600)

