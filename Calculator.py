#کتابخانه
from tkinter import*
windos = Tk()

#اسم
windos.title("Calculator")

#بک گراند و اندازه
windos.configure(background="black",height=465,width=360)

#موقعیت
windos.geometry("365x510+1150+150")

#قفل کردن سایز
windos.resizable(width=False,height=False)

#نمایش خروجی
entry = Entry(windos,borderwidth=19,font="arial",foreground="green")
entry.grid(row=0,column=0,ipadx=50,ipady=15,columnspan=4,)

# La = Label(windos,text="",background="black").grid(row=1,column=0,columnspan=3)

#تابع
def Calculator(number):
    contenet = entry.get()
    contenet = list(contenet)
    entry.insert(len(contenet),number)

def equal():
    number_two = entry.get()
    if mod == "plural":
        javab = float(number_one) + float(number_two)
    elif mod == "Minus":
        javab = float(number_one) - float(number_two)
    elif mod == "multiplication":
        javab = float(number_one) * float(number_two)
    elif mod == "division":
        javab = float(number_one) / float(number_two)
    entry.delete(0,END)
    entry.insert(0,javab)
    

def plural():
    global number_one
    global mod
    number_one = entry.get()
    entry.delete(0,END)
    mod = "plural"
    
def Minus():
    global mod
    global number_one
    number_one = entry.get()
    entry.delete(0,END)
    mod = "Minus"

def multiplication():
    global mod
    global number_one
    number_one = entry.get()
    entry.delete(0,END)
    mod = "multiplication"

def division():
    global mod
    global number_one
    number_one = entry.get()
    entry.delete(0,END)
    mod = "division"
    

#باتون
button_0 = Button(text="0",padx="70",pady="35",command=lambda: Calculator(0),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=5,column=0,columnspan=2)
button_1 = Button(text="1",padx="30",pady="30",command=lambda: Calculator(1),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=4,column=0)
button_2 = Button(text="2",padx="30",pady="30",command=lambda: Calculator(2),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=4,column=1)
button_3 = Button(text="3",padx="30",pady="30",command=lambda: Calculator(3),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=4,column=2)
button_4 = Button(text="4",padx="30",pady="30",command=lambda: Calculator(4),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=3,column=0)
button_5 = Button(text="5",padx="30",pady="30",command=lambda: Calculator(5),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=3,column=1)
button_6 = Button(text="6",padx="30",pady="30",command=lambda: Calculator(6),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=3,column=2)
button_7 = Button(text="7",padx="30",pady="30",command=lambda: Calculator(7),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=2,column=0)
button_8 = Button(text="8",padx="30",pady="30",command=lambda: Calculator(8),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=2,column=1)
button_9 = Button(text="9",padx="30",pady="30",command=lambda: Calculator(9),borderwidth=6,background="black",foreground="gold",font="arial").grid(row=2,column=2)


#عملگرا
Button_equal = Button(text="=",padx="30",font="arial",pady="30",borderwidth=10,background="green",foreground="white",command=equal).grid(row=2,column=3)
Button_Minus = Button(text="-",padx="30",font="arial",pady="30",borderwidth=10,background="red",foreground="white",command=Minus).grid(row=3,column=3)
Button_plural = Button(text="+",padx="30",font="arial",pady="30",borderwidth=10,background="red",foreground="white",command=plural).grid(row=4,column=3)
Button_multiplication = Button(text="x",padx="30",font="arial",pady="30",borderwidth=10,background="red",foreground="white",command=multiplication
).grid(row=5,column=3)
Button_division = Button(text="÷",padx="30",font="arial",pady="30",borderwidth=10,background="red",foreground="white",command=division).grid(row=5,column=2)

mainloop()

