#Weight Converter app
#Convert  your weight to either pounds or kilos.

#This section gets the user's data

weight  = input("How much do you weigh?   ")
unit = input("(L)bs or (K)gs?   ")
#Pounds to kilos
if unit == "L":
    new_weight = int(weight) // 2.205
    print("Your weight in kilos is : ", str(new_weight))
#Kilos to pounds
if unit == "K":
    new_weight = int(weight) * 2.205
    print ("Your weight in pounds is:  ", str(new_weight))
