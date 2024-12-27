from tkinter import*
total=0
def order():
        global total
        total+= x.get()
        print(total)

        l.config(text=f"Le prix total est {total} DH", fg="#3B4C42",bg="#C5E6D3",
              font=("arial",25,"bold"))

    
def finition():
      l=Label
      print(f"total is {total}DH")
      l1.config(text=f"c'est fini! le prix total est {total} DH",
              fg="#25201F",bg="#FE876C",font=("arial",50,"bold"))
      b.config(state=DISABLED)
      


menue=[("pizza",40),("tacos",49),("sandwich",30),("burger",32),
       ("frites",15),("nuggets",35),("soda",15),("limonade",18)]

s=Tk()
s.title("snack")
l1=Label(s,text="Menu de nos restaurant",font=('arial',30,'bold'),bg="#2BC994",fg="#1966E2")
l1.pack()
x=IntVar()
for plat, i in menue:
    y = Radiobutton(s, text=f"{plat} {i} DH"
                    , variable=x, value=i, indicatoron=0
                    , width=375, command=order)
    y.pack(anchor=W,pady=10)

b=Button(s,text="finir",font=("arial",25,"bold"),command=finition,bg="#F61717",fg="#020101")
b.pack(pady=10)

l=Label(s)
l.pack(pady=10)

l1=Label(s)
l1.pack(pady=10)



s.mainloop()