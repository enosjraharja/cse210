from tkinter import Tk,ttk,Button
from tkinter import messagebox
from random import randint

#This is for Module Layout
def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(&#91;'disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(&#91;'disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(&#91;'disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(&#91;'disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(&#91;'disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(&#91;'disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(&#91;'disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(&#91;'disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(&#91;'disabled'])

#This Is For Winner Checking Section 

def CheckWinner():
    global mov 
    winner = -1

    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and ( 9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and ( 9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and ( 7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner ==1:
        messagebox.showinfo(title="Congratulations.", 
            message="Player 1 is the winner")
    elif winner ==2:
        messagebox.showinfo(title="Congratulations.", 
            message="Player 2 is the winner")
    elif mov ==9:
        messagebox.showinfo(title="Draw", 
            message="It's a Draw!!")

#This is to make the button clickable
def ButtonClick(id):
    global ActivePlayer
    global p1,p2
    global mov

    if(ActivePlayer ==1):
        SetLayout(id,"X")
        p1.append(id)
        mov +=1
        root.title("Tic Tac Toe : Player 2")
        ActivePlayer =2

    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id)
        mov +=1
        root.title("Tic Tac Toe : Player 1")
        ActivePlayer =1
    CheckWinner()

def Restart():
    global p1,p2,mov,ActivePlayer
    p1.clear(); p2.clear()
    mov,ActivePlayer = 0,1
    root.title("Tic Tac Toe : Player 1")
    EnableAll()