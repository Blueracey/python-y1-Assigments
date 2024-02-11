#this program is inconplte

# unfornately I ran out of time due to the fact that the wifi went out november 21 from 7-12 so if unfinished is an automatic fail I'll save your time
# I worked from 7 to 12 on this and I am so close, if I had had those 7 hours I think I could have made it.
# but sometimes life get's in the way, I am going to comment heavily and explain my though process across the unfinsihed 





import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import csv


root= tk.Tk()

paragraphs = []
Sentences = []
letters = []
paragraphcount = []
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
Wordstotal = []

width  = 800
height = 500
x = screen_width / 2
y = screen_height / 2

root.geometry("%dx%d+%d+%d" %(width, height, x, y))


def loadFileData(filename): # the second function to be called, does  all the file manipulation to fill my haklf a dozen lists
    file = open(filename) #opens the inputed file 
    content = file.read() #read the inputed file 

    for row in content.split() : # puts the paragraphs in seperate elements of a list 
        wordnumber = 1 # i do this alot as a redundecy 

        paragraphs.insert(wordnumber,(content.split('\n\n'))) # \n is a line break most paragraphs are two line breaks so it can be used as a divider.
     

    paragraphcount.insert(wordnumber,content.count('\n\n')) # /n represents a linebreak as above, thgough for a count it does mean thew first is not counted, this is added later in the anlysis function 


    for items in content.split() :# seperates every word orginaly intended to be used for total words and to count repeats but unfortunately I never made it there 
        wordnumber = 1 
        Wordstotal.insert(wordnumber,content.split())   
        break 
    for items in content.split() :
        wordnumber = 1 
        Sentences.insert(wordnumber,content.split(".")) # seperaters out each sentences by finding perios, not a perfect system but works well enough 
        break
    file.close() #save memory, thogh the rest of the proram is not great for that 
    return content
def processFile1(): # the first function called, it is called by the open button
    name = filedialog.askopenfilename() # opens the choose a file 
    text2.insert(END, loadFileData(name)) #insert into the second text box, I never endned up using  the first textbox. I would delete it but I think it's better to show fully where I got to  
   # also calls the other function, this function does the heavy lifting 
    Fileouter = open(name) #this might actually do nothing right now

    return Fileouter 
def analyze(): # the function called by the analyze button  also where nearly 20 hours of my life  went,    I wornder if I had just  gone to bed insteadf of working 12-2am when the wifi came back I would have had a better time
    paragraphcountmk2 = (paragraphcount[0]) # I needed to both add 1 to the paragraph count which started as a list and change it  to a string so it goes from mk1 to mk2 to mk3 
    paragraphcountmk3 =  paragraphcountmk2 +1 # add +1 to the amout in order to count the first paragraph which would not be counted due to how I'm counting 
    text3.insert(END, "# of paragraphs " + str(paragraphcountmk3)) 
    onparagraph=0 # this vcariabler was  being used for far too much and was the sourse of alot of my  problems, it is used to count which paragraph I am on in order to be able to check more then just the first, it is also used for the loop and is used inm the making of most of the variables of the function 
    while onparagraph < paragraphcountmk3 : #loops the whole thing greter  then the amout of paragraphs,

      countingwords = [] # used to store the current paragraph seperated into individual words, this is done towards the end of the loop, it is in the loop in order to reset it after every loop. 
      onparagraph = onparagraph + 1 #adding one each loop so that it will stop when it is over the amount of paragraphs 

      Currentparagraphstring = str(paragraphs[onparagraph])  # current parragraph turned  into a string so that I can count  it for the sentences total, for somereason paragraphs only has one paragraph in it,m I almost solved why when I ran out of time 
      
      Currentparagraph = (paragraphs[onparagraph]) 
      text3.insert(END, '\n' '\n' "Paragraph " + str(onparagraph) + ":") # inserts the paragraph number we are currently on into the text box, the only part after the intial paragraph that works 


      CurrentSentencecount=Currentparagraphstring.count(".")  # counts up the amount of sentences, does not go up due to the paragraphs issues 
            
      text3.insert(END,'\n' '\n' "# of sentences: " + str(CurrentSentencecount)) #inserts the  sentence total into the text box 

      for i in Currentparagraph: #suffers from the same problem fo paragraphs only having one paragraph in it 
           countingwords.append(i.split(" "))
           print(onparagraph)


           
           listlol = [len(x) for x in countingwords[0]] # a fix because the intial counting words is nested in the other two paragraphs, though I suppose that's not aproblem now that the other paragraphs disapeared 



           text3.insert(END, '\n' '\n' "# of words:  " + str(len(listlol))) #inserts into the text box, works as intended unlike the rest of this part of the function 

#alll the widgits, I meant to make them look better but I prioritized fuctionality, which in hindsight may have been a mistake  
entry1 = tk.Entry(root) 


text1=ScrolledText(root, height = 20, width= 50, )
text1.grid(row=3, column=3)
  

text2=ScrolledText(root, height = 20, width= 50)
text2.grid(row=6, column=3
)



text3=ScrolledText(root, height = 20, width= 50)
text3.grid(row=100, column=3
)



button1 = tk.Button(text='Open', command=processFile1)
button1.grid(row = 0 , column = 0 )

button2 = tk.Button(text='Analyze', command=analyze)
button2.grid(row = 5 , column = 0  )

root.mainloop()