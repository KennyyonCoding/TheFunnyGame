gamer = input("Hey what's your name?: ")
name = gamer.title()
gaming = name.replace(name[0], 'Ligm')
input(f"{gaming.title()}?! What an odd name?\nDo you like your name? ")
gama = input(f"Wait? {gaming} is not your name?!\nTell me your real name then: ")
troll1 = input(f"{gama}, huh, interesting name.\nAny way do you know who Candice is?: ")
if troll1.lower() == 'who':
    print('Candice ba   lls fit in yo mouth. Lmaoooo')
    exit()
troll2 = input(f"{troll1}?? That is not the answer.\nIt seems like you clearly don't know. Ask me who: ")
if troll2.lower() == 'who':
    print('Candice balls fit in yo mouth. Lmaoooo')
    exit()
word = 'who'
guess = ""
while guess.lower() != 'who':
    guess = input("A bit rebellious are we?\nTry again ask me who: ")
print('Candice balls fit in yo mouth!! Lmaooo')