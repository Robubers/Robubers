while True:
    hapukapsas = input("Kas sul on hapukapsast? ja/ei: ")
    pott = input("Kas sul on pott? ja/ei: ")
    vesi = input("Kas sul on vett? ja/ei: ")
    kartul = input("Kas sul on kartulit? ja/ei: ")
    puljong = input("Kas sul on puljongit? ja/ei: ")
    muu = input("Kas sul on midagi muud kapis? ei/kirjuta mida: ")

    if not hapukapsas:
        print("Saad valmistada hautist.")
    elif not pott:
        print("Suppi ei saa teha")
    elif not vesi:
        print("Saadd valmistada mulgikapsast.")
    elif kartul and puljong:
        print("Saad valmistada suppi.")
    elif muud != "ei":
        print("Saad valmistada ühepajatoitu.")
    else:
        print("Sul pole piisavalt koostisosi ühegi toidu tegemiseks.")
    
    Proov = input("Kas soovid uuesti proovida? jah/ei: ")
    if Proov != "Jah":
        break