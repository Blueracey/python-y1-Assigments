
factor1 = int(input("Input largest number: "))   #A # asks for user input 
factor2s =  int(input("Input smaller number: "))  #B # asks for user input 
Result = 0 

def Eucldian_algoryth(factor1,factor2s):


  remainderanswer =  factor1%factor2s # finds the Remainder of the 2 numbers 

  factor1 = factor2s # changes the second number to the first 
  factor2s = remainderanswer #  Changes the second number to be the remainder 

  if  factor2s >= 1: # condition to stop the loop
    Eucldian_algoryth(factor1,factor2s) # Recall of the function 
  else :
    print("The GCF is " + str(factor1)) # output 


Eucldian_algoryth(factor1,factor2s) # call the recursive function 











