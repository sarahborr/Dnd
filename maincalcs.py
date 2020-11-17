import random
'''
sel_race = input("Races:")
sel_class_a = input("Class")
sel_lvl = input("level")
money = input('money')
'''

'''
store info for races/classes

'''
races = ['Human', 'Elf', 'Dwarf']
classes = ['Wizard', 'Barbarian', 'Bard']



ability_scores = []
###
#character rolls
###
#8-18
'''
randchar = [ ]
for i in range(6):
    ability_scores.append(random.randint(8,18))
    ability_scores.sort()
'''
def kht(ability_scores): 
    #4d6kh3
    for i in range(6):
        listy = []
        value = 0
        for i in range(4):
            rand_num_six = random.randint(1,6)
            listy.append(rand_num_six)
            value += rand_num_six
        listy.sort()
        value -= listy[0]
        listy.remove(listy[0])
        ability_scores.append(value)


'''
def elf_setup():
    for i in range(6):
        ability_scores[i] += elf_dict["Ability Increases"][i]
    print("Ability scores:", player_ability_score)
    print("TEST")


race = 'Elf'
if race == 'Elf':
    print('Elfyyy')
    elf_setup()
    #get info from elf.py
    #return info here from race
'''
#("Ablility Increase", "Speed","Darkvision","Skills","Languages","Proficiency","Spells", "Resistance", "Other")