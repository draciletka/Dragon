import hodnoty # Pomocný modul pro zpracování dat z uložené hry

"""
Hra, ve které se stanete majitelem dráčka. Dobře se o něj starejte, aby mu nic nescházelo. Hra končí, pokud dráčkovi klesne zdraví na nulu. 
"""

class Drak:
    
    # Dračí třída.
    def __init__ (self, jmeno, energie, sytost, stesti, cistota, zdravi, reputace, vzdelani):
        self.jmeno = jmeno
        self.max_energie = energie
        self.energie = energie
        self.sytost = sytost
        self.max_stesti = stesti
        self.stesti = stesti
        self.max_cistota = cistota
        self.cistota = cistota
        self.max_zdravi = zdravi
        self.zdravi = zdravi
        self.reputace = reputace
        self.vzdelani = vzdelani

    def __str__ (self):
        # Vypíše drakovo jméno.
        return self.jmeno

    def vypsat (self):
        # Spočítá zdraví a vypíše drakovy aktuální hodnoty.
        if self.cistota < 10:
            self.zdravi = self.zdravi - 1
        if self.energie < 10:
            self.zdravi = self.zdravi - 1
        if self.sytost < 10:
            self.zdravi = self.zdravi - 1
        
        en = self.energie - 10
        sy = self.sytost - 10
        ste = self.stesti - 10
        cis = self.cistota - 10
        zdr = self.zdravi - 10
        rep = self.reputace - 10
        vzd = self.vzdelani - 10
        print(f"\t{self.jmeno}\n\tenergie {en}\n\tsytost {sy}\n\tštestí {ste}\n\tčistota {cis}\n\tzdraví {zdr}\n\treputace {rep}\n\tvzdělání {vzd}")

    @property # vlastnost únava
    def unaveny (self):
        return self.energie < 14 

    @property # vlastnost hlad   
    def hladovy (self):
        return self.sytost < 14

    def jist (self):
        # Draka můžeme nakrmit. Dle druhu jídla se mu kromě hladu mohou změnit i jiné hodnoty.
        print(f"Čím chceš {self.jmeno} nakrmit?\n\t1 nechat napást v parku\n\t2 sousedovic slepice\n\t3 vlastní slepice\n\t4 čokoláda\n\t5 dračí pálivé lívanečky\nVyber číslo:") 
        odpoved = int(input())
        if odpoved == 1:
            self.sytost = self.sytost + 8
            self.energie = self.energie - 5
            self.reputace = self.reputace - 4
            self.stesti = self.stesti - 5
            self.cistota = self.cistota - 5
            print(f"{self.jmeno} se v parku nacpal pejskařem a dogou. Stálo ho to hodně sil, ale nacpal se k prasknutí. Moc nadšený ze svého činu není a ještě ho u toho viděli návštěvníci parku. A taky se zapatlal.")
        elif odpoved == 2:
            self.sytost = self.sytost + 3
            self.energie = self.energie - 1
            self.reputace = self.reputace - 1
            self.stesti = self.stesti - 1
            self.cistota = self.cistota - 3
            print(f"{self.jmeno} se vplížil na sousedovic dvůr a slupnul slípku. Zápas byl velice hlasitý a přivolal souseda. Draka to trochu rozesmutnilo. Taky se mu podařilo umazat.")
        elif odpoved == 3:
            self.sytost = self.sytost + 3
            self.stesti = self.stesti + 1
            self.cistota = self.cistota - 2
            print(f"{self.jmeno} spořádal slepici z vlastního kurníku. Nedalo mu to ani moc práce a je šťastný, že jedl z vlastních zásob a nezakousl žádného člověka.")
        elif odpoved == 4:
            self.sytost = self.sytost + 1
            self.energie = self.energie + 1
            self.stesti = self.stesti + 3
            self.cistota = self.cistota - 1
            print(f"{self.jmeno} slupnul čokoládu. Šťastně se zubí umazanou tlamkou.")
        elif odpoved == 5:
            self.sytost = self.sytost + 5
            self.energie = self.energie + 5
            self.stesti = self.stesti + 5
            self.cistota = self.cistota - 2
            print(f"{self.jmeno} spořádal hromadu dračích pálivých lívanečků. Jde vidět, jak moc mu chutnaly, protože je špinavý až za ušima.")
        else:
            print("Odpověď musí být číslo.")
        drak.vypsat()

    def spat (self):
        # Unavený drak získá energii.
        print("Vyber číslo pro druh spánku:\n\t1 Šlofík za komínem\n\t2 Hluboký spánek v krbu")
        spanek = int(input())
        if spanek == 1:
            self.energie = self.energie + 3
            print(f"{self.jmeno} si schrupnul.")
        elif spanek == 2:
            self.energie = self.energie + 10
            self.sytost = self.sytost - 5
            print(f"{self.jmeno} prospal několik hodin a pořádně mu vyhládlo.")
        else:
            print("Odpověď musí být číslo.")
        drak.vypsat()

    def hrat_si (self):
        # Pokud není hladový ani unavený, drak si může hrát, tím získat štěstí, ale i něco jiného. Pozor na zlobivé draky!
        if self.hladovy:
            print(f"{self.jmeno} má hlad.")
        else:
            if self.unaveny:
                print(f"{self.jmeno} je příliš unavený.")
            else:
                print("Vyber číslo pro druh hry:\n\t1 Podpalovat skládku za městem\n\t2 Běhat po lesích\n\t3 Skládat lego")
                hra = int(input())
                if hra == 1:
                    self.energie = self.energie - 5
                    self.cistota = self.cistota - 5
                    self.reputace = self.reputace - 5
                    self.stesti = self.stesti + 3
                    print(f"{self.jmeno} se při podpalování skládky pořádně zamazal a jeho pověst utrpěla. Je o něco veselejší a utahanější.")
                elif hra == 2:
                    self.energie = self.energie - 2
                    self.stesti = self.stesti + 5
                    print(f"{self.jmeno} je z lesa plný energie, že ho běh ani moc neunavil a je šťastný.")
                elif hra == 3:
                    self.energie = self.energie - 1
                    self.stesti = self.stesti + 5
                    self.vzdelani = self.vzdelani + 2
                    print(f"{self.jmeno} je šťastný. Skládání mu jde samo, procvičil si také mysl a ani se moc neunavil.")
                else:
                    print("Odpověď musí být číslo.")
        drak.vypsat()
           

    def ucit_se (self):
        # Bez únavy si dráček může potrénovat hlavu.
        if self.unaveny:
                print(f"{self.jmeno} je příliš unavený.")
        else:
            print("Vyber akci:\n\t1 Číst\n\t2 Počítat")
            uceni = int(input())
            if uceni == 1:
                self.energie = self.energie - 1
                self.vzdelani = self.vzdelani + 3
                self.stesti = self.stesti + 1
                print(f"{self.jmeno} je šťastnější a vzdělanější.")
            elif uceni == 2:
                self.energie = self.energie - 3
                self.vzdelani = self.vzdelani + 3
                self.stesti = self.stesti + 2
                print(f"{self.jmeno} se pořádně zapotil a přesto je šťastný, protože vyřešil velice obtížný příklad.")
            else:
                print("Odpověď musí být číslo.")
        drak.vypsat()

    def pracovat (self):
        # Pokud není unavený a hladový, může pracovat.
        if self.hladovy:
            print(f"{self.jmeno} má hlad.")
        else:
            if self.unaveny:
                print(f"{self.jmeno} je příliš unavený.")
            else:
                print(f"Vyber, co má {self.jmeno} udělat:\n\t1 Nanosit dříví a zapálit v krbu staré paní v lese.")
                prace = int(input())
                if prace == 1:
                    self.energie = self.energie - 4
                    self.reputace = self.reputace + 2
                    self.cistota = self.cistota - 2
                    self.stesti = self.stesti + 2
                    self.sytost = self.sytost + 3
                print(f"{self.jmeno} má ze sebe radost. Umazal se a utahal, dostal však pořádně najíst.")

    def koupat_se (self):
        # Doplní čistotu.
        print("Vyber číslo, co má dráček udělat:\n\t1 Zaplavat si v jezeře\n\t2 Vydrhnout si šupiny rejžákem")
        koupani = int(input())
        if koupani == 1:
            self.energie = self.energie -1
            self.cistota = self.cistota + 5
            self.stesti = self.stesti + 5
            print(f"{self.jmeno} se v jezeře náramně bavil. Teď se leskne na sluníčku, jak se vyhřívá na břehu.")
        elif koupani == 2:
            self.energie = self.energie - 4
            self.cistota = self.cistota + 10
            print("Dráčkovi to dalo pořádně zabrat. Ale vypucoval se důkladně.")
        else:
            print("Odpověď musí být číslo.")


    def akce (self):
        # Ovládací prvek celé hry. Ptá se hráče, co chce dělat, dokud je drak alespoň trochu zdravý.
        while self.zdravi > 10:
            print(f"\nCo má {self.jmeno} dělat?\n\t1 - Uložit hru\n\t2 - Ukázat statistiky\n\t3 - Jíst\n\t4 - Spát\n\t5 - Hrát si\n\t6 - Učit se\n\t7 Pracovat\n\t8 Vykoupat se")
            akce = int(input())
            if akce == 1:
                drak.ulozit()
            elif akce == 2:
                drak.vypsat()
            elif akce == 3:
                drak.jist()
            elif akce == 4:
                drak.spat()
            elif akce == 5:
                drak.hrat_si()
            elif akce == 6:
                drak.ucit_se()
            elif akce == 7:
                drak.pracovat()
            elif akce == 8:
                drak.koupat_se()
            else:
                print("Musíš napsat číslovku.")
        print("Draka odvezli ochránci magických tvorů.")

    def ulozit (self):
        # Uloží dračí hodnoty do textového souboru, aby se hráč mohl vrátit ke svému drakovi.
        with open("data.txt", "w", encoding="utf-8") as f:
            zapsat = []
            zapsat.append(f'{self.jmeno}\n')
            zapsat.append(f'{self.energie}\n')
            zapsat.append(f'{self.sytost}\n')
            zapsat.append(f'{self.stesti}\n')
            zapsat.append(f'{self.cistota}\n')
            zapsat.append(f'{self.zdravi}\n')
            zapsat.append(f'{self.reputace}\n')
            zapsat.append(f'{self.vzdelani}\n')
            f.writelines(zapsat)
            

"""
Umožňuje vybrat si novou nebo rozehranou hru. Nová má výchozí statistiky, rozehraná bere uložené hodnoty z prográmku hodnoty.py a ten pracuje s uloženými hodnotami načtenými z textového souboru. 
Po výběru hra pokračuje funkcí akce, která se opakuje, dokud drakovi neklesne zdraví na nulu.
"""

print("Hra, ve které se stanete majitelem dráčka. Dobře se o něj starejte, aby mu nic nescházelo.\nHra končí, pokud dráčkovi klesne zdraví na nulu.\nVyberte číslo:\n\t1 - Nová hra\n\t2 - Uložená hra")
hra = int(input())
if hra == 1:
    print("Stáváte se majitelem roztomilého dráčátka.\nJak se bude jmenovat?")
    drak = Drak(input(), 20, 15, 20, 20, 20, 15, 10)
elif hra == 2:
    drak = Drak(hodnoty.jmeno, hodnoty.energie, hodnoty.sytost, hodnoty.stesti, hodnoty.cistota, hodnoty.zdravi, hodnoty.reputace, hodnoty.vzdelani)
else:
    print("Odpověď musí být číslo.")
drak.akce()



