#PREMJESTANJE PODATAKA 1 - 33                   #Kod uspjesno appenda
from tkinter import *                           #podatke, ali ukupno nema jos
from tkinter import messagebox as tkmsg        #NADALJE unos provjeru dodati 
from tkinter import font as tkFont             #i u ukupno box zbroj cijena
import csv

fieldnames = ["Proizvod","Datum","Cijena","Ukupno"]
unos = []  

def reade():
    try:
        e, r, t = str(UnosProizvod.get()), UnosDatum.get(), float(UnosCijena.get()) #vucemo input sa entria
        unos.append([e, r, t, None])                                                #i appendamo u listu
                                                                                    # unos

        with open("majmun.csv", "a", newline = '') as ap:         # ovdje appendamo i pisemo u csv file
            apend = csv.writer(ap, delimiter = ";")               # input od komada koda prije 
            for red in unos:   
                apend.writerow(red)

        with open("majmun.csv","r", newline = '') as f:           # ovdje citamo csvfile i spremamo u citac
            citac = csv.reader(f, delimiter = ";")                # nakon toga clear-amo listu unos i
            unos.clear()                                          # appendamo liste iz citaca u listu unos
            
            for row in citac:
                if 'Cijena' in row:
                    continue
                else:
                    unos.append(row)

            unos[0].insert(3, sum(int(float(i[2])) for i in unos))
            #unos[0][2] = sum(int(float(i[2])) for i in unos)
            print(unos) 

        with open("majmun.csv", "w", newline = '') as wr:          # ovdje zapisujemo sa liste unos sa w
            pisac = csv.writer(wr, delimiter = ";")                # i time brisemo sve od prije u csvfile-u
                                                                   #
            fieldnames = ["Proizvod","Datum","Cijena","Ukupno"]

            pisac.writerow(fieldnames)
            pisac.writerow(unos[0][0:-1])
            for ny in unos[1:]:
                pisac.writerow(ny)

        unos.clear()
            
    except:
        tkmsg.showinfo(title = "Error", message = "Krivi unos!")
    else:
        tkmsg.showinfo(title = "Output", message = "Uspjesan unos!")
    finally:
        x.set('')
        y.set('')
        z.set('')
        
#TKINTER 35 - 84
prozor = Tk()

HelReg = tkFont.Font(family = 'Arial', size = 15)

x = StringVar()
y = StringVar()
z = StringVar()

#Geometrija i centriranje
w = 682
h = 130
#trazim duzinu i visinu ekrana
ws = prozor.winfo_screenwidth()
hs = prozor.winfo_screenheight()
#kalkuliram x i y koordinate za prozor
xos = (ws/2) - (w/2)
yos = (hs/2) - (h/2)
#set dimenzije i gdje da se pojavi
prozor.geometry('%dx%d+%d+%d' % (w, h, xos, yos)) #USPJESNO CENTRIRAN!

prozor.title("Program za pohranu troskova")

Unesite = Label(prozor, text = "Unesite sljedece:",
                font = HelReg, width = 20)
Unesite.grid(row=0, column=1)

UnesiteP = Label(prozor, text = "Proizvod", font = HelReg, width = 20)
UnesiteP.grid(row=1, column=0)

UnesiteD = Label(prozor, text = "Datum", font = HelReg, width = 20)
UnesiteD.grid(row=1, column=1)

UnesiteC = Label(prozor, text = "Cijena", font = HelReg, width = 20)
UnesiteC.grid(row=1, column=2)

UnosProizvod = Entry(prozor, text = x, font = HelReg, width = 20)
UnosProizvod.grid(row = 2, column = 0)

UnosDatum = Entry(prozor, text = y, font = HelReg, width = 20)
UnosDatum.grid(row = 2, column = 1)

UnosCijena = Entry(prozor, text = z, font = HelReg, width = 20)
UnosCijena.grid(row = 2, column = 2)

Pohrani = Button(prozor, text = "Pohrani", width = 20,
                 font = HelReg, command = reade)
Pohrani.grid(row = 3, column = 1)

prozor.mainloop()