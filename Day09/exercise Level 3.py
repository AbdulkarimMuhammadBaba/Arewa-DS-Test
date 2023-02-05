person={'first_name': 'Asabeneh','last_name':'Yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True,'skills': ['JavaScript' ,'React', 'Node', 'MongoDB', 'Python'], 'address': {'street': 'Space street','zipcode': '02210'}}
#first check
if "skills" in person and len(person["skills"])%2==1:
        middle_skill=person["skills"][len(person["skills"])//2]
        print("the middle skill is: ", middle_skill)
else:
            middle1=person["skills"][len(person["skills"])//2]
            middle2=person["skills"][len(person["skills"])//2-1]
            print("the middle skills are: ", middle1, " and ", middle2)
            
#second check
if  "skills" in person:
    print("Python" in person["skills"],)
else:
    print("no python skills")
#section
input
if len(person["skills"])==2:
      if "JavaScript" and "React" in person["skills"]:
          print("he is a frontend developer")
      else:
         print("he has more skills")
if "Node" and "Python" and "MongoDB" in person["skills"]:
    print ("he is a backend developer")
    if  "React" and "Node" and "MongoDB" in person["skills"]:
        print ("he is a fullstack developer")
else:
     print("unknown title")
#section
if person["is_marred"]==True:
    if person["country"]=="Finland":
       print(person["first_name"], person["last_name"], " lives in ", person["country"],". He is married")