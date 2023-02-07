import random
#1
def list_of_hexa_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(many):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes
print(list_of_hexa_colors(many=0))
#2
def list_of_rgb_colors(many=0):
   def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b =str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
    if many == 0:
        many = random.randint(1, 10)
    rgbs = []
    for _ in range(many):
        rgbs.append(rgb_color_gen())
    return rgbs
print(list_of_rgb_colors(many=0))
#3
def generate_colors(col_type,many):
    if col_type == 'hexa':
        return list_of_hexa_colors(many)
    elif col_type == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"
print(generate_colors("hexa",0))