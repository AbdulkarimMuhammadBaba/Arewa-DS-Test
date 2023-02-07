import random
#1
def shuffled_list(array):
    return random.sample(array, len(array))
print(shuffled_list([0,5,6,6]))
#2
def seven_random():
    ary = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in ary:
            arr.append(num)
            length = len(ary)
    return ary
print(seven_random())
