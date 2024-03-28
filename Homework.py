print("You are exploring a rainforest in search of treasure.")
print("Legend has it that there are some buried on a nearby island.")
choice = input("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait):")
if choice == "swim":
    print("You get eaten by a hungry shark. Game over.")
elif choice != "wait":
    print("GAME OVER. Should have listen to the rules")
else:
    print("A boat arrives and you arrive at the island safely.")
    choice = input("You come to a cave. Do you want to venture inside or walk on? (venture/walk):")
    if choice == "venture":
        print("You are squished by boulders never to be seen again. Game over. ")
    elif choice != "walk":
        print("GAME OVER. Should have listen to the rules")
    else:
        choice = input("You’re at a crossroads. Do you go left, right, or straight? (left/forwards/right):")
        if choice == "left":
            print("You are trampled by a herd of wildebeest. Game over.")
        elif choice == "forwards":
            print("You get stung by a poisonous wasp. Game over.")
        elif choice == "right":
             print("You march on and find the buried treasure! Yippee!!")
        else:
           print("GAME OVER. Should have listen to the rules")
