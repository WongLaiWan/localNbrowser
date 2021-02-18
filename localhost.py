#First HTTP Server
import socket
#Define the host as a tuple
HOST, PORT = "", 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(True)

print("Serving HTTP on port %s...." %PORT)

while True:
    client_connection, client_address = s.accept()
    request = client_connection.recv(1024) #Buffer Size
    print(request.decode("utf-8")) #Display the HTTP request
    #Define the Web response message
    http_reponse = "HTTP/1.1 200 OK \n\n<HTML>" \
    "<body>" \
    "PI2004K Project! Welcome<3 " \
    "<p>" \
    "<img src='https://steamusercontent-a.akamaihd.net/ugc/82595628823614964/59CA60267C9EF097829F8B6CFDED0CD489F0ECCE/'" \
    "</p>" \
    "</body>" \
    "</html>"

    client_connection.sendall(bytes(http_reponse, "utf-8"))
    client_connection.close()

