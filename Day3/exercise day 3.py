print ("Note!! All entries are numbers")
print () # this is for line spacing
# 1 
my_age=int(input("Enter your age as an integer: "))
# 2
print () # this is for line spacing
my_height=float(input("Enter your height as float: "))
#3
print () #: this is for line spacing
complex_num=complex (input ("enter a complex number:  "))
#4
print () # this is for line spacing
base=int(input("Enter base: "))
height=int(input ("Ente height: "))
print ("The area of triangle is ", (0.5*base*height))
#5
print() # this is for line spacing
a=int(input ("Enter Side a "))
b=int(input("Enter Side b "))
c=int(input ("Enter Side c "))
perimeter=a+b+c
print ("The Perimeter of the triangle is ", perimeter)
# 6
print() # this is for line spacing
length=int(input ("Enter length of triangle "))
width=int(input("Enter width of triangle  "))
its_area=length*width
its_perimeter=2*length + 2*width
print ("it area is ", its_area, "and", "it perimeter is ",its_perimeter)
# 7
print () # this is for line spacing
radius= int(input ("Enter the radius of circle "))
π=3.14
area=π*radius**2
print ("area = ", area, "and", "circumference = ", (2*π*radius))

#8
print () # this is for line spacing
import numpy as np
print ('''y= 2x - 2
at x = 0, y= -2
at y = 0, x = 1''')
x=[0, 1]
y=[-2, 0]
slope, y_intercept= np.polyfit(x, y, 1)
print ("slope", slope)
print("y-intercept ",round(y_intercept,0))
slope, x_intercept= np.polyfit(y, x, 1)
print ("x-intercept ", round(x_intercept,0))

#9
print () # this is line spacing
import math
x1, y1, x2, y2 = 2, 2, 6, 10
slope= (y2 - y1)/(x2-x1)
Euclidean_distance=math.sqrt((y2-y1)**2 + (x2-x1)**2)
print ("slope = ", slope, " and", "Euclidean distance = ", Euclidean_distance)

#10
print () # this is a line spacing
slope_task_8=2
slope_task_9=(y2 - y1)/(x2-x1)
print (slope_task_8 == slope_task_9)
print (slope_task_8 == slope_task_9 and slope_task_8 != slope_task_9)
print (slope_task_8 < slope_task_9)
print (slope_task_8 > slope_task_9)
print (slope_task_8 == slope_task_9)
print (slope_task_8 < slope_task_9 or slope_task_8 > slope_task_9)

#11
print () #this is for line spacing
for x in range(-5, 10):
    y=x**2 + 6*x + 9
    print ("@ x = ", x, "y is ", y)
print ("The value y is 0 @ x equal to -3")

#12
print () # this is for line spacing
print (len("python") != len("dragon"))

#13
print () # this for line spacing
print ("on" in "python" and "on" in "dragon")

#14
print () # this is for line spacing
print ("jargon" in "I hope this course is not full of jargon ")

#15
print () # this is for line spacing
print (not "on" in "python" and "dragon")

#16
print () # this is for line spacing
x=len("python")
print (float (x))
print (str(x))

#17
print () # this is for line spacing
x=int(input ("Enter the value of x "))
if x%2==0:
    print ("x is an even number")
else:
    print ("x is an odd number ")

#18
print () #this is for line spacing
print (7//3 == int(2.7))

#19
print () # this is for line spacing
print ('10' == 10)

#20
print () # this is for line spacing
print (int(9.8) == 10)

#21
print () # this is for line spacing
hour= int(input("Enter Hours: "))
rate_per_hour= int(input("Enter Rate Per Hour: "))
print ("Your Weekly Earning is ", hour * rate_per_hour)

#22
print() # this is for line spacing
years=int(input ("Enter the number of years you have lived "))
print ("You have lived ", years*365*24*60*60)

#23
print() # this is for line spacing
print("1\t1\t1\t1\t1")
print ("2\t1\t2\t4\t5")
print ("3\t1\t3\t9\t27")
print ("4\t1\t4\t16\t64")
print ("5\t1\t5\t25\t125")