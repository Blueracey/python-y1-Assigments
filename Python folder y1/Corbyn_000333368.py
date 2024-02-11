

#Corbyn bromling 000333368


def Prompt_library_card():
 print("***********Springfield Library Catalog**********") 
 print("************************************************")
 library_max = 9999
 Library_min = 1000
 Loop = 0
 while Loop < 1:
     getNumber=int(input("Enter your Library card number(valid library card# is between 1000-9999)"))
     if getNumber >=Library_min and getNumber<=library_max:
            getSearchOptions()
            Loop +1





def getSearchOptions():  #asks for which search option user is looking  for, provides option to exit 
     #list, in the original order you gave but all in one so I can search it ISBN are all even, Titles are all odd 
    Library_info =["978-1-60309-502-0", "Animal Stories",  "978-1-60309-454-2", "Cosmoknights", "978-1-60309-513-6", "Doughnuts and Doom",  "978-1-60309-038-4", "Essex County",  "978-1-60309-015-5", "Johnny Boo: Twinkle Power",  "978-1-60309-041-4", "Johnny Boo: Happy Apples",  "978-1-60309-522-8"," Shelley Frankenstein!:CowPiggy",  "978-1-60309-384-2", "Johnny Boo: Goes Like This",  "978-1-60309-392-7", "The Underwater Welder",  "978-1-60309-491-7"," Monster on the Hill",  "978-1-60309-411-5", "Surfside Girls: The Mystery at the Old Rancho", "978-1-60309-499-3", "Secret Passages", ]

    print("1: Search by ISBN")
    print("2: Search by Title")
    print("3: Quit")   
    getSearchOption=int(input("Enter your choice"))


    if getSearchOption>=1 and getSearchOption<=1: #
        LookUpByISBN()
    elif getSearchOption>=2 and getSearchOption<=2:
        lookUpByTitle()
    elif getSearchOption>=3 and getSearchOption<=3:
        exit()

    
    
   
def LookUpByISBN(): 
     isbnoption = str(input("enter the book's ISBN(input with hyphens)")) #asks for the ISBN
     booktitle = Library_info.index(isbnoption) #finds where in the list the ISBN is 
     if (booktitle % 2) == 0:  #checks if it is actually an isbn all even numbers will be ISBN where book titles will be odd 
         print(Library_info[booktitle+1]) #reads off  the place ithe ISBN was in the array +1 to read the title 
     else: 
         print("error input was either not in the database or not a proper ISPN")  #error message, then sends you back to search options so so you have the choice  to exit 
         getSearchOptions()
     searchagain()

     


     
     
     

def lookUpByTitle():
     Tittlechoice = str(input("enter the book's name(Capatalize all words in tittle)")) #asks for the Tittle of the book you are looking   for 
     isbn = Library_info.index(Tittlechoice) #finds where in the list the titlte is 
     if (isbn % 2) == 0: #checks if its actually a tittle  all tittles will be odd 
         print("error input was either not in the database or not a proper  tittle") #error message, then sends you back to search options so so you have the choice  to exit 
         getSearchOptions()
     else: 
         print(Library_info[isbn-1]) #reads off  the ISBN because 
     searchagain()



def exit(): #message that thanks user to end the program
    "thank you for using springfield library"


def searchagain(): #asks if user wants  to search again, loops if they put  in an invalid imput 
    yesno  = str(input("Do you want to search again(Y or N)"))
    if yesno >="Y" and yesno<="Y" and yesno >="y"and yesno<="y" : # making  sure any form of y will work, there is most  certainly  a better way to do this but this works
        getSearchOptions()

    elif  yesno >="n" and yesno<="n" and yesno >="N" and yesno<="N": 
        exit()
    else :
        print("invalid input")
        searchagain()

Prompt_library_card() # one line!, calls the first  fuction 

