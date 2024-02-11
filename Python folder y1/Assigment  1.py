Firstname = str(input("Employee full Name"))
Lastname = str(input("Employee full Name"))
production_this_year = int(input("type total Production"))
Production_last_year = int(input("type total Production  last year"))

print(Firstname+" "+Lastname)
if production_this_year > Production_last_year:
        print("congrats this employee exceeded last years production")
        if production_this_year >6001:
                print("the employee earned a 200$ bonus")
        elif production_this_year >3001: 
               print("the employee earned a 100$ bonus")
        elif production_this_year >1000: 
               print("the employee earned a 50$ bonus")
        elif production_this_year >1000: 
               print("the employee earned a 25$ bonus")
else: 
       print("Employee did not  exceed last years output")