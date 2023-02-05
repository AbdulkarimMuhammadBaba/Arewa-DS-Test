#1
empty_tuple=()
#2
sisters=("Maryam", "Fareedah", "Binta")
brothers=("Nura", "Abdul", "Fahad")
#3
siblings=sisters+brothers
#4
print(" I have ", len(siblings), "siblings")
#5
new_list=list(siblings)
new_list.insert(0,"Muhammad")
new_list.append("Amina")
family_members=tuple(new_list)
print(family_members)

