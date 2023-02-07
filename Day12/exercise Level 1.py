import random
import string
x=string.ascii_letters+string.digits
lst=[]
lst[:0]=x
#1
def random_user_id():
    y=' '
    for i in range(6):
        y+=random.choice(lst)
    return y
print(random_user_id())
#2
def user_id_gen_by_user():
    y=int(input("Enter the number of characters in user ID: "))
    x=int(input("Enter the number of user  ID to be generated: "))
    for i in range(x):
        z=" ".join([random.choice(lst) for i in range(y)])
        print(z)
    return ' '
print(user_id_gen_by_user())
#3
def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
print(rgb_color_gen())