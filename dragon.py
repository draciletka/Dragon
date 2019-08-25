import value

"""
The game where you become the Dragon keeper. Care it's needs carefully.
Game over if dragon's health drops to zero.
"""

class Dragon:
    
    # Dragon class
    def __init__ (self, name, energy, fullness, happiness, cleanness, health, reputation, education):
        self.name = name
        self.max_energy = energy
        self.energy = energy
        self.fullness = fullness
        self.max_happiness = happiness
        self.happiness = happiness
        self.max_cleanness = cleanness
        self.cleanness = cleanness
        self.max_health = health
        self.health = health
        self.reputation = reputation
        self.education = education

    def __str__ (self):
        # It writes out dragon's name.
        return self.name

    def vrite_out (self):
        # It writes out dragon's gaming values. 
        en = self.energy - 10
        ful = self.fullness - 10
        hap = self.happiness - 10
        cle = self.cleanness - 10
        he = self.health - 10
        rep = self.reputation - 10
        edu = self.education - 10  
        print(f"{self.name}\nenergy {en}\nfullness {ful}\nhappiness {hap}\ncleanness {cle}\nhealth {he}\nreputation {rep}\neducation {edu}")
        
    @property # attribute fatigue
    def exhausted (self):
        return self.energy < 4 

    @property # attribute hunger    
    def hungry (self):
        return self.fullness < 4

    def feeding (self): 
        """
        We can feed the dragon. Besides fullness another values can be changed dependind on kind of food.
        """
        print(f"What kind of food you choose for {self.name}?\nSelect number:\n\t1 Let graze in the park\n\t2 Neighbour's hen\n\t3 Chocolate\n\t4 Dragon's hot pancakes") 
        answer = int(input())
        if answer == 1:
            self.fullness = self.fullness + 8
            self.energy = self.energy - 5
            self.reputation = self.reputation - 4
            self.happiness = self.happiness - 5
            self.cleanness = self.cleanness - 5
            print(f"{self.name} filled up on dog keeper and his Great Dane in the park. It exhausted its. {self.name} is sad and dirty from this action. Visitors to the park seen it so it's reputation decreased.")
        elif answer == 2:
            self.fullness = self.fullness + 3
            self.energy = self.energy - 1
            self.reputation = self.reputation - 1
            self.happiness = self.happiness - 1
            self.cleanness = self.cleanness - 3
            print(f"{self.name} sneaked to neighbour's courtyard and ate a hen. The fight was noisy and brought neighbour. The dragon was little sad from it. It makes its dirtier.")
        elif answer == 3:
            self.fullness = self.fullness + 1
            self.energy = self.energy + 1
            self.happiness = self.happiness + 3
            self.cleanness = self.cleanness - 1
            print(f"{self.name} gobbled up chocolade. It made him smile of happiness on soiled mouth.")
        elif answer == 4:
            self.fullness = self.fullness + 5
            self.energy = self.energy - 3
            self.happiness = self.happiness + 5
            self.cleanness = self.cleanness - 2
            print(f"{self.name} polished off heaps by dragon hot pancakes. Dragon is dirty, happy and sleepy.")
        else:
            print("Answer must be a number.")
        dragon.vrite_out()

    def sleeping (self):
        """
        It refills dragon's energy. 
        """
        print("Select a number for kind of sleep:\n\t1 Nap behind the chimney\n\t2 Drowse in the fireplace")
        answer = int(input())
        if answer == 1:
            self.energie = self.energy + 3
            print(f"{self.name} napped.")
        elif aswer == 2:
            self.energie = self.energy + 10
            print(f"{self.name} slept many hours")
        else:
            print("Answer must be a number.")
        dragon.vrite_out()

    def play (self):
        """
        If it isn't hungry or exhausted, it can to play. It brings him happiness. Beware mischievous dragons!  
        """
        if self.hungry:
            print(f"{self.name} is hungry.")
        else:
            if self.exhausted:
                print(f"{self.name} is exhausted.")
            else:
                print("Select number for the kind of play:\n\t1 Set fire to dump past the town\n\t2 Running through the woods\n\t3 Put lego together")
                answer = int(input())
                if answer == 1:
                    self.energy = self.energy - 5
                    self.cleanness = self.cleanness - 5
                    self.reputation = self.reputation - 5
                    self.happiness = self.happiness + 3
                    print(f"{self.name} got dirty from the setting fire to dump past the town. Its reputation suffered. It's little happier and wearier.")
                elif answer == 2:
                    self.energy = self.energy - 2
                    self.happiness = self.happiness + 5
                    print(f"The woods gave {self.name} energy so it is from the running just a little weary and happy.")
                elif answer == 3:
                    self.energy = self.energy - 1
                    self.happiness = self.happiness + 5
                    self.education = self.education + 2
                    print(f"{self.name} is happy. Putting lego together does well. It trained it's brain.")
                else:
                    print("Answer must be a number.")
        dragon.vrite_out()
           

    def learn (self):
        """
        If it isn't exhausted, dragon can train it's brain.
        """
        if self.exhausted:
                print(f"{self.name} is exhausted.")
        else:
            print("Choose a number:\n\t1 Read\n\t2 Calculate")
            answer = int(input())
            if answer == 1:
                self.energy = self.energy - 1
                self.education = self.education + 3
                self.happiness = self.happiness + 1
                print(f"{self.name} is happier and more learned.")
            elif uceni == 2:
                self.energy = self.energy - 3
                self.education = self.education + 3
                self.happiness = self.happiness + 2
                print(f"{self.name} is exhausted and happy because it colved hard calculation.")
            else:
                print("Answer must be a number.")
        dragon.vrite_out()

    def work (self):
        # If it isn't hungry or exhausted, it can to work.
        if self.hungry:
            print(f"{self.name} is hungry.")
        else:
            if self.exhausted:
                print(f"{self.name} is exhausted.")
            else:
                print(f"Choose a number:\n\t1 To bring wood and light in the fireplace for old lady in the woods.")
                answer = int(input())
                if answer == 1:
                    self.energy = self.energy - 4
                    self.reputation = self.reputation + 2
                    self.cleanness = self.cleanness - 2
                    self.happiness = self.happiness + 2
                    self.fullness = self.fullness + 3
                    print(f"{self.name} is happy about itself. It is exhausted and more dirty but old lady gave it's big boar to eat.")
                else:
                    print("Answer must be a number.")
            dragon.vrite_out()

    def bath (self):
        # Increase cleanness.
        print("Choose a number:\n\t1 Swimming in the lake\n\t2 Scrub the scales")
        answer = int(input())
        if answer == 1:
            self.energy = self.energy -1
            self.cleanness = self.cleanness + 5
            self.stesti = self.stesti + 5
            print(f"{self.name} had fun in the lake. Now it is shinning in the sun.")
        elif answer == 2:
            self.energy = self.energy - 4
            self.cleanness = self.cleanness + 10
            print("It was hard work but with great result.")
        else:
            print("Answer must be a number.")

    def save (self):
        """
        It saves dragon's values into 'data.txt'.
        """
        with open("data.txt", "w", encoding="utf-8") as f:
            write = []
            write.append(f'{self.name}\n')
            write.append(f'{self.energy}\n')
            write.append(f'{self.fullness}\n')
            write.append(f'{self.happiness}\n')
            write.append(f'{self.cleanness}\n')
            write.append(f'{self.health}\n')
            write.append(f'{self.reputation}\n')                
            write.append(f'{self.education}\n')
            f.writelines(write)

    def action (self):
        """
        The whole game's control. It asks gamer what he wants to do until his dragon is at least little health. 
        """
        while self.health > 10:
            print(f"\nWhat {self.name} may to do?\n\t1 - Save game\n\t2 - Show statistics\n\t3 - Eat\n\t4 - Sleep\n\t5 - Play\n\t6 - Learn\n\t7 - Work\n\t8 - Take a bath\n\t9 - Exit\n")
            answer = int(input())
            if answer == 1:
                dragon.save()
            elif answer == 2:
                dragon.vrite_out()
            elif answer == 3:
                dragon.feeding()
            elif answer == 4:
                dragon.sleeping()
            elif answer == 5:
                dragon.play()
            elif answer == 6:
                dragon.learn()
            elif answer == 7:    
                dragon.work()
            elif answer == 8:
                dragon.bath()
            elif answer == 9:
                exit()
            else:
                print("Answer must be a number.")
        print("Dragon was saved by dragon rights activists.")


"""
Gamer can choose from new or saved game. New game has starting statistic, saved game brings saved statistics from module 'hodnoty.py' and it takes data from 'data.txt'   
After selection the game continues by function 'action' repeating until dragon's health isn't ten. 
"""
print("Select a number:\n\t1 - New game\n\t2 - Saved game")
answer = int(input())

if answer == 1:
    print("Write down dragon's name:")
    name = input()
    dragon = Dragon(name, 20, 15, 20, 20, 20, 15, 10)
   
elif answer == 2:
    dragon = Dragon(value.name, value.energy, value.fullness, value.happiness, value.cleanness, value.health, value.reputation, value.education)

dragon.action()
