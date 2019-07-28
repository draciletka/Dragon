"""
Pomocný prográmek na čtení hodnot uložené hry a jejich následnou použitelnost v hlavním programu. 
"""

with open("data.txt", "r", encoding="utf-8") as f:
    seznam = []
    for radek in f.readlines():
        seznam.append(radek.strip())
    
jmeno = seznam[0]
energie = int(seznam[1])
sytost = int(seznam[2])
stesti = int(seznam[3])
cistota = int(seznam[4])
zdravi = int(seznam[5])
reputace = int(seznam[6])
vzdelani = int(seznam[7])

if __name__ == "__main__":
    print(seznam)


    




