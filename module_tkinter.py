# import sys
import tkinter
import tkinter.messagebox
# from tkinter import Tk
# 初始化Tk()

'''
    參考:
    https://www.runoob.com/python/python-gui-tkinter.html
    whatever_you_do = "Only those who have the patience to do simple things per"
    msg = tkinter.Message(myWindow, text=whatever_you_do)
    msg.config(bg='lightgreen', font=('times', 20, 'italic'))
    msg.grid(row=0, column=1)
'''


def printinfo():
    print("test")
    tkinter.messagebox.showinfo(title="Tes", message="OK!")


myWindow = tkinter.Tk()
explanation = "abc"
logo = tkinter.PhotoImage(file=r"SourceFile/ima.gif")    # 格式： PGM, PPM, GIF, PNG format
'''
Label 用法： 
注意Pack / Place 
pack 只可以放在TOP or BOTTOM or LEFT or RIGHT
Place 可以指定位置
grid 網格
'''

# tkinter.Label(myWindow, image=logo).pack(side='left')
# tkinter.Label(myWindow,compound="center",text=explanation,image=logo).pack(side="right")
# tkinter.Label(myWindow, text="user-name",font=('Arial 12 bold'),width=20,height=3,padx=100, pady=50).pack()
# tkinter.Label(myWindow, text="password2",bg='green',width=20,height=3).pack(ipadx = 50, ipady = 120)
# tkinter.Label(myWindow, text="password2").pack(ipadx = 120, ipady = 120)
# label1=tkinter.Label(myWindow, text="user-name",font=('Arial 12 bold'),justify="left")
# label2=tkinter.Label(myWindow, text="password",font=('Arial 12 bold'),justify="left")
# label3=tkinter.Label(myWindow, text="user",font=('Arial 12 bold'))
# label1.place(x=5,y=5)
# label2.place(x=1,y=40)
# label3.place(x=150,y=5)
# label1.grid(row=1,column=1)
# label2.grid(row=2,column=1)
# logo2=tkinter.BitmapImage(file="SourceFile/ima.xbm")    #格式： XBM format
# tkinter.Label(myWindow, image=logo2).pack(side='left')

# 标签控件布局
tkinter.Label(myWindow, text="input").grid(row=0)
tkinter.Label(myWindow, text="output").grid(row=1)
# Entry控件布局
entry1 = tkinter.Entry(myWindow)
entry2 = tkinter.Entry(myWindow)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
# Quit按钮退出；Run按钮打印计算结果
tkinter.Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0, padx=15, pady=15)
tkinter.Button(myWindow, text='Run', command=printinfo).grid(row=2, column=1, padx=15, pady=15)

# 设置标题
myWindow.title('Python GUI (tkinter module)')
# 设置窗口大小
myWindow.geometry('380x300')
# 设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=True, height=True)

# 进入消息循环

myWindow.mainloop()
