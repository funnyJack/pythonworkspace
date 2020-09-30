from tkinter import *
from tkinter.filedialog import askopenfilename
import app

T = Tk()
T.geometry('500x145+400+200')
T.title("图片识别")

frame = Frame(T)
frame.pack(padx=10, pady=10)  # 设置外边距
frame1 = Frame(T)
frame1.pack(padx=10, pady=10)
frame2 = Frame(T)
frame2.pack(padx=10, pady=10)

v = StringVar()
a = StringVar()


# 训练参数
def train():
    with open('train.py', 'r', encoding='utf-8')as f:
        exec(f.read())


def fileopen():
    v.set('')  # 清除文本框
    a.set('')
    file_name = askopenfilename()
    if file_name:
        v.set(file_name)
        app.prepic(file_name)


def run():
    b = app.result()
    a.set(b)


ent = Entry(frame, width=50, textvariable=v).pack(fill=X, side=RIGHT)  # X方向填充，靠右
btn = Button(frame, width=20, text='选择文件', command=fileopen).pack(fill=X, padx=10)
shw = Entry(frame1, width=50, textvariable=a, state=DISABLED).pack(fill=X, side=RIGHT)
lab = Label(frame1, width=20, text='识别结果:').pack(fill=X, padx=10)
tri = Button(frame2, width=10, text='训练参数', command=train).pack(fill=Y, side=LEFT)
ext = Button(frame2, width=10, text='运行', command=run).pack(fill=Y, side=LEFT)
etb = Button(frame2, width=10, text='退出', command=sys.exit).pack(fill=Y, padx=10)

mainloop()
