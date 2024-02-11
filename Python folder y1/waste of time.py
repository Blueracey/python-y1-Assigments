def Convert_unix_to_Years():
   del timeunix[0] #deletes the entry that just  says "unix time"
   
   count2=0
   time_Years = []
   time_weeks = [0]
   for row  in timeunix:
     time_Years.append(int(timeunix[count2])%31556926) #devides by  the amount of seconds in a year in order  to get the amount of second this  year

     count2=count2+1
   print(time_Years)
   Convert_unix_to_months(time_Years)
   


def Convert_unix_to_months(time_Years):
    count2=0
    time_Months = []
    for row in time_Years:

     time_Months.append(int(time_Years[count2])%2629743) #devided by amout of second in a month  in order to get the remaing  week time 
        
     count2=count2+1
    print(time_Months)
    Convert_unix_to_weeks(time_Months)

def Convert_unix_to_weeks(time_Months):
        count2=0
        time_weeks = []
        for row in time_Months:

         time_weeks.append(int(time_Months[count2])%604800) #devided by amout of second in a month  in order to get the remaing  week time 

         count2=count2+1
        print(time_weeks)
        Convert_unix_to_days(time_weeks)
        

def Convert_unix_to_days(time_weeks):
        count2=0
        time_days = []
        print(time_weeks)
        for row in time_weeks:

         time_days.append(int(time_weeks[count2])%86400) #devided by amout of second in a month  in order to get the remaing  week time 
         print(count2)
         count2=count2+1
        print(time_days)
        Convert_unix_to_months(time_days)
 


def Convert_unix_to_days(time_days):
        count2=
        time_hours = []
        for row in time_days:

         time_hours.append(int(time_days[count2])%3600) #devided by amout of second in a month  in order to get the remaing  week time 
         
         count2=count2+1
        print(time_hours)