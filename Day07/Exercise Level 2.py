it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
C=A.union(B)
print (C)
#2
A_intersection_B=A.intersection(B)
print(A_intersection_B)
#3
is_A_subset_of_B=A.issubset(B)
print(is_A_subset_of_B)
#4
are_A_and_B_disjoint_sets=A.isdisjoint(B)
print(are_A_and_B_disjoint_sets)
#5
D=B.union(A)
print("Joining set A and B yields:  ", C, "\nwhile ", "Joining set B and A yields:  ", D)
#6
A_sym_difference_B=A.symmetric_difference(B)
print(A_sym_difference_B)
#7
del it_companies, A, B