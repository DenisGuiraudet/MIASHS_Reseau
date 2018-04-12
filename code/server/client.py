import socket
import sys

hote = "localhost"
port = 8080

connectS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectS.connect((sys.argv[1],  int(sys.argv[2]) ))

connectS.send(sys.argv[3].encode())
messageR = connectS.recv(1024)

print("Connexion établie avec le serveur sur le port {}".format(port))
#hey
messageE = ""
while messageE != b"fin":
    messageE = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    messageE = messageE.encode()
    # On envoie le message
    connectS.send(messageE)
    messageR = connectS.recv(1024)
    print(messageR.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion client")
connectS.close()
