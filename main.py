import random
import funcs
import postgres_funcs
import aws_funcs
from funcs import *
from postgres_funcs import *
from aws_funcs import *

town = funcs.get_zipcode()
cat = input("would you like to choose a category? y or n: ")
cat.lower()
if cat == "y":
    category = funcs.get_category()
    category.lower()
    x, y = funcs.get_category_restaurants(category, town)
    place = random.choice(x)

    pIndex = x.index(place)

    addy = y[pIndex]

    print(place)

    print(addy)
    dataframe = postgres_funcs.add_data_to_postgres(x,y,category)
else:
    user_idea_question = input("Do you have some places in mind? y/n : ")
    user_idea_question.lower()
    if user_idea_question == "y":
        ammount = input("How many places do you have in mind? : ")
        x=1
        user_place = []
        while x <= ammount:
            user_place.append(input(f"place {x} : "))
            x+=1
        print(random.choice(user_place))
    exist = postgres_funcs.checking_postgres_existence(town)
    if exist == True:
        df = csv_to_df(town)
        random_from_df(df)
    else:
        x, y = funcs.get_restaurants(town)

        place = random.choice(x)

        pIndex = x.index(place)

        addy = y[pIndex]

        print(place)

        print(addy)
        dataframe = postgres_funcs.add_data_to_postgres(x,y,town)

    # x, y = funcs.get_restaurants(town)

    # place = random.choice(x)

    # pIndex = x.index(place)

    # addy = y[pIndex]

    # print(place)

    # print(addy)
    ### exist will need be moved farther up in the program so im not using google everytime

        # pgadmin = funcs.to_s3(dataframe, town)





















    # asian = ["Wongs Express", "Panda Express", "Adorianas"]
    # mexican = ["Tio Tony's", "287 Tacos", "La Salsa Verde", "Taco Bell", "Taco Casa", "On the boarder", "El Fenix"]
    # burgers = ["whataburger", "pops burger", "burger king", "in n out"]
    # healthy = ["Subway", "Solata", "Mod Pizza", "Jersey Mike's Subs"]
    # pizza= ["Pizza Hut", "Dominos", "Marcos Pizza", "Mr.Jims"]
    # wings = ["Zaxby's", "Wingstop", "Slims Chicken", "Canes", "chicken express", "chick fila", "Buffalo Wild Wings", "kfc"]
    # places = ["Asian", "Mexican", "Burgers", "Healthy", "pizza", "Wings/chicken"]



    # def user_picks():
    #     print("how many places do you have in mind?")
    #     choice_ammount = input("enter here: ")
    #     ammount = int(choice_ammount)insert you own[2]? ")
    # choice = input("1 or 2: ")
    # if choice == "2":
    #     user_picks()

    # else:
    #     print("Would you like to choose the category?")
    #     choice1 = input("yes or no: ")
    #     if choice1 == "yes":
    #         cat_pick()
    #     else:
    #         complete_random()
    #     x=1
    #     users_choices = list()
    #     while x<=ammount:
    #         adding = input("choice"+str(x)+ ": ")
    #         users_choices.append(adding)
    #         x+=1
    #     print(random.choice(users_choices)+" is my choice for you!")

    # def cat_pick():
    #     print("what category would you like?")
    #     choice2=input("Asian,  Mexican, Burgers, Healthy, Pizza, Wings/chicken?: ")
    #     if choice2 == "Asian" or choice2 == "asian":
    #             print(random.choice(asian))
    #     elif choice2 == "Mexican" or choice2 == "mexican":
    #             print(random.choice(mexican))
    #     elif choice2 == "Burgers" or choice2 == "burgers":
    #             print(random.choice(burgers))
    #     elif choice2 == "Healthy" or choice2 == "healthy":
    #             print(random.choice(healthy))
    #     elif choice2 == "Pizza" or choice2 == "pizza":
    #             print(random.choice(pizza))
    #     else:
    #             print(random.choice(wings))

    # def complete_random():
    #     random1 = random.choice(places)
    #     if random1 == places[4]:
    #             print(f'{random1}\n{random.choice(pizza)}')
    #     elif random1 == places[2]:
    #             print(f'{random1}\n{random.choice(burgers)}')
    #     elif random1 == places[5]:
    #             print(f'{random1}\n{random.choice(wings)}')
    #     elif random1 == places[0]:
    #             print(f'{random1}\n{random.choice(asian)}')
    #     elif random1 == places[1]:
    #             print(f'{random1}\n{random.choice(mexican)}')
    #     elif random1 == places[3]:
    #             print(f'{random1}\n{random.choice(healthy)}')


    # print("Would you like to pick a preset category [1]? or would you like to insert you own[2]? ")
    # choice = input("1 or 2: ")
    # if choice == "2":
    #     user_picks()

    # else:
    #     print("Would you like to choose the category?")
    #     choice1 = input("yes or no: ")
    #     if choice1 == "yes":
    #         cat_pick()
    #     else:
    #         complete_random()

