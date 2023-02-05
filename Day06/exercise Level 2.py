#1
empty_tuple=()
sisters=("Maryam", "Fareedah", "Binta")
brothers=("Nura", "Abdul", "Fahad")
siblings=sisters+brothers
print(" I have ", len(siblings), "siblings")
new_list=list(siblings)
new_list.insert(0,"Muhammad")
new_list.append("Amina")
family_members=tuple(new_list)
print(family_members)
dad, sis1, sis2, sis3, bro1, bro2, bro3, mom = family_members
print(dad)
print(sis1)
print(sis2)
print(sis3)
print(bro1)
print(bro2)
print(bro3)
print(mom)
#2
print() # this is for line spacing
fruits=("Tangerine","Guava","Apple")
vegetables=("cabbage", "carrot","salad")
animal_products=("meat", "egg","milk")
food_stuff_tp=fruits+vegetables+animal_products

#3
food_stuff_list=list(food_stuff_tp)
print(food_stuff_list)
#4
print("Item at the centre is a ",food_stuff_list[int(len(food_stuff_list)/2)])
#5
print(food_stuff_list[0:3]+food_stuff_list[-4:-1])
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("meat" in nordic_countries)
print ("Iceland" in nordic_countries)

