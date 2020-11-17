import maincalcs
from maincalcs import kht
#cha con dex int str wis
#elf = ()


elf_dict = {
    "Speed": 30,
    "Darkvision": 60,
    "Skills": "Perception",
    "Languages": ("Common", "Elvish"),
}
elf_ai = [0,0,2,0,0,0]

elf_high_dict = {
    "Ability Increases": (0,0,0,1,0,0),
    "Proficiency": ("Longsword", "Shortsword", "Shortbow", "Longbow"),
    "Languages": ("One Extra"),
    "Spell": ("Cantrip", "Wizard"), #this might need to be dict
}
#if subrace != race, use subrace ((WHEN NOT STACKABLE))
#speed and darkvision do not stack

#("Ablility Increase", "Speed","Darkvision","Skills","Languages","Proficiency","Spells")
ability_scores = []
kht(ability_scores)

def elf_setup():
    print("Initial scores:", ability_scores)
    for i in range(5):
        ability_scores[i] += elf_ai[i]
    print("Ability scores with Racial Bonus:", ability_scores)



race = 'Elf'
if race == 'Elf':
    print('Race: Elf')
    elf_setup()