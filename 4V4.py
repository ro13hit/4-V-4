from tkinter import *
root=Tk()
root.title("REDEFINED TIC TAC TOE")
import tkinter.messagebox
root.configure(bg="#192226")
img=PhotoImage(file="zero.PNG")
img1=PhotoImage(file="cross.PNG")
win=[{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{1,5,9,13},{2,6,10,14},{3,7,11,15},{4,8,12,16},{1,6,11,16},{4,7,10,13}]
def result(t):
    global flag
    for s in win:
        if s<=t:
            return True
    else:
        return False
def Start():
    start["state"]="disable"
    for i,b in enumerate(bl,1):
        b["command"]=lambda x=i:pl1(x) if flag==True else pl2(x)
        b["state"]="active"
        lable2["text"]="TURN OF PLAYER 1"
        lable3["text"]="Turn 1"
        lable1["text"]=""
def pl1(x):
    global flag
    global c
    global pl
    global lable1
    bl[x-1]["image"]=img1
    bl[x-1]["height"]=170
    bl[x-1]["width"]=170
    lable2["text"]="TURN OF PLAYER 2"
    flag=False
    bl[x-1]["state"]="disable"
    c=c+1
    s="Turn "+str(c)
    lable3["text"]=s
    pl.add(x)
    if c>=8:
        a=result(pl)
        if a==True:
            lable2["text"]=""
            lable3["text"]="GAME OVER *_*"
            tkinter.messagebox.showinfo("Result","CONGRATS PLAYER 1 YOU WON!!")
            lable3["text"]=""
            main()
            return
    if c==17:
        lable2["text"]=""
        lable3["text"]="GAME OVER *_*"
        tkinter.messagebox.showinfo("Result","GAME RESULTED IN TIE")
        lable3["text"]=""
        main()
def pl2(x):
    global flag
    global c
    global p2
    global lable1
    bl[x-1]["image"]=img
    bl[x-1]["height"]=170
    bl[x-1]["width"]=170
    bl[x-1]["state"]="disable"
    c=c+1
    s="Turn "+str(c)
    lable2["text"]="PLAYER 1 YOUR TURN"
    lable3["text"]=s
    flag=True
    p2.add(x)
    if c>=8:
        a=result(p2)
        if a==True:
            lable2["text"]=""
            lable3["text"]="GAME OVER *_*"
            tkinter.messagebox.showinfo("Result","CONGRATS PLAYER 2 YOU WON!!")
            lable3["text"]=""
            main()
            return
    if c==17:
        lable2["text"]=""
        lable3["text"]="GAME OVER *_*"
        tkinter.messagebox.showinfo("Result","GAME RESULTED IN TIE")
        lable3["text"]=""
        main()

def main():
    global flag
    global c
    global pl
    global p2
    flag=True
    pl=set()
    p2=set()
    c=1
    global bl
    global start
    global lable1
    global lable2
    global lable3
    lable3=Label(root,text="THE 4V4",font=('arial',20,"bold"),fg ="#64F5EA",bg="#192226")
    lable3.grid(row=0,column=1,padx=5,pady=5)
    bl=[]
    for i in range(4):
        for j in range(4):
            bl.append(Button(root,height=4,state="disable",width =9,font=('arial',20,"bold"),fg="#192226"))
            bl[-1].grid(row=i+1,column=j,padx=5,pady=5)
    start=Button(root,text="PLAY",font=('arial',10,"bold"),width=13,height=1,bg ="#64F5EA",fg="#192226",command=Start)
    start.grid(row=0,column=2,padx=5,pady=5)
    lable1=Label(root,text="HIT THE PLAY",font=('arial',10,"bold"),fg ="#64F5EA",bg="#192226")
    lable2=Label(root,text="BUTTON TO BEGIN",font=('arial',10,"bold"),fg ="#64F5EA",bg="#192226")
    lable1.grid(row=0,column=0,padx=5,pady=5)
    lable2.grid(row=0,column=3,padx=5,pady=5)
main()
root.mainloop()
