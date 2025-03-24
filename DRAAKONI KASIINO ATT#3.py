 # 3 - Draakoni kasiino
 #
 # kirjuta programm mis:
 # küsib kasutajalt tsükli sees kui palju raha ta panustada soovib
 # - kui kasutaja sisestab positiivse arvväärtuse, tsükkel lõppeb ja programm läheb järgmise osa juurde
 # - kui kasutaja sisestab negatiivse arvväärtuse, siis öeldakse kasutajale et on vaja positiivset rahasummat ja küsimus küsitakse uuesti
 # - ja küsimus küsitakse uuesti
 # NB! - draakonil on sama arv raha, kui on mängijal, aga selleks ei kasutata ühte sama muutujat
 # järgmine osa toimub teise tsükli sees niikaua kuni mängijal raha otsas ei ole või niikaua kuni draakonil raha otsas ei ole:
 # - draakon küsib palju sisestatud rahasummast ta see mänguring panustada soovib.
 # - - panus ei saa olla suurem kui rahasumma mis kasutaja algselt sisestas.
 # - draakon küsib kas arv on suurem kui see arv, mis tema kolm kuuekülgset täringut kokku saavad.
 # - kasutaja sisestab arvu
 # - juhuarvu abil, veeretatakse kolme kuuekülgset täringut
 # - - kui kasutaja arvab õigesti, annab draakon talle 2x esialgset panust
 # - - kui kasutaja arvab valesti on ta oma eelnevast panusest ilma
 # - mängija võidab siis kui draakonil on näpud põhjas
 # - draakon küsib mängijalt peale igat mänguringi kas ta soovib oma võidud välja võtta ning mängulauast lahkuda
 # - - kui kasutaja vastab ei, jätkub mäng nagu tavaliselt
 # - - kui kasutaja vastab jah, ütleb draakon mängijale siin on sinu võidud (peab panema kui palju mängija oma algsummale juurde võitis), ootan sind ja sinu raha siia tagasi...
 
 
from random import randint
 
mangija_raha = 3000
draakoni_raha = 3000

 
print("tere tulemast draakoni kasiinose, palju tahate panustada?")
panus = int(input())
if panus <= 30:
    print("on vaja positiivse summaga panust")    
else:
    print("panus on vastuvõetud")
    
     
while mangija_raha > 0 and draakoni_raha > 0:
    print("palju tahate panust selle mänguringi sisse panna?")
    manguringi_panus = int(input())
    
    
    
    
    if manguringi_panus > 3000:
        print("kahjuks tee ei saa panna rohkemat summat mängu")
    
    elif manguringi_panus < 3000:
        print("panus on vastuvõetud, üelge arv ja veeretan täringu")
        
        taring = randint(1, 6)
        taringu_kulg = int(input())
        
        if (taringu_kulg == taring):
            print("Palju õnne, sa võitsid! Siin on sinu võit: " + str(manguringi_panus * 2)+"")
            
            mangija_raha + manguringi_panus
            draakoni_raha - manguringi_panus
            print("kas tahad jätkata?")
            kasutaja_vastus = input()
            if kasutaja_vastus == "ei":
                print("olgu nii, ootame teid järgmine kord!")
            else:
                print("alustame uue mänguringiga")
        
        else:
            print("kahjuks kaotasid, tahad jätkata?")
            
            kasutaja_vastus = input()
           
            mangija_raha - manguringi_panus
            draakoni_raha + manguringi_panus
            
            
            if kasutaja_vastus == "ei":
                print("olgu nii, ootame teid järgmine kord!")
            else:
                print("alustame uue mänguringiga")
            
                
if mangija_raha <= 0:
    print("Mängija raha on otsas. Mäng lõpeb, aitäh et osalesite!")
elif draakoni_raha <= 0:
    print("Draakoni raha on otsas. Mäng lõpeb, palju õnne võiduga!")                   
                    