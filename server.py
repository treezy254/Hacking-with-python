from re import T
import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    
    c.send('Thankyou for connecting'.encode())
    c.close()
    
    break