#1:  Examples of different python datatypes 
print(type(2))
print(type(2.5))
print(type(2+5j))
print(type('Arewa Data Science'))
print(type(2>1))
print(type(['boys', 12, str(12), 'goals']))
print(type(('boys', 12, str(12), 'goals')))
print(type({'boys', 12, str(12), 'goals'}))
print(type({'boys':12, str(12):'goals'}))

print() #This is for empty line

# 2: Finding Euclidean distance
import math
print("Given that point1 = (2,3) and point2 = (10,8)")
point1=(2,3)
point2=(10,8)
euclidean_dist=math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1]))
print("The Euclidean Distance between point 1&2 is:", euclidean_dist)