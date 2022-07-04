import socket
url = "0.tcp.ngrok.io"
ip = socket.gethostbyname(url)

print(ip)