#part 1
print("THIS IS PART ONE")
ages= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

print("The min age is",ages[0], "and ", "the max age is ",ages[-1])

ages.append(ages[0])
ages.append(ages[-2])
print(ages)

ages.sort()
print(ages)
length_of_ages=len(ages)
if length_of_ages%2==1:
    median=ages[length_of_ages//2]
    print("The median is ", median)
else:
    middle_1st=ages[length_of_ages//2]
    middle_2nd=ages[length_of_ages//2-1]
    median=(middle_1st+middle_2nd)/2
    print("The median is ", median)

average= sum(ages[0:])/length_of_ages
print("The average age is ", average)
min_age=ages[0]
max_age=ages[-1]
range=max_age - min_age
print(f"The range max({ages[-1]}) - min({ages[0]}) = ", range)

min_minus_average=abs(min_age - average)
max_minus_average=abs(max_age - average)
print ("Absolute values of (minimum minus averge) and (maximum minus average) equal? ",min_minus_average== max_minus_average)
print ("Absolute values of (minimum minus averge) less than or equal to (maximum minus average) ? ",min_minus_average <= max_minus_average)
print ("Absolute values of (minimum minus averge) greater than or equal to (maximum minus average) equal? ", min_minus_average >= max_minus_average)

# part 2
print() #for line spacing
print('THIS IS PART TWO')
#1
countries=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia','Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South','Kuwait','Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
   
num_of_countries=len(countries)
if num_of_countries % 2==1:
    middle_country=countries[num_of_countries//2]
    print("The middle country is ", middle_country)
else:
    first_middle_country=countries[num_of_countries//2-1]
    second_middle_country=countries[num_of_countries//2]
    middle_countries=   first_middle_country + "  and " + second_middle_country
    print("The middle countries are ", middle_countries)
    
#2
print()   # for line spacing
if num_of_countries%2==1:
    first_half=countries [0:(num_of_countries//2+1)]
    second_half=countries[num_of_countries//2+1:-1]
else:
    first_half=countries [0:(num_of_countries//2)]
    second_half=countries[num_of_countries//2:-1]

print() #This is for line spacing
print("The First Half Are: \n",first_half)

print() # for line spacing
print("The Second Half Are: \n",second_half)

#3
print() #this is for line spacing
new_countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rs, us, *scandic=new_countries
print(ch)
print(rs)
print(us)
