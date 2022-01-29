import random

places = ["Asian", "Mexican", "Burgers", "Healthy", "pizza", "Wings/chicken"]
random1 = random.choice(places)
if random1 == "pizza":
    print(random1)
    pizza=["Pizza Hut", "Dominos", "Marcos Pizza", "Mr.Jims"]
    print(random.choice(pizza))
if random1 == "Burgers":
    print(random1)
    burgers = ["whataburger", "pops burger", "burger king", "in n out"]
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
    mexican = ["Tio Tony's", "287 Tacos", "La Salsa Verde", "Taco Bell", "Taco Casa", "On the boarder", "El Fenix"]
    print(random.choice(mexican))
if random1 == "Healthy":
    print(random1)
    healthy = ["Subway", "Solata", "Mod Pizza", "Jersey Mike's Subs"]
    print(random.choice(healthy))
else:
    print(random1)