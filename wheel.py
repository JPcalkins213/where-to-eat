import random

places = ["chicken express", "panda express", "taco casa", "taco bell", "whataburer", "kfc", "subway", "pizza", "slims chicken", "zaxby's", "in n out", "wingstop"]
random1 = random.choice(places)
if random1 == "pizza":
    pizz_places=["Pizza Hut", "Dominos", "Little Cesars", "Marcos Pizza", "Mr.Jims", "Jimmy's Pizza Pasta and subs"]
    print(random.choice(pizz_places))
else:
    print(random1)