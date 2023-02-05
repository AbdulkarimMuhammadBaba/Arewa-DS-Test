#1
print ("for loop")
for x in range(11):
    print(x)
x=0
print("while loop")
while x<11:
    print(x)
    x=x+1
#2
print("for loop")
for x in reversed(range(11)):
    print(x)
print("while loop")
x=0
while x<11:
    print(10-x)
    x=x+1
#3
x=0
while x<7:
    print('#'*x)
    x=x+1
#4
for x in range(1,9):
    print('#\t'*8)
#5
for x in range(0,11):
    print(f"{x} x {x} = {x*x}")
#6
list= ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in list:
    print(items)
#7
for x in range(101):
    if x%2==0:
        print(x)
#8
for x in range(101):
    if x%2==1:
        print(x)
