it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
set_length=len( it_companies)
print("The length of the set it_companies is ",set_length)
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['WhatsApp', 'Instagram',  'chatGPT'])
print(it_companies)
#4
it_companies.remove('IBM')
print(it_companies)
#5
print("In remove, if an  item is not found it\n will raise an error while discard doesn't  raise an error\n e.g it_companies.remove(\"TikTok\") will raise an error while \n it_companies.discard(\"TikTok\") won't raise any error")
