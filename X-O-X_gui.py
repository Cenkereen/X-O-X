import tkinter as tk
from tkinter import messagebox

form = tk.Tk()
form.title("X-O-X")
form.geometry("390x404+700+250")

def click(n):
    global turn
    global rou
    if n["text"]==" " and turn:
        n["text"]="X"
        turn=False
        rou+=1
    elif n["text"]==" " and turn==False:
        n["text"] = "O"
        turn=True
        rou+=1
    check()

def check():
    if rou==9:
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b1["text"]==b2["text"]==b3["text"]=="X"or b1["text"]==b2["text"]==b3["text"]=="O":
        b1["bg"]="red"
        b2["bg"] = "red"
        b3["bg"] = "red"
        response=messagebox.askyesno("X-O-X","Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b4["text"]==b5["text"]==b6["text"]=="X" or b4["text"]==b5["text"]==b6["text"]=="O":
        b4["bg"]="red"
        b5["bg"] = "red"
        b6["bg"] = "red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b7["text"]==b8["text"]==b9["text"]=="X" or b7["text"]==b8["text"]==b9["text"]=="O":
        b7["bg"]="red"
        b8["bg"] = "red"
        b9["bg"] = "red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b1["text"]==b5["text"]==b9["text"]=="X" or b1["text"]==b5["text"]==b9["text"]=="O":
        b1["bg"]="red"
        b5["bg"] = "red"
        b9["bg"] = "red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b3["text"]==b5["text"]==b7["text"]=="X" or b3["text"]==b5["text"]==b7["text"]=="O":
        b3["bg"]="red"
        b5["bg"] = "red"
        b7["bg"] = "red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b1["text"]==b4["text"]==b7["text"]=="X" or b1["text"]==b4["text"]==b7["text"]=="O":
        b1["bg"]="red"
        b4["bg"] = "red"
        b7["bg"] = "red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b2["text"]==b5["text"]==b8["text"]=="X" or b2["text"]==b5["text"]==b8["text"]=="O":
        b2["bg"]="red"
        b5["bg"] = "red"
        b8["bg"] = "red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()
    elif b3["text"]==b6["text"]==b9["text"]=="X" or b3["text"]==b6["text"]==b9["text"]=="O":
        b3["bg"]="red"
        b6["bg"] ="red"
        b9["bg"] ="red"
        response = messagebox.askyesno("X-O-X", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()



def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,turn,rou
    turn=True
    rou=0
    b1=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b1))
    b1.grid(row=1,column=0)
    b2=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b2))
    b2.grid(row=1,column=1)
    b3=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b3))
    b3.grid(row=1,column=2)
    b4=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b4))
    b4.grid(row=2,column=0)
    b5=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b5))
    b5.grid(row=2,column=1)
    b6=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b6))
    b6.grid(row=2,column=2)
    b7=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b7))
    b7.grid(row=3,column=0)
    b8=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b8))
    b8.grid(row=3,column=1)
    b9=tk.Button(form,text=" ",font="Times 20",bg="white",height=3,width=8,command=lambda: click(b9))
    b9.grid(row=3,column=2)

reset()
label=tk.Button(form,width=35,text="Reset",command=reset)
label.grid(row=0,column=0,columnspan=3,padx=15,pady=15)
form.mainloop()