from socket import *
import pickle
import sys

def storeClient(nomUser):
    listeUser = {
        nomUser : 0
    }
    with open('donnees.txt', 'wb') as fichier:
        pick = pickle.Pickler(fichier)
        pick.dump(nomUser)
    with open('donnees.txt', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        score_recupere = mon_depickler.load()
        print (score_recupere)


#creation socket
sock_server = socket()
sock_server.bind(('',  int(sys.argv[1]) ))
sock_server.listen(5)

sock_client, adr_client = sock_server.accept()

while True:
    cmd = sock_client.recv(255)
    if cmd.decode().upper() == "CONNECT":
        sock_client.send(b"Connexion ....")
    else :
        storeClient(cmd.decode().upper())
        sock_client.send(b"Commande inexistante")
    print(cmd.decode())

sock_server.shutdown(SHUT_RDWR)
for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)
