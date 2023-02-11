countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def upper (country):
    return country.upper()
def square (num):
    return num**2
#1
new_lst=list(map(upper, countries))
print (new_lst)
#2
new_num_lst=list(map(square, numbers))
print (new_num_lst)
#3
new_name_lst=list(map(upper,names))
print (new_name_lst)
#4
def country(cont_name):
    if "land" in cont_name:
        return False
    else:
        return True
countries_without_land=list(filter(country, countries))
print (countries_without_land)
#5
def six_letter(cont):
    if len(cont)==6:
        return True
    else:
        return False
cont_six_letters=list (filter (six_letter, countries))
print (cont_six_letters)
#6

def more_than_six_letter(cont):
    if len(cont)>=6:
        return True
    else:
        return False
cont_more_than_six_letters=list (filter (more_than_six_letter, countries))
print (cont_more_than_six_letters)
#7
def start(contr):
    if 'E' in contr[0]:
        return False
    else:
        return True
cont_not_starting_with_E=list (filter (start, countries))
print (cont_not_starting_with_E)
#8
print (list(filter(start, list(filter(six_letter, countries)))))
#9
def string (strs):
    return str(strs)
def strs_lst():
    return list(map(string, numbers))
print (strs_lst())
#10
from functools import reduce
def sum(x,y):
    return int(x)+int(y)
summation=reduce (sum,strs_lst())
print (summation)
#11
def sent(x,y):
    x="Estonia, Finland, Sweden, Denmark, Norway "
    y=="Iceland"
    return x," and ", y, " are North European countries"
  
sentence=reduce (sent, countries)
print (sentence)
#12
country_list=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia','Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South','Kuwait','Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
def categorise_countries(cont):
    if "land" in cont:
        return True
    else:
        return False
countries_with_land=list(filter (categorise_countries, country_list))
print ("countries with land: ",countries_with_land)
#13
keys = []
keys = [i[0] for i in country_list if i[0] not in keys]
def countCountry(c):
    return sum([True for i in country_list if i[0].startswith(c)])

vals = [len(keys) for key in country_list]

print(dict(zip(keys, vals)))
#14
def get_first_ten():
    return country_list[:10]
#15
def get_last_ten():
    return country_list[-1:-11:-1]