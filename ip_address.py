import socket

hostname = socket.gethostname()

IPaddr = socket.gethostbyname_ex(hostname)
IIPaddr = socket.gethostbyname(hostname)

print(IPaddr)
print(IIPaddr)
