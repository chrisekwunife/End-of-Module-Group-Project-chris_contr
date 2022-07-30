import pickle
import json
import socket
#import xmltodict

# take the server name and port name
host = 'local host'
port = 5001

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect(('127.0.0.1', port))

# receive message from
while True:
    msg = s.recv(1024)

    # repeat as long as message
    # string are not empty
    while msg:
        data = msg.decode()
        print('Received data :' + data)

        # Conversion to Binary data
        c = ' '.join(format(ord(x), 'b') for x in data)
        print("===== Binary conversion =====")
        print(c)

        # # Conversion from Json to XML
        # json_to_xml = xmltodict.unparse(data)
        # print("===== XML conversion =====")
        # print(json_to_xml)

        print("\n\n")
        msg = s.recv(1024)

# disconnect the client
s.close()
