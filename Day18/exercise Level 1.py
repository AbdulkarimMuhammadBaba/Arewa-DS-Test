import re 
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word=re.findall('[a-z]+', paragraph,re.I)
words=set(word)
j=()
for i in words:
    x=len(re.findall(i, paragraph))
    j=(x,i)
    print(j)
sentence='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between them two furthest particles.'
var=r'-?[0-9]+'
points=re.findall(var, sentence)
print("points: ",points)
lst=[]
for i in points:
    i=int(i)
    lst.append(i)
lst.sort()
print("sorted_points: ",lst)
print (f"distance {lst[-1]} - ({lst[0]}) = ", lst[-1]-lst[0])
