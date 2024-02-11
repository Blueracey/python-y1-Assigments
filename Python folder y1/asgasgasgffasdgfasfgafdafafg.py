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


width  = 800
height = 500
x = screen_width / 2
y = screen_height / 2

root.geometry("%dx%d+%d+%d" %(width, height, x, y))


def loadFileData(filename):
    file = open(filename)
    content = file.read()

    for row in content.split() :
        wordnumber = 1 
        print(content) 
        print('\n' '\n')
        paragraphs.insert(wordnumber,(content.split('\n\n')))
        break
    paragraphcount.insert(wordnumber,content.count('\n'))
    print(paragraphs)

    for items in content.split() :
        wordnumber = 1 
        Sentences.insert(wordnumber,content.split())
        break
    for items in content.split() :
        wordnumber = 1 
        Sentences.insert(wordnumber,content.split("."))
        break
    file.close()
    return content
    
   


def processFile1():
    name = filedialog.askopenfilename()
    text2.insert(END, loadFileData(name))
    Fileouter = open(name)

    return Fileouter




entry1 = tk.Entry(root) 


text1=ScrolledText(root, height = 20, width= 50, )
text1.grid(row=3, column=3)
  

text2=ScrolledText(root, height = 20, width= 50)
text2.grid(row=6, column=3
)



text3=ScrolledText(root, height = 20, width= 50)
text3.grid(row=100, column=3
)



def analyze():
    paragraphcountmk2 = str(paragraphcount[0])
    text3.insert(END, "# of paragraphs " + paragraphcountmk2)
    onparagraph=0
    for i in paragraphs:    
           countingwords = []
           onparagraph = onparagraph + 1

           Currentparagraphstring = str(paragraphs[onparagraph-1]) 
           Currentparagraph = (paragraphs[onparagraph-1]) 
           text3.insert(END, '\n' '\n' "Paragraph " + str(onparagraph) + ":")

           
           CurrentSentencecount=Currentparagraphstring.count(".") 
            
           text3.insert(END,'\n' '\n' "# of sentences: " + str(CurrentSentencecount))
           currentword = 0
           while currentword < Currentparagraph.count(" ") :
             countingwords.append(i.split()[currentword])
             currentword=currentword+1
             print(countingwords)

           text3.insert(END, '\n' '\n' "# of words:  " + str(len(countingwords)))






button1 = tk.Button(text='Open', command=processFile1)
button1.grid(row = 0 , column = 0 )

button2 = tk.Button(text='Analyze', command=analyze)
button2.grid(row = 5 , column = 0  )

root.mainloop()