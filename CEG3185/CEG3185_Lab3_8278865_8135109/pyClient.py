# pyClient.py by Samantha Glavine and Mahyar Gorji


#Imports
import socket

#Globals

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8181))

userInput = input("Please enter a string of 0s and 1s to be encoded:")
userInput = str(userInput)

currentVoltage = -1 #starts positive
serverInputFromClient = ""
i = 0;

while i < len(userInput):
        if (userInput[i] == "0"):
                if (userInput[i:(i+8)] == "00000000"):
                        if (currentVoltage == 1):
                                serverInputFromClient = serverInputFromClient + "000+-0-+"
                                i += 8 #skips ahead required number of indices

                        elif (currentVoltage == -1):
                                serverInputFromClient = serverInputFromClient + "000-+0+-"
                                i += 8 #skips ahead required number of indices

                        else:
                                raise ValueError("currentVoltage can only be 1 or -1")
                else:
                        serverInputFromClient = serverInputFromClient + "0"
                        i +=1
        elif (userInput[i]=="1"):
                if(currentVoltage==1):
                        serverInputFromClient = serverInputFromClient + "-"
                        currentVoltage=-1
                        i +=1
                elif(currentVoltage==-1):
                        serverInputFromClient = serverInputFromClient + "+"
                        currentVoltage=1
                        i +=1
        else:
                 break
	#if (userInput[i+1]==None):
		#break
print("Encoded string of user input: " + serverInputFromClient)

clientsocket.send(serverInputFromClient.encode('utf-8'))
