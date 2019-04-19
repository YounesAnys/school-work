import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8181))
serversocket.listen(5) # become a server socket, maximum 5 connections

decodedClientInput = ""
i = 0

while True:
    connection, address = serversocket.accept()
    clientInput = connection.recv(64)
    if len(clientInput) > 0:
        clientInput = clientInput.decode('utf_8')
        print ("Encoded string recieved by server: " + clientInput)
        break

while i < len(clientInput):
    if  (clientInput[i:(i+8)] == "000+-0-+"):
         decodedClientInput = decodedClientInput + "00000000"
         i += 8
    elif (clientInput[i:(i+8)] == "000-+0+-"):
         decodedClientInput = decodedClientInput + "00000000"
         i += 8
    elif (clientInput[i] == "0"):
        decodedClientInput = decodedClientInput + "0"
        i += 1
            
    elif (clientInput[i] == "+" or clientInput[i] == "-"):
        decodedClientInput = decodedClientInput + "1"
        i += 1
    else:
        break

print(decodedClientInput)
