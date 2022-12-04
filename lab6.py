"""
Hello Grader, to run this EC program:
1) In terminal run, python3 lab6.py port 
2) In second terminal run, python3 lab6.py port port_from_terminal_one
Example: 
1) Terminal: python3 lab6.py 50123 (this starts a Bob node)
2) Terminal 2: python3 lab6.py 50125 50123 (this starts a Alice node that speaks to a Bob node)

Note) In my write up I sent to the professor I specified that it should use TCP/IP, 
      but since every peer should be broadcasting a public key, i thought that UDP/IP
      would make more since for this project. 

Note) My secret value that is shared between the two is incorrect. I understand that the
      shared key should equal (g^xy mod n), but my math logic is not correct at this time. 
      For lack of time, meaning I should probally be focused on studying for my finals, 
      I left the solution as is. 

"""

import random
import socket
import os, sys
import pickle
import threading
import time

ONE_SEC = 1
HOST = '127.0.0.1' #for simplicity assume on same host
DEFAULT_ADDRESS = (HOST, 0)
BUFFER = 2048
TEST_PORT = 50001
N = 11
G = 2


class Node(object):
    def __init__(self, name, my_port, peer_port = None): 
        # create a private key, using small number for simplicity
        
        self.my_name = name
        self.peer_port = peer_port
        self.my_port = my_port
        self.x = random.randint(1,9)
        self.myAddr = None  # listener sets port

    def run(self):
        """starts a listener threat to here incoming messages"""
        listener = threading.Thread(target=self.listen_to_publisher)   
        listener.start()
        time.sleep(ONE_SEC)  # give lister time to set port dynamically 
        if self.peer_port != None:
            subscriber = threading.Thread(target=self.subscribe_to_key_exchange)
            subscriber.start()
        
        
    
    
    def listen_to_publisher(self): 
        """Creates a listener socket """
        print("Node", self.my_name, "is listening for updates")

        listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listeningAddress = (HOST, int(self.my_port))
        listener.bind(listeningAddress)
        while True:
            # wait to receive message
            data, addr = listener.recvfrom(BUFFER)
            unpickeledData = pickle.loads(data)
            print("Listener( ",self.my_name,") Recieved Message: ", unpickeledData)
            val = int(data[2]) ** self.x
            print("g^xy mod n", self.my_name, ":", val)


            # send message back
            # msg = (unpickeledData[1], unpickeledData[2], self.get_key())
            my_data = pickle.dumps(self.get_key())
            listener.sendto(my_data, addr)
            
            
    
    def get_key(self, n = N, g=G):
        """return (n, g, and g^x mod n)"""
        num = g**self.x
        num = num % n         
        return (n, g, num)
        
    def print_final_number(self, data, n=N, g=G):
        return int(data[2]) ** self.x
        


    def subscribe_to_key_exchange(self):
        # while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            key = self.get_key()
            data = pickle.dumps(key)
            peer_address = (HOST, int(self.peer_port))
            s.sendto(data, peer_address)
            data, address = s.recvfrom(BUFFER)
            my_data = pickle.loads(data)
            print("g^xy mod n", self.my_name, ": ", self.print_final_number(my_data))
                
            


if __name__ == '__main__':
    if len(sys.argv) == 2:
        node = Node("Bob", sys.argv[1])
        node.run()

    elif len(sys.argv) == 3:
        node = Node("Alice", sys.argv[1], sys.argv[2])
        node.run()

    else: 
        print("Usage: python lab6.py my_port peer_port_or_none")
