#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i%2==0 and i>0])
#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list=[ number for row in list_of_lists for number in row]
print(flattened_list)
#3
lst_of_tuple=[(i,i** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11) ]
print(lst_of_tuple)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list_of_cont=[[cont[0].upper(), cont[0], cont[1].upper()] for con in countries for cont in con]
print(flattened_list_of_cont)
#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[country2[0].upper(), country2[1].upper()] for country in countries for country2 in country]
countries = [x for sub in countries for x in sub]
keys = ["country", "city"]
dictionary= [{keys[0]: countries[idx], keys[1]: countries[idx + 1]} for idx in range(0, len(countries), 2)]
print(dictionary)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_lst= [x for sub in names for sub2 in sub for x in sub2]
print([concatenated_lst[i] + ' ' + concatenated_lst[i + 1] for i in range(0, len(concatenated_lst), 2)])
#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(3,5,7,8))
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
print(y_intercept(3,6,8,1))