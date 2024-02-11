days = 3
hours =8 
hourlyrate = 15.50
tips = 100 


basetime = days*hours
basepay = hourlyrate*basetime
tipspay = days*tips
totalpay = tipspay+basepay

print(totalpay)