# server that needs to link to an IP address
import json
import socket


# take the server name and port name
host = 'local host'
port = 5001
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('local host', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
while True:
    c, addr = s.accept()

    # display client address
    print("CONNECTION FROM:", str(addr))

    dataDict = {}  # Dictionary Definition

    # Populate the dictionary ie Fruits,Vegetables and Nuts as store items
    dataDict = {'Store Items': ['Fruits', 'Vegetables', 'Nuts'], 'Fruits': {'Mango': 6, 'Orange': 3, 'Apple': 50, 'Grapes': 15}, 'Vegetables': {
        'Sweet potatoes': 100, 'Spinach': 20, 'Carrot': 18}, 'Nuts': {'Almonds': 10, 'Cashews': 5, 'Walnuts': 150, 'Peanuts': 80}}

    # Serialize the dictionary
    dataSerialize = json.dumps(dataDict)


    c.send(dataSerialize.encode())

    with open("file_1.txt", "rb") as f:
        c.send(f.read())
    # disconnect the server
    c.close()






