import zmq
import sys
import time

def SendCmdToCTP(s):
    context = zmq.Context()
    print ("Connecting to server...")
    socket = context.socket(zmq.REQ)
    socket.connect ("tcp://localhost:5555")
    socket.send_string(s)
    print ("done send command :", s)
    message = socket.recv()
    print(message)


#context = zmq.Context(1)
#socket = context.socket(zmq.REP)
#socket.bind("tcp://*:5556")

#while True:
    #  Wait for next request from client
#    message = socket.recv()
#    print("Received request: ", message)
#    time.sleep (1)  
#    socket.send("World from ")



#StartBuy("rb buy 3600")

#CloseBuy("rb closebuy 3580")



#  Do 10 requests, waiting each time for a response
#for request in range (10):
#socket.send_string("rb buy 3670")
#print ("done send msg")
    #  Get the reply.
#message = socket.recv()
#print(message)
    #print ("Received reply ", request, "[", message, "]")
