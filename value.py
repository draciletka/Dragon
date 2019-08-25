""" 
This program loads saving data from 'data.txt' into 'dragon.py'.
"""

with open("data.txt", "r", encoding="utf-8") as f:
    value = []
    for line in f.readlines():
        value.append(line.strip())
    
name = value[0]
energy = int(value[1])
fullness = int(value[2])
happiness = int(value[3])
cleanness = int(value[4])
health = int(value[5])
reputation = int(value[6])
education = int(value[7])

if __name__ == "__main__":
    print(value)


    




