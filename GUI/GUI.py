'''''
# GUI Creation

from tkinter import*
#from PIL import ImageTk,Image


# Window Creation
root = Tk()

# Modify Window

root.title("ANCLA")
root.geometry ("200x100")

app = Frame (root)
app.grid()

runbtn = Button (app, text = "RUN")
runbtn.grid()

clearbtn = Button (app, text ="CLEAR")
clearbtn.grid()

#label = Label (app, text = " This is ANCLA IDE")
#label.grid()
# Activate Window
root.mainloop()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.configure(background ='white')
        self.grid()
        self.button_clicks = 0 #Count number of button clicks
        self.create_widgets()
        
          
    def create_widgets(self):
        self.text1 = Text(self, height=9, width=38)
        self.photo=PhotoImage(file='ANCLA.png')
        self.text1.grid(row=0,column =0,sticky=W)
        self.text1.insert(END,'\n')
        self.text1.image_create(END,image=self.photo)

        header =Label(self, text="CODE: ",font='System 17 bold')
        header.grid(row=1,column = 0)
        header.configure(background = 'white')
        self.e1 = Entry(self, width = 61)
        self.e1.grid(row=1, column=1)
        self.e1.configure(background = '#FFFBF5')

    
        self.var1 = IntVar()
        check1 = Checkbutton(self, text="verbose",font='System 12 bold', variable=self.var1)
        check1.grid(row=2,column = 0, sticky=W)
        check1.configure(background = 'white')
        self.var2 = IntVar()
        check2 = Checkbutton(self, text="datalog", font='System 12 bold',variable=self.var2)
        check2.grid(row=2,column = 1,sticky=W)
        check2.configure(background = 'white')
        
        self.setbtn = Button (self, text = "SETTINGS",font='System 14 bold',width =10)
        self.setbtn.grid(row = 3, column = 1,columnspan=2, rowspan=2,
               sticky=W)
        self.setbtn["command"]= self.var_states

        self.runbtn = Button (self,text=u"\u25B6",fg ='green',font='System 16 bold',width =10)
        #self.runbtn.configure(background='#32CD32')
        self.runbtn.grid(row = 5, column = 0,columnspan = 1,sticky = W)
        #self.runbtn["command"]=self.update_count
        self.runbtn["command"]= self.showLabel

        lab = Label(self, text="OUPUT:",font='System 14 bold')
        lab.grid(row=5,column =1)
        lab.configure(background = 'white')

        self.clearbtn = Button (self, text ="CLEAR", fg ="red",font='System 14 bold',width =10)
        self.clearbtn.grid(row = 5, column = 1,columnspan = 1,sticky = W)
        self.clearbtn["command"]= self.clear_call

        textUni = Label(self,text=u"\u2693",font='System 32 bold', fg='orange')
        textUni.configure(background = 'white')
        textUni.grid(row=4,column =0)
       
        self.scroll = Scrollbar(self)
        self.text = Text (self, width=85,height =9, wrap = WORD)
        self.text.configure(background = '#E0FFFF')
        self.text.grid(row=6,column =0,columnspan = 2, sticky = W)
        self.scroll.grid(row=6,column =0,columnspan = 2, sticky = W)
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

        
    def update_count(self):
        self.button_clicks += 1
        self.runbtn["text"] = "Total Clicks: " + str(self.button_clicks)


    def var_states(self):
     if self.var1.get() == 1:
         message = "Verbose is True\n"
         self.text.insert(0.0,message)
        
     else:
         message = "Verbose is False\n"
         self.text.insert(0.0,message)
        
     if self.var2.get() == 1:
         message = "Datalog is True\n"
         self.text.insert(0.0,message)
        
     else:
         message = "Datalog is False\n"
         self.text.insert(0.0,message)

    def clear_call(self):
        self.text.delete(0.0,END)

    def showLabel(self):
        content = self.e1.get()
        fileStack = []
        if content == "analyze-sentiment" or content =="live-sentiment":
            message = "Correct Syntax\n"
            self.text.insert(0.0,message)
        
        elif content =="help-config":
            fileName = "generic"
            try:
             with open(fileName + ".txt", 'r') as helpFile:
                 for line in helpFile:
                     fileStack.append(line)

                 while True:
                     if len(fileStack) == 0:
                         break

                     message = fileStack.pop()
                     self.text.insert(0.0,message)
            except FileNotFoundError:
             message = "Function doesn't exist.\nTry calling help-function without parameters to see a list of all available functions."
             self.text.insert(0.0,message)
        else:
            message = "Incorrect Line Code\n"
            self.text.insert(0.0,message)


# Window Creation
root = Tk()

# Modify Window
root.title("ANCLA IDE")
root.configure(background='white')
root.geometry ("700x450")
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Terminal", menu=helpmenu)
app = Application (root)
root.mainloop()
'''''