#
# * Core 134. Missed Classed

# 


#%%

# * Solution 1
def missedClasses(year: int, daysOfTheWeek: list, holidays: list):
    import datetime as dt

    count = 0
    for h in holidays:
        month = int(h.split('-')[0])
        if month < 9:
            hDate = dt.datetime.strptime((h+'-'+str(year+1)), '%m-%d-%Y')
        else:
            hDate = dt.datetime.strptime((h+'-'+str(year)), '%m-%d-%Y')
        # print(hDate)
        # print(hDate.weekday())
        if hDate.weekday()+1 in daysOfTheWeek:
            count +=1

    return count
 
    


y1 = 2015
d1 = [2, 3]
h1 = ["11-04", "02-22", "02-23", "03-07", "03-08", "05-09"]
r1 = missedClasses(y1, d1, h1)
print(r1)
