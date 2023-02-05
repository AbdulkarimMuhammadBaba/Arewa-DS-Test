#1
age=input("Enter your age: ")
print("you are old enough to learn to drive") if int(age)>=18 else print("you need ",18-int(age), "more years to learn to drive") if int(age)<=18 else print()
#2
my_age=int(input('Enter your age: '))
your_age=int(input('Enter your age: '))
if my_age>your_age:
    print("I am older than you")
    if my_age-your_age==1:
          print("difference is ", 1,"year")
    else:
          print("difference is ", my_age-your_age, "years")
          
elif my_age<your_age:
      print("you are older than me")
      if your_age-my_age==1:
          print("difference is ", 1,"year")
      else:
          print("difference is ", your_age-my_age, "years")
else:
    print("my_age = your_age ")
#3
a=input("Enter number one: ")
b=input("Enter number two: ")
if a>b:
    print("a is greater than b ")
elif a<b:
    print("a is smaller than b")
else:
    print("a is equal to b")