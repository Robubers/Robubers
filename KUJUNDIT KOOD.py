# NB! kasutajalt sisendi võtmine peab igal juhul tsüklis olema niikaua kuni programm saab õige sisendi
# NB! kasutajasisend tuleb töödelda standardkujuke, nime puhul esisuurtäht, programmi jaoks vajalik sisend ühtlasele kujule jne
# kirjuta programm mis
#
# küsib kasutajalt kui vana ta on
# küsib kasutajalt kui pikk ta on meetrites
# küsib kasutajalt tema ees ja perekonnanime
# küsib kasutajalt kas talle meeldivad geomeetrilised kujundid
# kui kasutaja vastab jah, siis küsitakse kasutajalt terve rida küsimusi järgnevate kujundite kohta: (ring, ruut, kolmnurk, ovaal)
# - kas talle meeldib <kujund>
# - kui kasutaja vastab <kujund>i kohta jah, siis peab programm meelde jätma et kasutaja tahab seda kujundit eraldi muutujas
# - kasutajalt küsitakse ka tema lemmikvärvi kohta, mille jaoks antakse kasutajale inglisekeelne valik
# - seejärel joonistab programm kõik kujundid mis said "jah" vastuse kasutaja lemmikvärviga ekraanile +
# - kujundite küljepikkus tuleb läbi korrutada kasutaja pikkusega. kujundite standardküljepikkus on 100px
# - Viimasena joonistatakse ekraanile teksti abil sõnum "palun"<kasutajanimi>"siin on sinu lemmikkujundid"<värv> värviga



from tkinter import *


kujund_oval = ""
kujund_kolmnurk = ""
kujund_ruut = ""
kujund_ring = ""
pikkus = ""
lemmik_varv = "" 



tsukkel = True
while tsukkel:
    vanus = input("Tere kasutaja! Kui vana sa oled?").lower()
    nimi = input("mis on su nimi ja perkonnanimi ?").lower().title()
    vastus = input("kas sulle meeldivad geomeetrilised kujundid?").lower()
    if vastus == "jah":
        kujund_oval = input("kas sulle meeldib ovaal?").lower()
        kujund_kolmnurk = input("kas sulle meeldib kolmnurk?").lower()
        kujund_ruut = input("kas sullle meeldib ruut?").lower()
        kujund_ring = input("kas sulle meeldib ring?").lower()
        valik = input("vali üks värv ja ma joonistan sulle kujundi sinu lemmikuga värviga valikus on: \n 1. orange \n 2. yellow \n 3. green \n 4. red \n 5. blue \n 6. black \n ( sisesta number mis tahistab su lemmik varvi )  ")

        if valik == "1":
            lemmik_varv = "orange"
        elif valik == "2":
            lemmik_varv = "yellow"
        elif valik == "3":
            lemmik_varv = "green"
        elif valik == "4":
            lemmik_varv = "red"
        elif valik == "5":
            lemmik_varv = "blue"
        elif valik == "6":
            lemmik_varv = "black"
        
        else:
            lemmik_varv = ""
            print("Invalid choice, sa ei valinud värvi ")
        
        
        
    raam = Tk()
    raam.title("window")
    
        
    tahvel = Canvas(raam, width=600, height=600  )
    
    tahvel.create_text(300,300, text="siin on sinu kujund "+nimi+" koos sinu "+lemmik_varv+" lemmik värviga")

    if kujund_oval == "jah":
        tahvel.create_oval(247, 297, 353, 603, fill=lemmik_varv)
        
    elif kujund_kolmnurk == "jah":
        tahvel.create_polygon(300, 100, 200, 300, 400, 300, fill=lemmik_varv)
        
    elif kujund_ruut == "jah":
        tahvel.create_rectangle(50,50,300,300, fill=lemmik_varv)
    
    elif kujund_ring == "jah":
        tahvel.create_oval(200, 200, 400, 400, fill=lemmik_varv)
        
        
    tahvel.pack()
    
    raam.mainloop()
        
        
else:
    print("okei head aega siis ")
    
        
        
        
    

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        