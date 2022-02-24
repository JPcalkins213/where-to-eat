import random

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
            asian = ["Wongs Express", "Panda Express", "Adorianas"]
            print(random.choice(asian))
        if choice2 == "Mexican" or choice2 == "mexican":
            mexican = ["Tio Tony's", "287 Tacos", "La Salsa Verde", "Taco Bell", "Taco Casa", "On the boarder", "El Fenix"]
            print(random.choice(mexican))
        if choice2 == "Burgers" or choice2 == "burgers":
            burgers = ["whataburger", "pops burger", "burger king", "in n out"]
            print(random.choice(burgers))
        if choice2 == "Healthy" or choice2 == "healthy":
            healthy = ["Subway", "Solata", "Mod Pizza", "Jersey Mike's Subs"]
            print(random.choice(healthy))
        if choice2 == "Pizza" or choice2 == "pizza":
            pizza=["Pizza Hut", "Dominos", "Marcos Pizza", "Mr.Jims"]
            print(random.choice(pizza))
        if choice2 == "wings" or choice2 == "chicken" or choice2 == "Wings" or choice2 == "Chicken" or choice2 == "wings/chicken" or choice2 == "Wings/Chicken":
            wings = ["Zaxby's", "Wingstop", "Slims Chicken", "Canes", "chicken express", "chick fila", "Buffalo Wild Wings", "kfc"]
            print(random.choice(wings))

    else:
        places = ["Asian", "Mexican", "Burgers", "Healthy", "pizza", "Wings/chicken"]
        random1 = random.choice(places)
        if random1 == "pizza":
            print(random1)
            pizza=["Pizza Hut", "Dominos", "Marcos Pizza", "Mr.Jims"]
            print(random.choice(pizza))
        if random1 == "Burgers":
            print(random1)
            burgers = ["whataburger", "pops burger", "burger king", "in n out",]
            print(random.choice(burgers))
        if random1 == "Wings/chicken":
            print(random1)
            wings = ["Zaxby's", "Wingstop", "Slims Chicken", "Canes", "chicken express", "chick fila", "Buffalo Wild Wings", "kfc"]
            print(random.choice(wings))
        if random1 == "Asian":
            print(random1)
            asian = ["Wongs Express", "Panda Express", "Adorianas"]
            print(random.choice(asian))
        if random1 == "Mexican":
            print(random1)
            mexican = ["Tio Tony's", "287 Tacos", "La Salsa Verde", "Taco Bell", "Taco Casa", "On the boarder", "El Fenix", "la tapitios", "Uncle Julios"]
            print(random.choice(mexican))
        if random1 == "Healthy":
            print(random1)
            healthy = ["Subway", "Solata", "Mod Pizza", "Jersey Mike's Subs"]
            print(random.choice(healthy))
        else:
            print("no food for you")