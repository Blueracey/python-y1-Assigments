#Corbyn bromling #000333368



import tkinter as tk
from pathlib import Path
import csv
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *


# the project is not finished to the level I would like but I spent alot of time trying to convert unix time to hours instead of using my time to build more graphs
# I learnt alot of this project and more that I did not even use in the final product 






folder_location = Path("InfoFP")
Gui = Tk()
screen_width = Gui.winfo_screenwidth()
screen_height = Gui.winfo_screenheight()


# all the global variables used 
Temperature = []
time = []
test = []
width  = 1600
height = 1000
x = screen_width / 2
y = screen_height / 2
windspeed = []
Gui.geometry("%dx%d+%d+%d" %(width, height, x, y))




def Open_txt(): #opens  the text file and  returns it to the varaible 
    text_file = open(folder_location / 'weatherstats_grandeprairie_hourly_Cleaned.csv')

    return text_file 

def Break_By_Line():
  

    read = csv.reader(text_file) #takes the variable open text 

    count = 0 # count for the variable 

    for row in read:
     
     if(len(row) != 0 ): # makes sure the loop does not repeat more times then there is information 
        time.append(row[0][11:13])  # takes the 11,12 and 13th character of the string to be sued for the time in the 24 hour period 
        Temperature.append((row[10])[1:]) # removes the negative sign because it is  not graphable and they are all negative sofor demostrating just change it is the smae 
        windspeed.append((row[6]))
        count = count + 1 


    
    
    print (windspeed)








class GFG: # controls all of the UI 
    def __init__(self, Gui = None):

        self.Gui = Gui
 

        self.Create()
    
    def Create(self):


     self.canvas = tk.Canvas(self.Gui , bg = "grey" , height = 700 , width = 700 )#produces the actual canvas evertyhing is made on 
     #def do_zoom(event,self):
     

      #self.canvas.scale(ALL, 1, 1, 2, 2)  failed attept to allowing zooming, left here just is case I want to take another shot at it on my  own 
      #END
    # goes through every interaction of both lists with the exception of  the first 
     self.canvas.create_line(int(time[1])+10, float(Temperature[1])+20,int(time[2])+10,float(Temperature[2])+20,int(time[3])+10, float(Temperature[3])+20 
     ,int(time[4])+10, float(Temperature[4])+20,int(time[5])+10, float(Temperature[5])+20,int(time[6])+10, float(Temperature[6])+20,                         
     int(time[7])+10, float(Temperature[7])+20,int(time[8])+10, float(Temperature[8])+20,int(time[9])+10, float(Temperature[9])+20,                       
     int(time[10])+10, float(Temperature[10])+20,int(time[11])+10, float(Temperature[11])+20,int(time[12])+10, float(Temperature[12])+20,  
     int(time[13])+10, float(Temperature[13])+20,int(time[14])+10, float(Temperature[14])+20,int(time[18])+10, float(Temperature[18])+20,                          
     int(time[19])+10, float(Temperature[19])+20,int(time[20])+10, float(Temperature[20])+20,int(time[21])+10, float(Temperature[21])+20, 
     int(time[22])+10, float(Temperature[22])+20,int(time[23])+10, float(Temperature[23])+20,int(time[24])+10, float(Temperature[24])+20)
     self.canvas.place(relx=0.5, rely=0.5, anchor="center") #centers the canvas to the center of the screen 
     self.canvas.scale(ALL,1,1,10,10,)
     self.canvas.create_text(185,330, text ="X = 1 to 24 " )
     self.canvas.create_text(125,250, text ="Y = 0 to -13.4 " )
     #end of first graph stuff 

     
     text=ScrolledText(Gui, height = 20, width= 50) #sets the height of the text, below sets the text 
     text.insert(END,"The graph shown demonstratees the change in temperature in Grande Prarire alberta over a 24 hour period unfortunately Because the changes in temperature are so small it is difficult to actually see the difference. you can however drag to move the graphy wherever you want ")
     text.grid(row=100, column=3) #sets the location of the text 
     # text code end 
     
     self.canvas.create_rectangle(int(time[1])+20,int(windspeed[1])+20,int(time[1])+20,1+20,)
     self.canvas.create_rectangle(int(time[2])+30,int(windspeed[2])+20,int(time[2])+40,1+20,)
     self.canvas.create_rectangle(int(time[3])+50,int(windspeed[3])+20,int(time[3])+60,1+20,)
     self.canvas.create_rectangle(int(time[4])+70,int(windspeed[4])+20,int(time[4])+80,1+20,)                             
     self.canvas.create_rectangle(int(time[5])+90,int(windspeed[5])+20,int(time[5])+100,1+20,)   
     self.canvas.create_rectangle(int(time[6])+110,int(windspeed[6])+20,int(time[6])+120,1+20,)
     self.canvas.create_rectangle(int(time[7])+130,int(windspeed[7])+20,int(time[7])+140,1+20,)
     self.canvas.create_rectangle(int(time[8])+150,int(windspeed[8])+20,int(time[8])+160,1+20,)
     self.canvas.create_rectangle(int(time[9])+170,int(windspeed[9])+20,int(time[9])+180,1+20,)                             
     self.canvas.create_rectangle(int(time[10])+190,int(windspeed[10])+20,int(time[10])+200,1+20,)   
     self.canvas.create_rectangle(int(time[11])+210,int(windspeed[11])+20,int(time[11])+220,1+20,)
     self.canvas.create_rectangle(int(time[12])+230,int(windspeed[12])+20,int(time[12])+240,1+20,)
     self.canvas.create_rectangle(int(time[13])+250,int(windspeed[13])+20,int(time[13])+260,1+20,)
     self.canvas.create_rectangle(int(time[14])+270,int(windspeed[14])+20,int(time[14])+280,1+20,)                             
     self.canvas.create_rectangle(int(time[15])+290,int(windspeed[15])+20,int(time[15])+300,1+20,)   
     self.canvas.create_rectangle(int(time[16])+310,int(windspeed[16])+20,int(time[16])+320,1+20,)
     self.canvas.create_rectangle(int(time[17])+330,int(windspeed[17])+20,int(time[17])+340,1+20,)
     self.canvas.create_rectangle(int(time[18])+350,int(windspeed[18])+20,int(time[18])+360,1+20,)
     self.canvas.create_rectangle(int(time[19])+370,int(windspeed[19])+20,int(time[19])+380,1+20,)                             
     self.canvas.create_rectangle(int(time[20])+390,int(windspeed[20])+20,int(time[20])+400,1+20,)   
     self.canvas.create_rectangle(int(time[21])+410,int(windspeed[21])+20,int(time[21])+420,1+20,)
     self.canvas.create_rectangle(int(time[22])+430,int(windspeed[22])+20,int(time[22])+440,1+20,)
     self.canvas.create_rectangle(int(time[23])+450,int(windspeed[23])+20,int(time[23])+460,1+20,)
     self.canvas.create_rectangle(int(time[24])+470,int(windspeed[24])+20,int(time[24])+480,1+20,)                             
     self.canvas.create_line(int(time[24])+470,int(windspeed[24])+20,int(time[24])+6+480,1+20,1,1+20)
     self.canvas.create_text(185,10, text ="Wind speed change on the hour over 24 hours" )

     # end for the bar chart 



     self.canvas.create_rectangle(295,400,560,425, )
     self.canvas.create_text(425,410, text ="Grande prarie has no way to detect solar radiation" )
     self.canvas.create_line(400,425,400,450,400,500,arrow=tk.LAST)
     self.canvas.create_text(405,450, text ="So" )
     self.canvas.create_rectangle(295,500,580,525, )
     self.canvas.create_text(440,510, text ="all results are 0 even though there should be variance " )
     #self.canvas.bind("<MouseWheel>",do_zoom(Event,self)) # failed atempt to allow scrolling in on the graph, left it here just incase I wamt  to make anotehr atempt later
     self.canvas.bind('<ButtonPress-1>', lambda event: self.canvas.scan_mark(event.x, event.y)) # on button press allows the  drag to actually  function 
     self.canvas.bind("<B1-Motion>", lambda event: self.canvas.scan_dragto(event.x, event.y, gain=1)) # allows the canvas to be dragged around 

# https://app.diagrams.net/#G1qHZLLtsikfJMxNszLFbyOjqdlVxKQzsb



      
 


text_file = Open_txt() #calls  the function that opens the text file and then assigns the result to this varaibler 
Break_By_Line()  # calls the function that does all the heavy lifting on seperaing the file into 2 
geeks = GFG(Gui)  #  calls all of the UI                                          
















Gui.mainloop() #loop for the UI