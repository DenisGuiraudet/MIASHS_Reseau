from socket import *
import pickle
import sys,os, threading

def storeClient(adr,nomUser):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        if adr in data:
            pass
        else:
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
        users = {"res" : "null", "192.168.1.1" : ["jo", "pause", {"x" : 0, "y" : 0, "res" : 0}]}
        with open('./donnees.json', 'wb') as fichier:
            pickle.dump(users,fichier)

def initRobot(adr,Tx,Ty):
    isTaken = False
    if getPos(Tx,Ty) == 1:
        takeRes(Tx,Ty)
        isTaken = True
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        if isTaken == True:
            data[adr][2] = {"x" : Tx, "y" : Ty, "res" : 1}
        else :
            data[adr][2] = {"x" : Tx, "y" : Ty, "res" : 0}
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def takeRes(Tx,Ty):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)
        if data["res"] == "null":
            data["res"] = [[Tx,Ty]]
        else:
            data["res"].append([Tx,Ty])
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
    isTaken = False
    if getPos(Tx,Ty) == 1:
        takeRes(Tx,Ty)
        isTaken = True

    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        data[adr][2]['x'] = Tx
        data[adr][2]['y'] = Ty
        if isTaken == True:
            data[adr][2]['res'] = data[adr][2]['res'] + 1
    with open('./donnees.json','wb') as fichier:
        pickle.dump(data,fichier)
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        print(data)

def appStatus():
    mapStatus = {}
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        for value in data:
            if value == "res":
                pass
            else :
                mapStatus[value] = data[value]
        return mapStatus

def getMap():
    themap = []
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        for value in data:
            if value == "res":
                pass
            else :
                themap.append([data[value][0],data[value][2]['x'],data[value][2]['y']])
        return themap

def getMyPos(adr):
    mypos = []
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        mypos.append([data[adr][2]['x'],data[value][2]['y']])
        return mypos

def traiter_client(client,adre):
    cmd = client.recv(255)
    tab = cmd.decode().split(" ")
    print (tab)

def isInit(adr):
    with open('./donnees.json', 'rb') as fichier:
        data = pickle.load(fichier)
        if data[adr][2] == "null":
            return False
        else:
            return True


    if tab[0].upper() == "INIT":
        if len(tab) != 3:
            client.send(b"Nombre parametre incorrect .... NOK")
        else:
            initRobot(adre,tab[1],tab[2])
            client.send(b"Initialisation .... OK")


    elif tab[0].upper() == "PAUSE":
        pauseClient(adre)
        client.send(b"Mise en pause .... OK")


    elif tab[0].upper() == "PLAY":
        playClient(adre)
        client.send(b"Mise en jeu .... OK")


    elif tab[0].upper() == "TAKERES":
        takeRes(tab[1],tab[2])
        client.send(b"Recolte .... OK")


    elif tab[0].upper() == "SETPSEUDO":
        if len(tab) != 2:
            client.send(b"Nombre parametre incorrect .... NOK")
        else:
            setPseudo(adre,tab[1])
            client.send(b"Changement de pseudo .... OK")


    elif tab[0].upper() == "GETATPOS":
        if len(tab) != 3:
            client.send(b"Nombre parametre incorrect .... NOK")
        else :
            val = getPos(tab[1],tab[2])
            client.send(str(val).encode())

    elif tab[0].upper() == "MOVETO":
        if len(tab) != 3:
            client.send(b"Nombre parametre incorrect .... NOK")
        else :
            moveTo(adre,tab[1],tab[2])
            client.send(b"Deplacement ..... OK")

    elif tab[0].upper() == "APPSTATUS":
        mapStat = appStatus()
        client.send(str(mapStat).encode())

    elif tab[0].upper() == "GETMAP":
        print("hey")
        mapActu = getMap()
        client.send(str(mapActu).encode())

    elif tab[0].upper() == "GETMYPOS":
        mapActu = getMyPos(adre)
        client.send(str(mapActu).encode())

    elif tab[0].upper() == "ISINIT":
        isInit = isInit(adre)
        client.send(str(isInit).encode())

    elif tab[0].upper() == "CONNECT":
        storeClient(adre,tab[0])
        client.send(b"Init ok")

    else :
        client.send(b"Commande Inconnu")

    client.close()






#creation socket
sock_server = socket()
sock_server.bind(('',  int(sys.argv[1]) ))
sock_server.listen(5)

initFile()

while True:
    sock_client, adr_client = sock_server.accept()
    threading.Thread(target=traiter_client, args=(sock_client,adr_client[0],)) \
        .start()



    #print(cmd.decode())

sock_server.shutdown(SHUT_RDWR)
for t in threading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)
