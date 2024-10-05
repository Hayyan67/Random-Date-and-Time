import random
import time

def getrandomdate(start, end):
    print('Printing dates between ', start,'and',end,":")
    r1=random.random
    dateformate="%m/%d/%y"
    s1=time.mktime(time.strptime(start,dateformate))
    e1=time.mktime(time.strptime(end,dateformate))
    randomtime=time.s1+r1*(e1-s1)
    randomdate=time.strftime(dateformate,time,localtime(randomtime))
    return randomdate
getrandomdate("1/1/2024","12/31/2024")