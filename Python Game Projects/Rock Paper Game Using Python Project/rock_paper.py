#importing the basic library that we will use for the development of this project
from tkinter import *
from PIL import Image,ImageTk
import random

#these are some of the variables that we will use in rock paper and scissor game
userscore=0
pcscore=0


#these are various function that will help us to handle all the events that will take place in this project
#we also used the config() function to configure the various widgets like its color, size etc
def enter(event):
    rock.config(bg='black',fg='white')
def enter1(event):
    paper.config(bg='black',fg='white')
def enter2(event):
    scissor.config(bg='black',fg='white')
def leave(event):
    rock.config(bg='white',fg='black')
def leave1(event):
    paper.config(bg='white',fg='black')
def leave2(event):
    scissor.config(bg='white',fg='black')
def entergame(event):
    maingame()

#Maingame Function will bring a new window of GUI and will provide a platform to play rock paper and scissor Game
def maingame():
    global userscore,pcscore
    global nameinp
    global rock,paper,scissor
    #this is used to set the size of the tkinter window
    #for this purpose we made use of geometry() function
    root.geometry('850x750')
    #we used the destroy function to destroy the widgets on the screen
    name.destroy()
    f1.destroy()
    inpname.destroy()
    sub.destroy()
    
    #the below 4 lines will work for the display of scores
    #we used the grid() in tkinter to adjust the place of the labels for displaying scores
    L2=Label(text=f"{nameinp.get()} Score: {userscore}",bg='#4834DF',fg='#ffffff',borderwidth=5,relief=RAISED,font='Rockwell 13 bold',padx=4,pady=2)
    L2.grid(row=6,column=0,pady=15)
    L3=Label(text=f"PC Score: {pcscore}",bg='#4834DF',fg='white',borderwidth=5,relief=RAISED,font='Rockwell 13 bold',padx=4,pady=2)
    L3.grid(row=7,column=0,pady=15)
    
    #the below function handles the click event
    def click(event):
         #These variable will get or count the scores of user and pc
        global userscore,pcscore
        #We are using L1 Label that we defined in the above code
        global L1     
        #we are using old pcchose label
        global pcchose  
        #here we will use the forgetting or removing function to remove the other labels properly
        L1.grid_forget() 
        #this below will destroy the selected label
        pcchose.destroy()   
        
        #This command will take the text of button
        val=event.widget.cget('text')

        #this is to make a computer's selection random
        #we made a list of 3 elements, so that the pc can choose randomly from it
        x=random.randint(0,2)
        l1=['Rock','Paper','Scissor']
        #this is the variable where the choice of the pc will be stored
        pc_opt=l1[x] 

        #the below label in rock paper and scissor game will display the choice of the pc in the form of a label
        pcchose=Label(text=f'PC Opted: {pc_opt}',font='lucida 15 bold',bg='black',fg='red')
        #here along with grid() function, we used various other parameters of that function in order to set the postion of the elements
        pcchose.grid(row=6,column=1,pady=15)

        #The below conditionals hold the actual logic behind the game of Rock, Paper and Scissor Game in Python 
        #val means what user chose and pc_opt means what pc chose or opted
        #below is the conditional block for users choice equal to rock and pc's choice equal to paper
        if val=='Rock' and pc_opt=='Paper':
            L1=Label(text='PC Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=7,column=1,pady=15)
            pcscore+=1
            
        #below is the conditional block for users choice equal to rock and pc's choice equal to scissor    
        elif val=='Rock' and pc_opt=='Scissor':
            L1=Label(text=f'{nameinp.get()} Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=6,column=1,pady=15)
            userscore+=1
            
        #below is the conditional block for users choice equal to paper and pc's choice equal to scissor    
        elif val=='Paper' and pc_opt=='Scissor':
            L1=Label(text='PC Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=7,column=1,pady=15)
            pcscore+=1
            
        #below is the conditional block for users choice equal to paper and pc's choice equal to rock    
        elif val=='Paper' and pc_opt=='Rock':
            L1=Label(text=f'{nameinp.get()} Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=7,column=1,pady=15)
            userscore+=1
            
        #below is the conditional block for users choice equal to scissor and pc's choice equal to rock    
        elif val=='Scissor' and pc_opt=='Rock':
            L1=Label(text='PC Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=7,column=1,pady=15)
            pcscore+=1
            
        #below is the conditional block for users choice equal to scissor and pc's choice equal to paper    
        elif val=='Scissor' and pc_opt=='Paper':
            L1=Label(text=f'{nameinp.get()} Won',font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=7,column=1,pady=15)
            userscore+=1
            
        #below is the conditional block when user's choice and pc's choice are same    
        elif val==pc_opt:
            L1=Label(text=f"It's A Tie",font='lucida 15 bold',bg='black',fg='gold')
            L1.grid(row=7,column=1,pady=15)
        maingame()

        
    
    #the overall Layout of RPS Game is handled by the below code
    #we used the lable() to add various labels on our new window
    head=Label(text='Rock Paper Scissor',font='arial 35 bold',bg='black',fg='white')
    head.grid(columnspan=2,row=0,ipadx=70,padx=33,pady=10)
    head1=Label(text='CopyAssignment',font='arial 35 bold',bg='red',fg='white')
    head1.grid(columnspan=2,row=1,ipadx=70,padx=33,pady=10)
    playerone=Label(text=f'Player 1 : {nameinp.get()}',font='lucida 16')
    playerone.grid(row=2,column=0)
    playertwo=Label(text=f'Player 2 : Computer',font='lucida 16')
    playertwo.grid(row=2,column=1)
    
    #the below are the set of buttons that are available for the player 1
    rock=Button(text='Rock',font='comicsansms 14 bold',height=1,width=7)
    rock.grid(row=3,column=0,pady=15)
    #the bind() is used to bind multiple methods in the Program
    rock.bind('<Enter>',enter)
    rock.bind('<Leave>',leave)
    rock.bind('<Button-1>',click)
    paper=Button(text='Paper',font='comicsansms 14 bold',height=1,width=7)
    paper.grid(row=4,column=0)
    paper.bind('<Enter>',enter1)
    paper.bind('<Leave>',leave1)
    paper.bind('<Button-1>',click)
    scissor=Button(text='Scissor',font='comicsansms 14 bold',height=1,width=7)
    scissor.grid(row=5,column=0,pady=15)
    scissor.bind('<Enter>',enter2)
    scissor.bind('<Leave>',leave2)
    scissor.bind('<Button-1>',click)

    #these are the buttons for the computer
    rock1=Button(text='Rock',font='comicsansms 14 bold',height=1,width=7)
    rock1.grid(row=3,column=1,pady=15)
    paper1=Button(text='Paper',font='comicsansms 14 bold',height=1,width=7)
    paper1.grid(row=4,column=1)
    scissor1=Button(text='Scissor',font='comicsansms 14 bold',height=1,width=7)
    scissor1.grid(row=5,column=1,pady=15)

    #this is the button to close the Game
    #it will basically destroy all the widgets that we used in the game
    btnclose=Button(text='Close Game',command=root.destroy,bg='green',font='arial 10 bold')
    btnclose.place(x=300,y=410)

#now the actul programming of the GUI starts

#if __name__=='__main__':
root=Tk()
root.title('Rock Paper Scissor - CopyAssignment')
root.wm_iconbitmap("play.png")
#the below three lines are used to set the size of the window of username and main game
root.geometry('650x750')
#this maxsize() function is used to set the max size of window equivlent to the one that we passed in the function
root.maxsize
#this is minsize() function annd it is bascially responsible for handling the minimum size of the tkinter window
root.minsize(650,450)

#Defining some widgets to use them in diff functions
rock=Button()
paper=Button()
scissor=Button()

#Defining Label to use it later in the program
#This Label will show the who won pc or user
L1=Label()    
#This Label will show the preference of what pc opted or chose
pcchose=Label()     


#the below is the code to handle the first frame  of thee window
#this window will allow the user to add the username of his/her choice
#once the username is added the user will be able to enter in the game
f1=Frame(root)
img=Image.open('symbols.png')
img=img.resize((650,450),Image.ANTIALIAS)
pic=ImageTk.PhotoImage(img)
Lab=Label(f1,image=pic)
Lab.pack()
f1.pack()

#we made a label widget to add the label that informs the user about entering his/her name in rock, paper and sicssor game
name=Label(root,text='Enter Your Name :',font='arial 15 bold')
name.place(x=262,y=250)

#This below variable will store the name of user and will further be used to display the name of the user wherever we want to display
nameinp=StringVar()
inpname=Entry(root,textvar=nameinp,font='arial 10 bold')
#We binded Return event with inpname entry widget i.e. if enter key is pressed then entergame function will be called
inpname.bind('<Return>',entergame)  
inpname.place(x=275,y=290)

#this is the button that will appear on the home username window
#a button of lets play is added so that the user can enter the main game window once the username is added
sub=Button(root,text="Let's Play",font='lucida 10 bold',bg='black',fg='white',command=maingame)
sub.place(x=305,y=350)

#this the tkinter mainloop() function that will call the main window of the tkinter
root.mainloop()