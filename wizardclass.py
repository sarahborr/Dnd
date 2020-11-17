#begining
'''
Skills: Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion

(a) a quarterstaff or (b) a dagger
(a) a component pouch or (b) an arcane focus
(a) a scholar’s pack or (b) an explorer’s pack
A spellbook

#school
spellcaster = True
'''
#equipment list of name and properties as string

equipment = {
    "Dagger": "1d4 Piercing",
    "Arcane Focus": "Used in place of material components",
    "Scholars Pack": "Writing supplies",
    "Spellbook": "What wizards use to learn Spells",
}

def wizard_choose():
    skills = input("Skills: Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion")
    equipment_chosen = input("(a) a quarterstaff or (b) a dagger \n (a) a component pouch or (b) an arcane focus \n (a) a scholar’s pack or (b) an explorer’s pack \n A spellbook")


wizard_choose()