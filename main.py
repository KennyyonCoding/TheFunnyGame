beginning = input('Type "balls" to start. When given instructions type any words to proceed.\n>')
if beginning.lower() == 'balls':
    gamer = input("\nWelcome to the best game ever!\nStart by entering your name: ")
    hostage = input(f"\nAllrighty {gamer.title()}, you are currently a hostage in Alpha Omega! Anything to say?\n>")
    ack_know = input(f"{hostage.upper()}? huh. I guess we continue. \n\nA suspicious bearded guy has"
          f" unleashed his fury on everyone. He is on a rampage! Your thoughts?\n>")
    act_th = input(f"{ack_know.title()} indeed! Look you have few choices here. "
          f"\nYou gotta type the words:\n\nRun - to attempt to exit the building"
          f"\nFight - to chuck a left hook\nCry - to cry\n> ")

    if act_th.lower() == "run":
        print(f"\nYou try running away, but the bearded guy senses you with his bear tingles.\n"
              f"His beard grabs your legs and breaks it and yells:"
              f"'{gamer.upper()} more like {gamer.replace(gamer[0], 'Pussy')}'\n"
              f"You die of blood loss. GG You lost!")
        exit()

    if act_th.lower() == "cry":
        cry = input(f"You stay on the ground, crying out loud. The bearded guy hears you. "
                    f"\n'{gamer.upper()}! stop being a pussy' yells out your friend.\n"
                    f"Yes/No --> Stop Crying?\n>")
        if cry.lower() == "yes":
            print("You wipe the tears off your face, but it's too late.\n"
                  "The bearded guy charges towards you with his beard and wraps it around your nose and mouth.\n"
                  "You can't breathe and die. GG. You lost! ")
            exit()
        if cry.lower() == "no":
            print(f'WAAHHH!!!!, you keep crying. "STFU {gamer.upper()}" yells out your friend!\n'
                  f'It is too late. Bearded guy swings his sharp beard. It hits your eye.\n'
                  f'You become blind and die. GG! You lost!')
            exit()
        else:
            print("Literally, you can't even type the word 'Yes' or 'No'. Disgraceful. GG. You lost!")

    if act_th.lower() == "fight":
        violence = input(f"\nYou. Mr. {gamer.upper()}! walk up to the bearded fellow and try giving him a left hook!\n"
                         f"- But he dodges!!!\n"
                         f"Yes/No --> Giving him another hook?"
                         f"\n> ")
        if violence.lower() == "yes":
            print(f"\nYou get his nose this time! He gets K tf O'ed.\n"
                  f"{gamer.title()}, today you became the hero. Game over")
            exit()
        if violence.lower() == "no":
            print(f"\nHe charges towards you with his beard and wraps it around your nose and mouth.\n"
                  f"You pass away from suffocation. GG. You lost! ")
            exit()
        else:
            print("Literally, you can't even type the word 'Yes' or 'No'. Disgraceful. GG. You lost!")

else:
    print("Game is already over lol. Should've typed 'help'.")