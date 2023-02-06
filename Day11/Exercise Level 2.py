#1
def  evens_and_odds(num):
    lst=[]
    for i in range(1,num+1):
        if i%2==1:
            lst.append(i)
    x=len(lst)
    lsst=[]
    for j in range(num+1):
        if j%2==0:
            lsst.append(j)
    y=len(lsst)
    return f"the number of odds are {x} \nthe number of evens are {y}"
print(evens_and_odds(100))
#2
def factorial(num):
    if num!=0 and num!=1:
        n=num
        for n in range(1,n+1):
                for i in range(1,n):
                    n=n*i
    else:
        n=1 
    return f"n! = {n}"
print (factorial(4))
#3_01
def calculate_mean(list):
    mean=sum(list)/len(list)
    return mean
print("mean =", calculate_mean([1,3,5]))
#3_02
def calculate_median(list):
    list.sort()
    if len(list)%2==1:
        median=list[len(list)//2]
    else:
        median=(list([len(list)/2]) + list[len(list)/2-1])/2
    return median
print("median = ", calculate_mean([1,4,3,5])) # for even list len
print("median = ", calculate_mean([1,3,5])) # for odd list len
#3_03
def calculate_mode(list):
    list.sort()
    x=list[-1]
    return x
print("mode = ",calculate_mode([1,2,8,4,8,9,11,44,3,4]))
#3_04
def calculate_range(list):
    list.sort()
    x=list[-1]-list[0]
    return x
print("range = ",calculate_range([1,2,8,4,8,9,11,44,3,4]))
#3_04
def calculate_variance(list):
    sum_of_x=sum(list)
    square_of_sum_of_x=sum_of_x**2
    lst=[]
    for i in list:
        i=i**2
        lst.append(i)
    sum_of_square_of_x=sum(lst)
    variance=(sum_of_square_of_x - square_of_sum_of_x/len(list))/(len(list)-1)
    return variance
print("variance = ",calculate_variance([1,2,8,4,8,9,11,44,3,4]))
#3_05
def calculate_std(list):
    sum_of_x=sum(list)
    square_of_sum_of_x=sum_of_x**2
    lst=[]
    for i in list:
        i=i**2
        lst.append(i)
    sum_of_square_of_x=sum(lst)
    var=(sum_of_square_of_x - square_of_sum_of_x/len(list))/(len(list)-1)
    std=var**.5
    return std
print("standard deviation = ",calculate_std([1,2,8,4,8,9,1,2,5,11,44,11,55,3,4]))