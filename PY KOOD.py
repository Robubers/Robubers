# NB! kasutajalt sisendi võtmine peab igal juhul tsüklis olema niikaua kuni programm saab õige sisendi
# NB! kasutajasisend tuleb töödelda standardkujuke, nime puhul esisuurtäht, programmi jaoks vajalik sisend ühtlasele kujule jne
# kirjuta programm mis
#
# küsib kasutajalt tema pin koodi
# küsib kasutajalt tema isikukoodi
# kasutaja saab sisestada pin koodi ainult 3 korda
# kasutaja saab sisestada isikukoodi ka ainult 3 korda
# kui kasutaja on kõik korrad valesti sisestanud kas isikukoodi või pin koodi:
# - joonista kasutajale pilt, kus on kurb nägu trellide taga
# kui pinkood ja isikukood on õiged, küsi kasutajalt:
# - kas ta tahab raha välja võtta või oma pangakaarti tagasi
# - kui ta tahab raha välja võtta siis
# - - küsi kasutajalt kui palju ning joonista talle rahaleht mille peal on väljavõetud summa kirjutatud
# - kui ta tahab oma pangakaarti tagasi siis
# - - joonista talle pangakaart mille peal on tema isikukood


from tkinter import *

pinkood = "1111"  
isikukood = "12345678901"  
kood_attempt1 = 3
isikukood_attempt1 = 3

while kood_attempt1 > 0 and isikukood_attempt1 > 0:  
    kood_attempt = input("Sisestage pinkood: ")
    isikukood_attempt = input("Sisestage isikukood: ")

    if kood_attempt != pinkood:  
        kood_attempt1 -= 1
        print(f"Pinkood on vale! Sisesta veel. Sul on jäänud {kood_attempt1} katset.")

    if isikukood_attempt != isikukood:  
        isikukood_attempt1 -= 1
        print(f"Isikukood on vale! Sisesta veel. Sul on jäänud {isikukood_attempt1} katset.")

    if kood_attempt1 == 0 or isikukood_attempt1 == 0:  
        raam = Tk()
        raam.title("Ligipääs keelatud")

        tahvel = Canvas(raam, width=600, height=600)
        tahvel.pack()

        # Joonistame kurva näo trellide taga
        tahvel.create_rectangle(50, 50, 550, 500, outline="black", width=3)  # Trellid
        tahvel.create_oval(200, 100, 400, 300, fill="yellow")  # Nägu
        tahvel.create_oval(250, 150, 270, 170, fill="black")  # Vasak silm
        tahvel.create_oval(330, 150, 350, 170, fill="black")  # Parem silm
        tahvel.create_arc(250, 220, 350, 270, start=0, extent=-180, style=ARC)  # Kurb suu
        tahvel.create_line(50, 50, 50, 500, fill="black", width=5)  # Vasak trell
        tahvel.create_line(550, 50, 550, 500, fill="black", width=5)  # Parem trell
        tahvel.create_text(300, 550, text="Kahjuks oled süsteemi lukustanud!", font=("Arial", 20, "bold"), fill="red")

        raam.mainloop()
        break  

    if kood_attempt == pinkood and isikukood_attempt == isikukood:  
        print("Pinkood ja isikukood on õiged.")
        vastus = input("Kas tahate raha välja võtta või oma pangakaarti tagasi? ")
        break 
        
    if vastus.lower() == "raha välja võtta":
            # Küsime, kui palju raha tahab välja võtta
        summa = input("Kui palju raha soovite välja võtta? ")

        raam = Tk()
        raam.title("Väljavõetud raha")

        tahvel = Canvas(raam, width=600, height=600)
        tahvel.pack()

            # Joonistame rahalehe
        tahvel.create_rectangle(50, 50, 550, 350, outline="black", width=3)  # Rahaleht
        tahvel.create_text(300, 200, text=f"Väljavõetud summa: {summa} €", font=("Arial", 20, "bold"), fill="green")

        raam.mainloop()

    elif vastus.lower() == "pangakaart tagasi":
        raam = Tk()
        raam.title("Pangakaart")

        tahvel = Canvas(raam, width=600, height=600)
        tahvel.pack()

            # Joonistame pangakaardi
        tahvel.create_rectangle(50, 50, 550, 350, outline="blue", width=3)  # Pangakaart
        tahvel.create_text(300, 200, text=f"Isikukood: {isikukood}", font=("Arial", 15, "bold"), fill="black")

        raam.mainloop()
        
    break   
    







