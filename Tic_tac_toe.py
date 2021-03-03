#Game logic and functions required
#board
#display
#play game
#check win
    #check rows, columns, diagonals
#check for draw
#flip players
#check if input is valid etc


#tic tac toe using tkinter with gui and stuff

# Tic-Tac-Toe
Tic Tac Toe for the computer project
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')
#root.geometry("1200x710") #Get back to this later

#Define the function b_click
count=0
def b_click(m):
    global count
    message = ''
    if count%2==0:
        m["text"] = 'X'
    else:
        m["text"] = 'O'
    count+=1
    find_winner()
b1 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
b2 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
b3 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))
b4 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
b5 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
b6 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))
b7 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))
b8 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b8))
b9 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b9))
#"""

#Grid our buttons to the screen
#Row 1
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

#Row 2
b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

#Row 3
b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)


def find_winner():
    #Checking horizontally
    if b1["text"]==b2["text"]==b3["text"] and b1["text"]!=" ":
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b1["text"]+"\nCONGRATULATIONS!!")
    elif b4["text"]==b6["text"]==b5["text"] and b6["text"]!=" ":
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b6["text"]+"\nCONGRATULATIONS!!")
    elif b7["text"]==b8["text"]==b9["text"] and b7["text"]!=" ":
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b7["text"]+"\nCONGRATULATIONS!! ")

    #Checking vertically
    elif b1["text"]==b4["text"]==b7["text"] and b4["text"]!=" ":
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b4["text"]+"\nCONGRATULATIONS!!")
    elif b2["text"]==b5["text"]==b8["text"] and b2["text"]!=" ":
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b2["text"]+"\nCONGRATULATIONS!!")
    elif b3["text"]==b6["text"]==b9["text"] and b9["text"]!=" ":
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b9["text"]+"\nCONGRATULATIONS!!")

    #Checking diagonally
    elif b1["text"]==b5["text"]==b9["text"] and b9["text"]!=" ":
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b1["text"]+"\nCONGRATULATIONS!!")
    elif b3["text"]==b5["text"]==b7["text"] and b7["text"]!=" ":
        b3.config(bg="yellow")
        b7.config(bg="yellow")
        b5.config(bg="yellow")
        disable()
        messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b7["text"]+"\nCONGRATULATIONS!!")
    elif count==9:
        messagebox.showinfo("Tic-Tac_Toe","IT'S A DRAW!")
def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
root.mainloop()
