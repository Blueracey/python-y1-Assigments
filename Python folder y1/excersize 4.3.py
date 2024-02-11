list_of_numbers = []


sum = 0,0
for i  in range(0,5):
    list_of_numbers.insert(i,float(input("enter a decimal number")))
    sum=sum +list_of_numbers[i]

print(list_of_numbers)
print("total sum =",sum)\

average =  sum //i
print("average ="average)