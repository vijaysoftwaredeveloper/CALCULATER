from tkinter import*
t=Tk()
t.title("calculator")
t.geometry("570x600")
t.configure(bg="black")

equation=""
def show(value):
    global equation
    equation+=value
    l.config(text=equation)
def clear():
    global equation
    equation=""
    l.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    l.config(text=result)
    
l=Label(t,text="",width=25,height=2,font=("arial",30))
l.pack()

b1=Button(t,text="C",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="blue",command=lambda:clear())
b1.place(x=10,y=100)
b2=Button(t,text="/",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("/"))
b2.place(x=150,y=100)
b3=Button(t,text="%",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("%"))
b3.place(x=290,y=100)
b4=Button(t,text="*",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("*"))
b4.place(x=430,y=100)

b4=Button(t,text="7",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("7"))
b4.place(x=10,y=200)
b4=Button(t,text="8",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("8"))
b4.place(x=150,y=200)
b4=Button(t,text="9",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("9"))
b4.place(x=290,y=200)
b4=Button(t,text="-",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("-"))
b4.place(x=430,y=200)

b5=Button(t,text="4",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("4"))
b5.place(x=10,y=300)
b5=Button(t,text="5",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("5"))
b5.place(x=150,y=300)
b5=Button(t,text="6",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("6"))
b5.place(x=290,y=300)
b5=Button(t,text="+",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("+"))
b5.place(x=430,y=300)

b6=Button(t,text="1",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("1"))
b6.place(x=10,y=400)
b6=Button(t,text="2",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("2"))
b6.place(x=150,y=400)
b6=Button(t,text="3",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("3"))
b6.place(x=290,y=400)

b7=Button(t,text="0",width=11,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("0"))
b7.place(x=10,y=500)
b7=Button(t,text=".",width=5,height=1,font=("arial",30),bd=1,fg="white",bg="black",command=lambda:show("."))
b7.place(x=290,y=500)
b7=Button(t,text="=",width=5,height=3,font=("arial",30),bd=1,fg="white",bg="orange",command=lambda:calculate())
b7.place(x=430,y=400)
t.mainloop()





