import tkinter as tk
from tkinter import messagebox
import random


class Vislice:
    def __init__(self, okno, poskusi, resitev):
        self.okno = okno
        self.poskusi=poskusi
        self.resitev=resitev
        
        self.igra()
                               
    #ustvarimo okno za igranje
    def igralno_polje (self):
        okno = self.okno
        ugani_crko = tk.Label(okno, text = 'Ugani črko:')
        ugani_crko.grid(row = 1, column = 1)
        self.crka = tk.StringVar(okno, value = None)
        vnos_crke = tk.Entry(okno, textvariable = self.crka)
        vnos_crke.grid (row = 1, column = 2)
        gumb_enter = tk.Button(okno, text = "Izberi", command = self.pravilnost)
        gumb_enter.grid(row = 1, column = 3)
        #izriši rezultat
        self.rezultat = tk.Canvas(okno, width = 300, height = 350)
        self.rezultat.grid(row = 2, column = 1)
        self.rezultat.create_rectangle(4, 4, 300, 350, width = 4, outline = "green")
        self.rezultat.create_text(200, 30, text = "Stanje:")
        #narise prazne črtice
        self.crte = tk.Canvas(okno, width = 550, height = 150)
        self.crte.grid( row = 2, column = 2)
        #nepravilne črke
        self.nepravilne_crke = tk.Canvas (okno, width = 300, height = 300)
        self.nepravilne_crke.grid (row = 3, column = 1)
        self.nepravilne_crke.create_rectangle(4, 4, 300, 100, width = 4)
        self.nepravilne_crke.create_text (200, 30, text = "Že poskušene črke:")       
       

    def pravilnost(self):
        abeceda="abcčdefghijklmnoprsštuvzž"
        if len(self.crka.get()) == 1 and self.crka.get() in abeceda:
            if self.crka.get() in self.resitev:
                if self.crka.get() not in self.ze_ugotovljene:
                    self.ze_ugotovljene.append(self.crka.get())
                    for i, znak in enumerate(self.crke_v_rezultatu):
                        if znak in self.ze_ugotovljene:
                            self.pravilna(i,znak)
            else:
                if self.crka.get() not in self.nepravilne:
                    self.nepravilne.append(self.crka.get())
                    self.poskusi = self.poskusi + 1
                    self.nepravilna(self.poskusi, self.crka.get())
                    self.izris(self.poskusi)
                    
        #počisti vnosno polje
        self.crka.set('')
        
        #konec igre (zmanjka ti poskusov ali uganeš besedo)
        if self.poskusi>=8:
            self.konec(False)
        if set(self.ze_ugotovljene) == set(self.crke_v_rezultatu):
            self.konec(True)
            
    def konec(self, zmaga):
        if zmaga:
            messagebox.showinfo("Igra je zaključena! Čestitke, zmaga je vaša!")
        else:
            messagebox.showinfo("igra je zaključena! Več sreče prihodnjič! Rešitev:" + self.resitev)

        nova_igra= messagebox.askyesno("Nova igra", "Želite nov izziv?")
        if nova_igra == True:
            self.igra()
        else:
            okno.destroy()

    def izris_(self, napacnih_crk):
        if napacnih_crk == 1:
            mapa1 = PhotoImage(file = "hangman1")
            self.rezultat.create_image(100, 100, image = mapa1)
        if napacnih_crk == 2:
            mapa2 = PhotoImage(file = "hangman2")
            self.rezultat.create_image(100, 100, image = mapa2)
        if napacnih_crk == 3:                               
            mapa3 = PhotoImage(file = "hangman3")
            self.rezultat.create_image(100, 100, image = mapa3)
        if napacnih_crk == 4:                               
            mapa4 = PhotoImage(file = "hangman4")
            self.rezultat.create_image(100, 100, image = mapa4)
        if napacnih_crk == 5:                               
            mapa5 = PhotoImage(file = "hangman5")
            self.rezultat.create_image(100, 100, image = mapa5)
        if napacnih_crk == 6:                               
            mapa6 = PhotoImage(file = "hangman6")
            self.rezultat.create_image(100, 100, image = mapa6)
        if napacnih_crk == 7:                               
            mapa7 = PhotoImage(file = "hangman7")
            self.rezultat.create_image(100, 100, image = mapa7)                              
        if napacnih_crk == 8:                               
            mapa8 = PhotoImage(file = "hangman8")
            self.rezultat.create_image(100, 100, image = mapa8)

    def narisemo_crtice(self, dolzina_besede):
        dolzina_besede = len(resitev)
        for i in range (dolzina_besede):
            self.crte.create_line(40 + 50 * i, 100, 80 + 50 * i, 100)
            
    def pravilna(self, mesto, crka):
        crka = crka.upper()
        self.crte.create_text(60 + 50 * mesto, 80, text = crka, font = ('Helvetica', '28', 'bold'))
                              
    def nepravilna(self, mesto, crka):
        crka = crka.upper()
        self.nepravilne_crke.create_text(60 * mesto, 90, text = crka, font = ('Helvetica', '28', 'bold'))
                              
    def igra(self):
        self.igralno_polje()                     
        self.seznam_besed = []
        with open(besede.txt)as dat:
            seznam_besed = dat.readline().split()
            self.resitev = random.choice(seznam_besed)
            self.crke_v_rezultatu = list(self.resitev.lower())
            self.ze_ugotovljene = []
            self.poskusi = 0
            self.nepravilne = []
            narisemo_crtice(len(self.crke_v_besedi))
            
        
                              
okno=tk.Tk()
okno.wm_title("Športne vislice")
vislice=Vislice(okno, 0, '')
                              
okno.mainloop()
