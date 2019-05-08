import zmq
import sys
import time


context = zmq.Context(1)
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    message = socket.recv()
    print("Received request: ", message)
    time.sleep (1)  
    socket.send_string("World from ")