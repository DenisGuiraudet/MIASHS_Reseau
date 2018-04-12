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
        users = {"res" : [[1,2],[2,3]]}
        with open('./donnees.json', 'wb') as fichier:
            pickle.dump(users,fichier)

def initRobot(adr,Tx,Ty):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        data[adr][2] = {"x" : Tx, "y" : Ty, "res" : 0}
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def pauseClient(adr):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        data[adr][1] = "pause"
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def playClient(adr):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        data[adr][1] = "play"
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def setPseudo(adr,newPseudo):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        data[adr][0] = newPseudo
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def getPos(Tx,Ty):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        if data["res"] == "null":
            return 1
        else :
            for value in data["res"]:
                if str(value[0]) == Tx and str(value[1]) == Ty:
                    return 0
            return 1

def moveTo(adr,Tx,Ty):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data[adr][2])
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
    elif tab[0].upper() == "PAUSE":
        pauseClient(adr_client[0])
        sock_client.send(b"Mise en pause .... OK")
    elif tab[0].upper() == "PLAY":
        playClient(adr_client[0])
        sock_client.send(b"Mise en jeu .... OK")
    elif tab[0].upper() == "SETPSEUDO":
        if len(tab) != 2:
            sock_client.send(b"Nombre parametre incorrect .... NOK")
        else:
            setPseudo(adr_client[0],tab[1])
            sock_client.send(b"Changement de pseudo .... OK")
    elif tab[0].upper() == "GETATPOS":
        if len(tab) != 3:
            sock_client.send(b"Nombre parametre incorrect .... NOK")
        else :
            val = getPos(tab[1],tab[2])
            print(val)
            sock_client.send(str(val).encode())
    elif tab[0].upper() == "MOVETO":
        if len(tab) != 3:
            sock_client.send(b"Nombre parametre incorrect .... NOK")
        else :
            val = getPos(tab[1],tab[2])
            print(val)
            sock_client.send(str(val).encode())
    else :
        storeClient(adr_client[0],tab[0])
        sock_client.send(b"Stockage du client .... OK")

    #print(cmd.decode())

sock_server.shutdown(SHUT_RDWR)
for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)
