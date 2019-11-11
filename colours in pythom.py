#=============================================================
swimming_1=int(input("please enter the time for swimming"))
cycling_1=int(input("please enter the time for cycling"))
running_1=int(input("please enter the time for running"))
print(swimming_1)
print(cycling_1)
print(running_1)

place=input("are you placed first or second")
print(place)

totalTime_1= swimming_1+cycling_1+running_1
print(totalTime_1)

if totalTime_1 <= 100 and place=="fisrt":
    print("totalTime_1")
    print("you recive Provincial colours")
elif totalTime_1 >= 110 and place ==("first or second"):
    print("totalTime_1")
    print("you recive provincial half colours")
elif totalTime_1 <= 115:
    print("totalTime_1")
    print("you receive a provincial scroll")
elif totalTime_1 <= 120:
    print("totalTime_1")
    print("you receive a provincial certificate")
else:
    print("totalTime_1")
    print("you do not receive an award")
#===============================================================
swimming_2=int(input("please enter the time swimming"))
cycling_2=int(input("please enter the time cycling"))
running_2=int(input("please enter the time running"))
print(swimming_2)
print(cycling_2)
print(running_2)
place=input("are you placed first or second")
print(place)
totalTime_2= swimming_2+cycling_2+running_2
print(totalTime_2)

if totalTime_2 <= 100 and place=="fisrt":
    print("totalTime_2")
    print("you recive Provincial colours")
elif totalTime_2 >= 110 and place== ("first or second"):
    print("totalTime_2")
    print("you recive provincial half colours")
elif totalTime_2 <= 115:
    print("totalTime_2")
    print("you receive a provincial scroll")
elif totalTime_2 <= 120:
    print("totalTime_2")
    print("you receive a provincial certificate")
else:
    print("totalTime_2")
    print("you do not receive an award")
#===============================================================
swimming_3=int(input("please enter the time for swimming"))
cycling_3=int(input("please enter the time for cycling"))
running_3=int(input("please enter the time for rinning"))
print(swimming_3)
print(cycling_3)
print(running_3)

totalTime_3= swimming_3+cycling_3+running_3
print(totalTime_3)

if totalTime_3 <= 100 and place ==("fisrt"):
    print("totalTime_3")
    print("you recive Provincial colours")
elif totalTime_3 >= 110 and place== ("first or second"):
    print("totalTime_3")
    print("you recive provincial half colours")
elif totalTime_3 <= 115:
    print("totalTime_3")
    print("you receive a provincial scroll")
elif totalTime_3 <= 120:
    print("totalTime_3")
    print("you receive a provincial certificate")
else:
    print("totalTime_3")
    print("you do not receive an award")
