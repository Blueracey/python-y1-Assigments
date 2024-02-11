#Defines the function (fib) which computes the fibonacci numbers recursively (positive int)
def fib(n):
    if n <= 0:                   #checks if n is greater than or equal to zero in which it will return none as it has not met the criteria for being calculated
        return None
    elif n == 1 or n == 2:   #checks for the base case of the fibonacci sequence 
        return 1
    else:
        return fib(n - 1) + fib(n - 2)      #checks if n is greater than 1, in which case it will go ahead and compute the previous fib numbers until it reaches its conclusion
    
n = int(input("Please input a positive int: "))
result = fib(n)
if result is not None:                        #if th result is not none aka a positive int then it will return the Fib number and the result
    print("Fibonacci Number", n, "Is:", result)
else:
    print("Please Input a Positive Int.")     #is tied to the none response/invalid response to entering a positive int
