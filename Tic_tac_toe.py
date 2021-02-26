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

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')
#root.geometry("1200x710") #Get back to this later
    
#b = [] #Button list

#Define the function b_click
count=0
def b_click(m):
    global count
    message = ''
    if count%2==0:
        #b[b.index(m)]["text"] = 'X'
        m["text"] = 'X'
    else:
        #b[b.index(m)]["text"] = 'O'
        m["text"] = 'O'
    count+=1
"""

#Creating buttons
b = []

for i in range(9):
    m = Button(root, text =" ",font = ("Helvetica",20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(m))
    b.append(m)

"""
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
"""
x = 0
for i in range(3):
    for j in range(3):
        b[x].grid(row = i, column = j)
        x+=1
"""
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
#"""

root.mainloop()
