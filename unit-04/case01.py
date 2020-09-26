import datetime as dt
#
# today = dt.date.today()
# mybirthday = dt.date(today.year,9,24)
#
# if mybirthday < today:
#     mybirthday = mybirthday.replace(year= today.year+1)
#
# time2birthday = abs(mybirthday - today)
# print(time2birthday)
t1 = dt.datetime.now().time()
# help(dt)

date1 = dt.date(year = 2020, month = 12, day = 23)
print(date1)
t2 = dt.datetime.now().time()
time1 = dt.time(t2.hour,t2.minute, t2.second)
ordianl = date1.toordinal()
date2 = dt.date.fromordinal(ordianl)
print(ordianl, date2)
date2 = dt.datetime.today().date()
print(date2)
print(dt.date.fromisoformat(str(date2)))
print(dt.date.fromordinal(767890))
print(dt.date.fromtimestamp(dt.datetime.now().timestamp()))

