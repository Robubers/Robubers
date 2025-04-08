# kirjuta programm mis
# küsib kasutajalt tsükli sees
# kas tal on hapukapsas
# - kui kasutajal ei ole, siis öeldakse et saab hautist
# kas tal on pott
# - kui kasutajal potti ei ole, siis öeldakse et suppi teha ei saa
# kas tal on vett
# - kui kasutajal vett ei ole, siis öeldakse et saab mulgikapsaid teha
# kas tal on kartulit
# kas tal on puljongit
# kas kasutajal on midagi muud kapis (ei/kasutajavastus)
# - kui kasutajal ei ole, siis öeldakse midagi eelnevatest sobivatest vastustest
# - kui kasutajal on, siis öeldakse et saab ühepajatoitu
# kogu arvutamine peab toimuma loogiliste tehetega






while True:
    hapukapsas = input("Kas sul on hapukapsast? (jah/ei): ").lower() == "jah"
    pott = input("Kas sul on pott? (jah/ei): ").lower() == "jah"
    vesi = input("Kas sul on vett? (jah/ei): ").lower() == "jah"
    kartul = input("Kas sul on kartulit? (jah/ei): ").lower() == "jah"
    puljong = input("Kas sul on puljongit? (jah/ei): ").lower() == "jah"
    muu = input("Kas sul on midagi muud kapis? (ei/kirjuta mida): ").lower()

    if not hapukapsas:
        print("Saad teha hautist.")
    elif not pott:
        print("Suppi teha ei saa.")
    elif not vesi:
        print("Saad teha mulgikapsaid.")
    elif kartul and puljong:
        print("Saad teha supi.")
    elif muu != "ei":
        print("Saad teha ühepajatoitu.")
    else:
        print("Sul ei ole piisavalt koostisosi ühegi toidu tegemiseks.")
    
    kas_jatkata = input("Kas soovid uuesti proovida? (jah/ei): ").strip().lower()
    if kas_jatkata != "jah":
        break