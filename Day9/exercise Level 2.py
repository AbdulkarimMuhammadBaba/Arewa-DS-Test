#1
score=int(input("Enter student score: "))
if score>=0 and score<=49:
    print("F")
elif score<=59 and score>=50:
    print("D")
elif score<=69 and score>=60:
    print("C")
elif score>=70 and score<=79:
    print("B")
elif score>=80 and score<=100:
    print("A")
else:
    print("Wrong Entry")
#2
month=(input("Enter a month to check the season: "))
if month=="September":
    print("the season is Autumn")
elif month=="October":
       print("the season is Autumn")
elif month=="November":
    print("the season is Autumn")
elif month=="December":
    print("the season is Winter")
elif month=="January":
      print("the season is Autumn")
elif month=="February":
    print("the season is Winter")
elif month=="March":
    print("the season is Spring")
elif month=="April":
    print("the season is Spring")
elif month=="May":
    print("the season is Spring")
elif month=="June":
    print("the season is Summer")
elif month=="July":
    print("the season is Summer")
elif month=="August":
    print("the season is Summer")
else:
    print()
#3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input("Enter the name of new fruit: ")
if new_fruit in fruits:
    print("the fruit already exist in the list")
else:
    fruits.insert(0,new_fruit)
    print(fruits)