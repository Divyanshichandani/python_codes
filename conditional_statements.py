temp=30
if(temp<=40 and temp>=50):   #semicolon is used after IF and ELIF statements
    print("it is very hot")
elif(temp<=35 or temp>=20):
    print("it is mid today ")
elif(not temp==20):
    print("temperature can be predicted")
else:
    ('whatever the temperature is, i have to be there')

# write a weight conversion factor in python(two conditions kg or lbs or g)
weight=int(input('weight given'))
unit=(input('enter the units')) #no need of typecast here
if(unit=='kg'):
    weight= weight * 0.45
    print("weight in popunds",weight)
else:
    weight=weight/0.45
    print("weight in kg",weight)

#wap car automation(conditions:start stop quit help)
    while True:
    print("1:Start \n2:Stop \n3:Help \n4:Quit")
    a=int(input("Enter Choice: "))
    if a == 1:
        print("The car has started")
    elif a == 2:
        print("The car has stopped")
    elif a == 3:
        print("Start --> The car has started \nStop --> The car has stopped \nQuit -->Quit the game")
    elif a == 4:
        print("Thank you")
        break