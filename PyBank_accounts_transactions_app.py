import os
import datetime


ocisti = 'cls' if os.name == 'nt' else 'clear'

while True:
    #### Glavni izbornik

    os.system(ocisti)

    print("*************************************************************")
    print("\t\t\tPyBANK App\n")
    print("\t\t\tGLAVNI IZBORNIK\n")
    print("1. Kreiranje racuna")
    print("2. Prikaz stanja racuna")
    print("3. Prikaz prometa po racunu")
    print("4. Polog novca na racun")
    print("5. Podizanje novca s racuna")
    print("0. Izlaz")
    print("-------------------------------------------------------------")
    print("Jos niste otvorili racun. Molimo prvo kreirajte racun. Hvala!")
    print("-------------------------------------------------------------")
   
    izbor = input("Vas izbor:\t")
   
    os.system(ocisti)
   
    if izbor == "1":
        #### Kreiranje racuna

        print("*************************************************************")
        print("\t\t\tPyBANK App\n")
        print("\t\t\tKREIRANJE RACUNA\n")

        print("Podaci o vlasniku racuna\n")

        naziv_tvrtke = input("Naziv Tvrtke:\t\t\t\t")
        ulica_broj = input("Ulica i broj sjedista Tvrtke:\t\t")
        posta = input("Postanski broj sjedista Tvrtke:\t\t")
        grad = input("Grad u kojem je sjediste Tvrtke:\t")

        while True:
            oib = input("OIB Tvrtke:\t\t\t\t")
            if len(oib) != 11:
                print("Unos Vašeg OIB-a je neispravan. Molimo pokušajte ponovno.")
                continue
            else:
                break

        osoba = input("Ime i prezime odgovorne osobe Tvrtke:\t")
        valuta = input("\nUpisite naziv valute racuna (EUR ili HRK):\t")

        input("\nSPREMI? (Pritisnite bilo koju tipku)")
        os.system(ocisti)

        ## Potvrda kreiranja racuna

        print("*************************************************************")
        print("\t\t\tPyBANK App\n")
        print("\t\t\tKREIRANJE RACUNA\n")
        print(f"Podaci o vlasniku racuna tvrtke {naziv_tvrtke} su uspjesno spremljeni\n")
        input("Za nastavak pritisnite bilo koju tipku ")
        os.system(ocisti)

        ## Stanje racuna

        print("*************************************************************")
        print("\t\t\tPyBANK App\n")
        print("\t\t\tKREIRANJE RACUNA\n")
        print("Stanje racuna\n")

        timestamp_racun = datetime.datetime.now()
        godina_mjesec = timestamp_racun.strftime("%Y-%m")
        business_account = "BA"
 
        redni_broj = "36"  #hardcoded for now
        if len(redni_broj) <= 5:
            redni_broj = redni_broj.zfill(5)
               
        racun = business_account + "-" + godina_mjesec + "-" + redni_broj
        stanje_racuna = 0
        promet = []

        def polog(novi_polog):
            global stanje_racuna 
            stanje_racuna += novi_polog
            promet.append(("Polozili ste ", novi_polog))

        def podizanje(iznos_podizanja):
            global stanje_racuna 
            stanje_racuna -= iznos_podizanja
            promet.append(("Podigli ste ", iznos_podizanja)) 

        print(f"Broj racuna {racun}")
        print(f"Trenutno stanje racuna: {stanje_racuna} {valuta}")
        print("_____________________________________________________________")
        print("Molimo vas upisite iznos koji zelite poloziti na racun.")
        print("NAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n")
        novi_polog = float(input())
        polog(novi_polog)
        stanje_racuna_2dec = round(stanje_racuna, 2)
        print(f"Novo stanje racuna: {stanje_racuna} {valuta}")
        stanje_racuna += 0
        print("-------------------------------------------------------------")
        input("Za povratak u Glavni izbornik pritisnite bilo koju tipku ")
        os.system(ocisti)

    elif izbor == "2":

        #### Prikaz stanja racuna

        print("*************************************************************")
        print("\t\t\tPyBANK App\n")
        print("\t\t\tPRIKAZ STANJA RACUNA\n")

        print(f"Broj racuna:\t\t{racun}")
        print(f"Datum i vrijeme:\t{timestamp_racun}")

        stanje_racuna += 0
        stanje_racuna_2dec = round(stanje_racuna, 2)

        print(f"\nTrenutno stanje racuna: {stanje_racuna_2dec} {valuta}")
        print("-------------------------------------------------------------")
        input("Za povratak u Glavni izbornik pritisnite bilo koju tipku ")
        os.system(ocisti)
   
    elif izbor == "3":

        #### Prikaz prometa po racunu
        
        print("*************************************************************")
        print("\t\t\tPyBANK App\n")
        print("\t\t\tPRIKAZ PROMETA RACUNA\n")

        print(f"Broj racuna:\t\t{racun}")
        print(f"Datum i vrijeme:\t{timestamp_racun}")

        stanje_racuna += 0
        stanje_racuna_2dec = round(stanje_racuna, 2)

        print(f"\nTrenutno stanje racuna: {stanje_racuna_2dec} {valuta}")
        print("_____________________________________________________________")
        print("Prikaz prometa racuna:")
        for p in promet:
            print(p[0], p[1])

        print("-------------------------------------------------------------")
        input("Za povratak u Glavni izbornik pritisnite bilo koju tipku ")
        os.system(ocisti)

    elif izbor == "4":

        #### Polog novca na racun

        print("*************************************************************")
        print("\t\t\tPyBANK App\t\t\t\n")
        print("\t\tPOLOG NOVCA NA RACUN\t\t\n")

        print(f"Broj racuna:\t\t{racun}")
        print(f"Trenutno stanje racuna: {stanje_racuna_2dec} {valuta}")
        print("_____________________________________________________________")

        print("\nMolimo vas upisite iznos koji zelite poloziti na racun.")
        print("NAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n")
        novi_polog = float(input())
        polog(novi_polog)
        #stanje_racuna += novi_polog
        stanje_racuna_2dec = round(stanje_racuna, 2)

        print(f"Novo stanje racuna: {stanje_racuna_2dec} {valuta}")
        print("-------------------------------------------------------------")
        input("Za povratak u Glavni izbornik pritisnite bilo koju tipku ")
        os.system(ocisti)

    elif izbor == "5":

        #### Podizanje novca s racuna

        print("*************************************************************")
        print("\t\t\tPyBANK App\t\t\t\n")
        print("\t\tPODIZANJE NOVCA S RACUNA\t\t\n")

        print(f"Broj racuna:\t\t{racun}")
        print(f"Trenutno stanje racuna: {stanje_racuna_2dec} {valuta}")
        print("_____________________________________________________________")

        print("\nMolimo vas upisite iznos koji zelite podici s racuna.")
        print("NAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n")
        iznos_podizanja = float(input())
        podizanje(iznos_podizanja)
        #stanje_racuna -= iznos_podizanja
        stanje_racuna_2dec = round(stanje_racuna, 2)

        print(f"Novo stanje racuna: {stanje_racuna_2dec} {valuta}")
        print("-------------------------------------------------------------")
        input("Za povratak u Glavni izbornik pritisnite bilo koju tipku ")
        os.system(ocisti)

    else:

        #### Izlaz
       
        break
