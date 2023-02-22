import re
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?''' 
sub=re.sub("[$?!?@?!?:?;?,?&?%?#?\??]","",sentence)
print (sub)
word=re.findall('[A-Za-z]+', sub)
words=set(word)
j=()
for i in words:
    z=len(re.findall(i, sub,re.I))
    j=(i,z)
    if z>=2:
       print (j)