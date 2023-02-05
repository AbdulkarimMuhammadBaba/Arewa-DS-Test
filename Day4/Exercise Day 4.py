#1
Thirty, Days, Of, Python= 'Thirty ', 'Days ', 'Of ', 'Python '
print(Thirty + Days + Of + Python)
#2
Coding, For, All='Coding ', 'For ' , 'All '
print (Coding + For + All)
#3
company="Coding For All"
#4
print(company)
#5
print(len(company))
#6
print (company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company [0:7])
#10
print(company.find('Coding'))
print(company.index("Coding"))
print(company.rfind('Coding'))
print(company.rindex("Coding"))
#11
print(company.replace("Coding", "Python"))
#12
Python_For_All=company.replace("Coding", "Python")
print(Python_For_All.replace("All","Everyone"))
#13
print (company.split())
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))
#15
print(company [0])
#16
print(company [-1])
#17
print(company [10])
#18
Python_For_Everyone=Python_For_All.replace("All", "Everyone")
PFE=Python_For_Everyone[0]+ Python_For_Everyone[7]+ Python_For_Everyone[11]
print (PFE.strip())
#19
CFA=company[0]+company [7]+company [11]
print (CFA.strip())
#20
print(company.index("C"))
#21
print(company.index("F"))
#22
coding_for_all_people=company + "People"
print(coding_for_all_people.rfind("l"))
#23
print ( 'You cannot end a sentence with because because because is a conjunction'.find("because"))
#24
print ( 'You cannot end a sentence with because because because is a conjunction'.rindex("because"))
#25
print ( 'You cannot end a sentence with because because because is a conjunction'[31:-17])
#26
print ("You cannot end a sentence with because because because is a conjunction".find("because"))
#27
print ( 'You cannot end a sentence with because because because is a conjunction'[31:-17])
#28
print (company.startswith("Coding"))
#29
print (company.endswith("Coding"))
#30
print ('   Coding For All      '.strip())
#31
print ("thirty_days_of_python". isidentifier ())
#32
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))
#33
print ("I am enjoying this challenge. \nI just wonder what is next.")
#34
print ("Name      \tAge     \tCountry   \tCity \nAsabeneh  \t250     \tFinland   \tHelsinki")
#35
radius = 10
area = 3.14 * radius ** 2
print (f"The area of a circle with radius {radius} is {area} meters ")
#36
a=8
b=6
print (f"{a} + {b} = {a+b}")
print (f"{a} - {b} = {a+b}")
print (f"{a}*{b} = {a*b}")
print (f"{a}/{b} = {a/b}")
print (f"{a}%{b} = {a%b}")
print (f"{a}//{b} = {a//b}")
print (f"{a}**{b} = {a**b}")