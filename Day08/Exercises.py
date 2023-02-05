#1
dog={}
#2
dog['name']="star"
dog['colour']="white"
dog['breed']="caucasian"
dog['legs']="long"
dog['ages']="5months"
print(dog)
#3
student={}
student['first_name']="Abdulkarim"
student['last_name']="Baba"
student['age']="21"
student['marital status']="Sinle"
student['skills']=["Excel","Python","Orion"]
student['country']="Nigeria"
student['city']="Kano"
student['address']={"No:. ":"53","LGA": "Tarauni", "Ward":"Limawa", "street": ["Maiduguri road", "behind NNPC depot" ]}
print (student)
#4
print ("the number of items in student dictionary is: " , len(student))
#5
print ("the data type of dictionary key \'skills\' is: ", type(student.get("skills")))
#6
student["skills"][0]="java"
print(" \'java\' was added to skills: ", student)
#7
print("list of dictionary keys: ", student.keys())
#8
print("list of dictionary values: ",student.values())
#9
print("tuple of dictionary items: ", student.items())
#10
del student["skills"][-1]
print("The last item in skills was deleted: ",student)
#11
del dog