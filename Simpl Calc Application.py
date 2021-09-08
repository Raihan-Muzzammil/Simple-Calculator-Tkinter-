import tkinter
from tkinter import *
calc = Tk()
main = tkinter.Frame(calc, bg="black")
proc = tkinter.Frame(calc, bg="black")


calc.geometry("1280x720")
calc.title("Better than your everyday tool")
calc.configure(bg="black")

def add():
    res = float(num1_b.get()) + float(num2_b.get())
    n1 = float(num1_b.get())
    n2 = float(num2_b.get())
    lbl_text.config(text="The answer is %f" % (res))
    print(res)

def sub():
    res = float(num1_b.get()) - float(num2_b.get())
    n1 = int(float(num1_b.get()))
    n2 = int(float(num2_b.get()))
    lbl_text.config(text="The answer is %f" % (res))
    print(res)

def mul():
    res = float(num1_b.get()) * float(num2_b.get())
    n1 = float(num1_b.get())
    n2 = float(num2_b.get())
    lbl_text.config(text="The answer is %f" % (res))
    print(res)

def div():
    res = float(num1_b.get()) / float(num2_b.get())
    n1 = float(num1_b.get())
    n2 = float(num2_b.get())
    lbl_text.config(text="The answer is %f" % (res))
    print(res)

def printmes1():
    print("Alright then, nibba")
    main.pack_forget()
    proc.pack()

def printmes2():
    print("Rotating Back, nibba")
    proc.pack_forget()
    main.pack()

def exit1():
    print("Goodbye then, nibba")
    exit()

label1 = Label(main,text=" | Simple Calculator | ",fg="cyan",bg="black",relief="solid",font=("Balgin-BlackCondensed",40))
label1.grid(row=0, column=0, padx= 100, pady= 100)

label2 = Label(proc,text=" | Simple Calculator | ",fg="cyan",bg="black",relief="solid",font=("Balgin-BlackCondensed",40))
label2.grid(row=0, column=0, padx= 100, pady= 100)

buttonadd = Button(proc,text=" Addition  ",fg="black",bg="cyan",relief="groove",font=("Balgin-Black",18),command = add).grid(row=1, column=0, padx= 10, pady= 5)
buttonsub = Button(proc,text=" Subtraction  ",fg="black",bg="cyan",relief="groove",font=("Balgin-Black",18),command = sub).grid(row=2, column=0, padx= 10, pady= 5)
buttonmul = Button(proc,text="Multiplication",fg="black",bg="cyan",relief="groove",font=("Balgin-Black",18),command = mul).grid(row=3, column=0, padx= 10, pady= 5)
buttondiv = Button(proc,text="   Division   ",fg="black",bg="cyan",relief="groove",font=("Balgin-Black",18),command = div).grid(row=4, column=0, padx= 10, pady= 5)


labeln1 = Label(proc,text="Enter the First Number : ",fg="cyan",bg="black",relief="solid",font=("Balgin-BlackCondensed",18)).grid(row=2, column=1, padx= 10, pady= 5)
num1_b = Entry(proc)
num1_b.grid(row=2, column=2, padx= 10, pady= 5)


labeln2 = Label(proc,text="Enter the Second Number : ",fg="cyan",bg="black",relief="solid",font=("Balgin-BlackCondensed",18)).grid(row=3, column=1, padx= 10, pady= 5)
num2_b = Entry(proc)
num2_b.grid(row=3, column=2, padx= 10, pady= 5)

buttonback = Button(proc,text="Back",fg="black",bg="cyan",relief="groove",font=("Balgin-BlackCondensed",18),command = printmes2).grid(row=5, column=0, padx= 10, pady= 30)

lbl_text = Label(proc,fg="cyan",bg="black",relief="solid",font=("Balgin-BlackCondensed",25))
lbl_text.grid(row=4, column=1, padx= 10, pady= 5)

button1 = Button(main,text="Continue to Application",fg="black",bg="cyan",relief="groove",font=("Balgin-BlackCondensed",25),command = printmes1).grid(row=3, column=0, padx= 50, pady= 30)
button2 = Button(main,text="         Quit          ",fg="black",bg="cyan",relief="groove",font=("Balgin-BlackCondensed",25),command = exit1).grid(row=4, column=0, padx= 25, pady= 30)
main.pack()

calc.mainloop()
