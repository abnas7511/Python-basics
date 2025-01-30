import datetime

today = datetime.date.today() #this will give you the current date and time

date = datetime.date(2020, 5, 17) #this will give you the date you want

print(date)
print(today)

time = datetime.time(10, 30, 0) #this will give you the time you want
print(time)

now = datetime.datetime.now() #this will give you the current date and time
now = now.strftime("%H:%M:%S %m/%d/%Y")
print(now)

target_datetime = datetime.datetime(2020,1,2,12,30,1)
curr_datetime = datetime.datetime.now()

if target_datetime < curr_datetime:
    print("The target date has passed")
else:
    print("The target date has not passed yet")

