from datetime import *
now=datetime.now()
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second
timestamp=now.timestamp()
print (day)
print (hour)
print (minute)
print (second)
print (day, now.year, now.month)
print (f"timestamp: {timestamp}")
t=now.strftime("%d-%m-%y , %H:%M:%S")
print (t)
date_string="5 December, 2019"
date_object=datetime.strptime(date_string, "%d %B, %Y")
print (date_object)
new_year=date(day=1, month=1, year=2024)
today=date(day=20, month=2, year=2023)
the_difference_btw_now_n_new_year=new_year-today
print (f"the difference between now and new year is {the_difference_btw_now_n_new_year}")
dt="1 January, 1970"
t=datetime.strptime(dt, "%d %B, %Y")
dff=now-t
print (f'the difference between 1 January, 1970 and now is : {dff}')