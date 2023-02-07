import random
#1
def shuffled_list(array):
    return random.sample(array, len(array))
print(shuffled_list([0,5,6,6]))
#2
def seven_random():
    arr = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr
print(seven_random())