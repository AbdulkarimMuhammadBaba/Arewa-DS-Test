#1
empty_list=[]
#2
list=["item1","item2","item3","item 4","item5","item6","item7"]
#3
print("The length of empty list is ",len(empty_list), "and", "length of list of items is ", len(list))
#4
print(list[::3])
#5
mixed_data_types=["Abdulkarim", 28, 1.78, "Single", "Tarauni Maiduguri Road Kano"]
#6
it_companies= [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7
print( mixed_data_types)
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[::3])
#10
it_companies[0]="Meta"
print(it_companies)
#11
it_companies.append("Binance")
print(it_companies)
#12
it_companies.insert(4,"Twitter")
print(it_companies)
#13
it_companies[4]="Twitter".upper()
print(it_companies)
#14
print("#; ".join(it_companies))
#15
print(it_companies.index("Google"))
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)
#18
print(it_companies[0:3])
#19
print(it_companies[-3:])
#20
middle_item=len(it_companies)//2
print(it_companies[middle_item])
#21
it_companies.pop(0)
print(it_companies)
#22
middle_item_1=len(it_companies)//2
middle_item_2= middle_item_1 - 1
it_companies.pop(middle_item_1)
it_companies.pop(middle_item_2)
print(it_companies)
#23
it_companies.pop()
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
#26
full_stack=front_end.copy()
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)