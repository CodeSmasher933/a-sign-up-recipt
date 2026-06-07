#sign up for spotless auto repair and service
customername= input("Enter your name:")
phonenum=input("Enter your number:")
caryr= input ("Enter the year of your car production:")
carmodel= input("Enter your car model:")
damagedpart = input ("Enter your car damaged part:")
print (" we will get back to you as soon as we can. Thanks for trying spotless auto repair and service")
repaircost=input("Enter estimated repair cost")
if damagedpart == "engine":
    print("Engine repair usually takes longer")
elif damagedpart == "tyres":
    print("tyre repair takes a few time")
elif damagedpart == "brakes":
    print("brakes repair are important and we will contact fast")
else:
    print("we will inspect the damaged part")

print("\n -------REPAIR REQUEST------------")
print("name:",customername)
print(" phone number:",phonenum)
print("car model:",carmodel)
print("car year of production:", caryr)
print("car damaged part:", damagedpart)
print("car repair cost:", repaircost)
print("\n we will get back to you as soon as we can")
print("Thanks for trying spotless")