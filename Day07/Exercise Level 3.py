ages= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#1
ages_set=set(ages)
print("list", ages)
print("Set", ages_set)
list_length=len(ages)
set_length=len(ages_set)
list_length_is_bigger=list_length>=set_length
if list_length_is_bigger==True:
    print ("The List length is Bigger")
else:
    print ("The Set length is Bigger")
#2
print ("String is a text or single str data type while list, \ntuple and set are all collection of different data types \nwhich might be a strings, integers, floats,\na sub_list, sub_tuple, sub_set or even a dictionary")
#3
sentence="I am a teacher and I love to inspire and teach people"
list=sentence.split()
print(list)
set=set(list)
print(set)
set.remove("I")
set.remove("and")
length_of_unique_words=len(set)
print("If unique words are words that appear only once; then their number is ", length_of_unique_words)