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
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

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

def reset():
    global b, b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count
    count = 0

    b1 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
    b2 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
    b3 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))
    b4 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
    b5 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
    b6 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))
    b7 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))
    b8 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b8))
    b9 = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b9))

    b = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

    #Grid our buttons to the screen

    x = 0
    for i in range(3):
        for j in range(3):
            b[x].grid(row = i, column = j)
            x+=1

def find_winner():
    #To check if winnner
    #r --> rows     c --> columns   d --> diagonals
    r = [[b1,b2,b3], [b4,b5,b6], [b7,b8,b9]]
    c = [[b1,b4,b7], [b2,b5,b8], [b3,b6,b9]]
    d = [[b1,b5,b9], [b3,b5,b7]]
    win = [r, c, d]
    res = False
    for i in win:
        for j in i:
            if j[0]["text"]==j[1]["text"]==j[2]["text"] and j[0]["text"]!=" ":
                for k in j:
                    k.config(bg="yellow")
                disable()
                messagebox.showinfo("Tic-Tac_Toe","WINNERR is "+b1["text"]+"\nCONGRATULATIONS!!")
                res = True
    #To check if draw
    if count == 9 and res == False :
        messagebox.showinfo("Tic-Tac_Toe","IT'S A DRAW!")

def disable():
    global b
    for i in b:
        i.config(state = DISABLED)

#Creating menu
my_menu = Menu(root)
root.config(menu = my_menu)

#Creating options in the Menu
options_menu = Menu(root, tearoff = False)
my_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Reset Game", command = reset)

reset()

root.mainloop()
