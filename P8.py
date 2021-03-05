from tkinter import *
from tkinter import messagebox
def f():
    a=Tk()
    a.title('TICTACTOE')
    l=Label(a,text='player 1 or \'X\' \'s  turn',relief=SUNKEN,bd=5)
    l.grid(columnspan=3,row=4,pady=10,) 
    

    d=1
    count=0    
    def res():
        a.destroy()#rest of combinations donot close the previous window
        f()        
        
    def ex():
        a.destroy()
    
    b_r=Button(a,text='reset',command=res,bg='yellow',relief=RIDGE,anchor=E)
    b_r.grid(row=5,column=1,sticky=E)

    b_e=Button(a,text='exit',command=ex,bg='blue',fg='white',relief=RIDGE,anchor=W)
    b_e.grid(row=5,column=3,sticky=W)
    
    def buttonclick(b):
        nonlocal count,d
        #donot use global as it refers outside the function
        if d==1:
            d=0            
            b['text']='X'
            l['text']='player 2 or \'O\' \'s  turn'
            b.config(state=DISABLED) 
            count+=1

        elif d==0:
            d=1            
            b['text']='O'
            l['text']='player 1 or \'X\' \'s  turn'
            b.config(state=DISABLED) 
            count+=1

        def wincheck(a): 

            if (b1['text'],b5['text'],b9['text']) == (a,a,a):
                (b1['bg'],b5['bg'],b9['bg'])=('red','red','red')
                return True

            elif (b3['text'],b5['text'],b7['text']) == (a,a,a):
                (b3['bg'],b5['bg'],b7['bg'])=('red','red','red')
                return True

            elif (b1['text'],b2['text'],b3['text']) == (a,a,a):
                (b1['bg'],b2['bg'],b3['bg'])=('red','red','red')
                return True

            elif (b4['text'],b5['text'],b6['text']) == (a,a,a):
                (b4['bg'],b5['bg'],b6['bg'])=('red','red','red')
                return True

            elif (b7['text'],b8['text'],b9['text']) == (a,a,a):
                (b7['bg'],b8['bg'],b9['bg'])=('red','red','red')
                return True

            elif (b1['text'],b4['text'],b7['text']) == (a,a,a):
                (b1['bg'],b4['bg'],b7['bg'])=('red','red','red')
                return True

            elif (b2['text'],b5['text'],b8['text']) == (a,a,a):
                (b2['bg'],b5['bg'],b8['bg'])=('red','red','red')
                return True

            elif (b3['text'],b6['text'],b9['text']) == (a,a,a):
                (b3['bg'],b6['bg'],b9['bg'])=('red','red','red')
                return True

            else:
                return False

        if count==9:
            messagebox.showinfo('tictactoe','match draw!!')

        elif count<9:
            wincheck('X')
            wincheck('O')
            if wincheck('X')==True:
                messagebox.showinfo('tictactoe','player 1  or \'X\' \'s wins!!')
                a.quit()
            elif wincheck('O')==True:
                messagebox.showinfo('tictactoe','player 2 or \'O\' \'s  wins!!')
                a.quit()
        
    b1=Button(a,text='',command=lambda: buttonclick(b1),bd=5)
    b2=Button(a,text='',command=lambda: buttonclick(b2),bd=5)
    b3=Button(a,text='',command=lambda: buttonclick(b3),bd=5)
    b4=Button(a,text='',command=lambda: buttonclick(b4),bd=5)
    b5=Button(a,text='',command=lambda: buttonclick(b5),bd=5)
    b6=Button(a,text='',command=lambda: buttonclick(b6),bd=5)
    b7=Button(a,text='',command=lambda: buttonclick(b7),bd=5)
    b8=Button(a,text='',command=lambda: buttonclick(b8),bd=5)
    b9=Button(a,text='',command=lambda: buttonclick(b9),bd=5)

    b1.grid(row=1,column=1,columnspan=1, padx=10, pady=10)
    b2.grid(row=1,column=2,columnspan=1, padx=10, pady=10)
    b3.grid(row=1,column=3,columnspan=1, padx=10, pady=10)
    b4.grid(row=2,column=1,columnspan=1, padx=10, pady=10)
    b5.grid(row=2,column=2,columnspan=1, padx=10, pady=10)
    b6.grid(row=2,column=3,columnspan=1, padx=10, pady=10)
    b7.grid(row=3,column=1,columnspan=1, padx=10, pady=10)
    b8.grid(row=3,column=2,columnspan=1, padx=10, pady=10)
    b9.grid(row=3,column=3,columnspan=1, padx=10, pady=10)

    a.mainloop()
f()