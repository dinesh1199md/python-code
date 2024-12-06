import datetime

'''time '''
time_format=datetime.time(2,20,48,10)
#time(hour,min*,second,millisec)
print(time_format)

'''date '''
date_f=datetime.date(1999,11,14)
#date(year,month,day)
print(date_f)
print("day",date_f.day,"of month",date_f.month,"year",date_f.year)

'''date time'''
print(datetime.datetime.strptime('15/11/2000', '%d/%m/%Y'))