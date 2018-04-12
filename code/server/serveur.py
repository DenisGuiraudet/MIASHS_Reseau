from socket import *
import pickle
import sys,os

def storeClient(adr,nomUser):
    ## TODO: Verif si c'est le bon user avec l'IP et le nom
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        if type(data) == dict:
            data[adr] = [nomUser,"play","null"]
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def initFile():
    try:
        with open('./donnees.json'):
            pass
    except IOError:
        users = {}
        with open('./donnees.json', 'wb') as fichier:
            pickle.dump(users,fichier)

def initRobot(adr):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        data[adr][2] = {"x" : 1, "y" : 0, "res" : 0}
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)


#creation socket
sock_server = socket()
sock_server.bind(('',  int(sys.argv[1]) ))
sock_server.listen(5)

initFile()
sock_client, adr_client = sock_server.accept()

while True:
    cmd = sock_client.recv(255)
    tab = cmd.decode().split(" ")
    print (tab)
    if tab[0].upper() == "INIT":
        if len(tab) != 3:
            sock_client.send(b"Nombre parametre incorrect .... NOK")
        else:
            initRobot(adr_client[0],tab[1],tab[2])
            sock_client.send(b"Initialisation .... OK")
    else :
        storeClient(adr_client[0],tab[0])
        sock_client.send(b"Stockage du client .... OK")

    #print(cmd.decode())

sock_server.shutdown(SHUT_RDWR)
for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)
