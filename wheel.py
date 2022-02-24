import random

asian = ["Wongs Express", "Panda Express", "Adorianas"]
mexican = ["Tio Tony's", "287 Tacos", "La Salsa Verde", "Taco Bell", "Taco Casa", "On the boarder", "El Fenix"]
burgers = ["whataburger", "pops burger", "burger king", "in n out"]
healthy = ["Subway", "Solata", "Mod Pizza", "Jersey Mike's Subs"]
pizza= ["Pizza Hut", "Dominos", "Marcos Pizza", "Mr.Jims"]
wings = ["Zaxby's", "Wingstop", "Slims Chicken", "Canes", "chicken express", "chick fila", "Buffalo Wild Wings", "kfc"]
places = ["Asian", "Mexican", "Burgers", "Healthy", "pizza", "Wings/chicken"]

print("Would you like to pick a preset category [1]? or would you like to insert you own[2]? ")
choice = input("1 or 2: ") 
if choice == "2":
    print("how many places do you have in mind?")
    choice_ammount = input("enter here: ")
    ammount = int(choice_ammount)
    x=1
    users_choices = list()
    while x<=ammount:
        adding = input("choice"+str(x)+ ": ")
        users_choices.append(adding)
        x+=1
    print(random.choice(users_choices)+" is my choice for you!")

else:
    print("Would you like to choose the category?")
    choice1 = input("yes or no: ")
    if choice1 == "yes":
        print("what category would you like?")
        choice2=input("Asian,  Mexican, Burgers, Healthy, Pizza, Wings/chicken?: ")
        if choice2 == "Asian" or choice2 == "asian":
            print(random.choice(asian))
        elif choice2 == "Mexican" or choice2 == "mexican":
            print(random.choice(mexican))
        elif choice2 == "Burgers" or choice2 == "burgers":
            print(random.choice(burgers))
        elif choice2 == "Healthy" or choice2 == "healthy":
            print(random.choice(healthy))
        elif choice2 == "Pizza" or choice2 == "pizza":
            print(random.choice(pizza))
        else:
            print(random.choice(wings))

    else:
        random1 = random.choice(places)
        if random1 == places[4]:
            print(f'{random1}\n{random.choice(pizza)}')
        elif random1 == places[2]:
            print(f'{random1}\n{random.choice(burgers)}')
        elif random1 == places[5]:
            print(f'{random1}\n{random.choice(wings)}')
        elif random1 == places[0]:
            print(f'{random1}\n{random.choice(asian)}')
        elif random1 == places[1]:
            print(f'{random1}\n{random.choice(mexican)}')
        elif random1 == places[3]:
            print(f'{random1}\n{random.choice(healthy)}')