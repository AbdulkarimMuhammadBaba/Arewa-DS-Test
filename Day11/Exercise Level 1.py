#1
def add_two_numbers(par1,par2):
    sum=par1+par2
    return sum
print(add_two_numbers(2,2))
#2
def area_of_circle(r):
    π=3.14
    area=π*r*r
    print("The area of circle = ",area)
area_of_circle(7)
#3
def add_all_nums(*args):
    sum=0
    for arg in args:
        sum+=arg
    return sum
print(add_all_nums(3,4,6,6,85,4,4))
#4
def convert_celsius_to_fahrenheit(C):
    F = (C * 9/5) + 32
    print("the temperature in Fahrenheit is: ", F,"F")
convert_celsius_to_fahrenheit(50)
#5
def check_season(month):
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
check_season("July")
#6
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print("The slope is: ",calculate_slope(2,3,5,7))
#7
def solve_quadratic_eqn(a,b,c):
    x3=(b**2-4*a*c)**(.5)
    x1=(-b+x3)/2*a
    x2=(-b-x3)/2*a
    return x1, x2
print("The roots are: ",solve_quadratic_eqn(1,2,1))
#8
def print_list(*par):
    lst=[]
    for i in par:
        lst.append(i)
    return lst
print(print_list("books","boys","kings","arewa"))
#9
def reverse_list(par):
    lst=par
    for i in lst:
        lst.reverse()
    return lst
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A","B","C"]))
#10
def capitalize_list_items(par):
    lst=[]
    for i in par:
        lst.append(i.upper())
    return lst
print(capitalize_list_items(["i am a hero","Aren't i?",'12',"Can't you respond"]))
#11
def add_item(list,item):
    lst=list
    lst.append(item)
    return lst
print(add_item(["orange","banana"],"tangerine"))
#12
def remove_item(list,item):
    lst=list
    lst.remove(item)
    return lst
print(remove_item(["boys","girls","men"],"men"))
#13
def sum_of_numbers(num):
    sum=0
    for i in range(num):
        sum=sum+i
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100)) 
#14
def sum_of_odds(num):
    sum=0
    for i in range(num):
        if i%2==1:
            sum=sum+i
    print(f"the sum of odd numbers in the range of {num} is: ",sum)
sum_of_odds(5)
#15
def sum_of_evens(num):
    sum=0
    for i in range(num):
        if i%2==0:
            sum=sum+i
    print(f"the sum of even numbers in the range of {num} is: ",sum)
sum_of_evens(5)