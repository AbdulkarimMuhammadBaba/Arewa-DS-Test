# Day 2: 30 Days of python programming
first_name= input ("first name: ")
last_name= input ("last name: ")
full_name= first_name + " "+ last_name
country= input ("country: ")
city="Tarauni"
age=input ("age: ")
year=1995
is_married="no"
is_true="yes"
is_light="yes"
#multiline variable
first_name, last_name, full_name, country, city, age, year, is_married,  is_true,
is_light = "Abdulkarim", "Baba", first_name + " "+ last_name, "Nigeria", "Tarauni", 27, 1995, "no", "yes", "yes"

# 1
print () # for line spacing
print(type(first_name))
print(type (last_name))
print(type(full_name))
print(type (country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

# 2
print () # for line spacing
print ("the length of my first name is :", len(first_name))

# 3
print () # for line spacing
print (len(first_name)>=len(last_name))
print (len(first_name)<=len(last_name))

# 4
print () # for line spacing
num_one=5
num_two=2

# (i)
total= num_one + num_two
print ("total= ", total)
# (ii)
diff = num_one - num_two
print ("diff = ", diff)
#(iii)
product = num_one * num_two
print ("product = ", product)
#(iv)
division = num_one / num_two
print ("division = ", division)
#(v)
remainder = num_one % num_two
print ("remainder =", remainder)
#(vi)
exp = num_one ** num_two
print ("exponential =", exp)
#(vii)
floor_division = num_one // num_two
print ("floor_division =", floor_division)

# 5
print () # for line spacing
r= 30
π = float(3.14)

# (i)
area_of_circle= π*r**2
print ("the area of circle is: ", area_of_circle,"square meters")

#(ii)
print () # for line spacing
circumference_of_circle=2*π*r
print ("the circumference of circle is: ", circumference_of_circle, "meters")

#(iii)
print () # for line spacing
area = π*int((input ("what is the radius of circle?")))**2
print ("the area is: ", area,"square meters")

# 6 refer to line 1, 2, 5 and 7

# 7
help("zip")
