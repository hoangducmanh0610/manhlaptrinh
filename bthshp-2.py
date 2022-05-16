import tkinter
from tkinter import messagebox
tk=Tk()
tk.title('Khai bao')
tk.geometry("250x80+600+250")
tk.configure(bg='yellow')
l1=Label(tk,text="Tên")
l1.grid(row =0, column =0)
l1.configure(fg='black',bg="yellow")
e1=Entry(tk)
e1.grid(row=0,column=1)
l2=Label(tk,text="Mật khẩu")
l2.grid(row=1,column=0)
l2.configure(fg="black",bg="yellow")
e2=Entry(tk)
e2.grid(row=1,column=1)

def nhan():
    r1=e1.get()
    r2=e2.get()
    if r1=='Đinh Văn Ngãi'and r2=="205752021610045" :
        messagebox.showinfo('Thông báo','Thông tin đúng!')
    else:
        messagebox.showinfo('Thông báo','Thông tin sai!\n Vui lòng nhập đúng!')
        
nut=Button(tk,text="Xác nhận",command=nhan)
nut.grid(row=3,column=0)

tk.mainloop()
