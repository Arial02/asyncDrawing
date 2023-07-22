import random
import threading
import tkinter
from tkinter import ttk
import ctypes
from time import sleep

LEFT = 10
TOP = 10
BOTTOM = 340
RIGHT = 540
SLEEP_TIME = 0.2

def doChaos(funcs, is_run):
    while is_run():
        #random.choice(funcs)()
        threading.Thread(target=random.choice(funcs)).start()
        sleep(SLEEP_TIME)

def z13line(y):
    return -(11/7)*y+550

def z23line(y):
    return (11/7)*y

ISCHAOS = False
thread = threading.Thread()

def main():
    def zone1():
        tag = f'p1o{str(random.randint(0,999999)).zfill(6)}'
        yr = random.randint(TOP,BOTTOM)
        xr = random.randint(LEFT,int(z13line(yr))) if yr > 175 else random.randint(LEFT,375)
        for i in range(10):
            canvas.create_oval(xr-i, yr-i, xr+i, yr+i, fill='#FFFF00', tags=tag)
            root.update()
            sleep(SLEEP_TIME)
            canvas.delete(tag)
    def zone2():
        tag = f'p2o{str(random.randint(0, 999999)).zfill(6)}'
        yr = random.randint(TOP,BOTTOM)
        xr = random.randint(int(z23line(yr)), RIGHT) if yr > 175 else random.randint(375,RIGHT)
        for i in range(10):
            canvas.create_oval(xr - i, yr - i, xr + i, yr + i, fill='#FF0000', tags=tag)
            root.update()
            sleep(SLEEP_TIME)
            canvas.delete(tag)
    def zone3():
        tag = f'p3o{str(random.randint(0, 999999)).zfill(6)}'
        yr = random.randint(175, BOTTOM)
        xr = random.randint(int(z13line(yr)), int(z23line(yr)))
        for i in range(10):
            canvas.create_oval(xr - i, yr - i, xr + i, yr + i, fill='#008000', tags=tag)
            root.update()
            sleep(SLEEP_TIME)
            canvas.delete(tag)
    def chaos():
        global ISCHAOS
        global thread
        if not ISCHAOS:
            ISCHAOS = True
            bt1.config(state=tkinter.DISABLED)
            bt2.config(state=tkinter.DISABLED)
            bt3.config(state=tkinter.DISABLED)
            thread = threading.Thread(target=doChaos, args=((zone1, zone2, zone3), lambda: ISCHAOS))
            thread.start()
        else:
            ISCHAOS = False
            bt1.config(state=tkinter.NORMAL)
            bt2.config(state=tkinter.NORMAL)
            bt3.config(state=tkinter.NORMAL)
    root = tkinter.Tk()
    root.title('NOasyncioLSN')
    root.eval('tk::PlaceWindow . center')

    mainFrame = ttk.Frame(root)
    mainFrame.pack(fill=tkinter.Y)
    canvas = tkinter.Canvas(mainFrame, bg='white', width=550, height=350)
    canvas.pack(side=tkinter.TOP)
    canvas.create_line(0, 350, 275, 175)
    canvas.create_line(550, 350, 275, 175)
    canvas.create_line(275, 0, 275, 175)


    buttonFrame = ttk.Frame(root, borderwidth=1, relief=tkinter.RAISED)
    buttonFrame.pack(side=tkinter.BOTTOM)

    bt1 = ttk.Button(buttonFrame, text='1', command=lambda: zone1(), width=15)
    bt1.grid(row=0, column=4)
    bt2 = ttk.Button(buttonFrame, text='2', command=lambda: zone2(), width=15)
    bt2.grid(row=0, column=5)
    bt3 = ttk.Button(buttonFrame, text='3', command=lambda: zone3(), width=15)
    bt3.grid(row=0, column=6)
    bt4 = ttk.Button(buttonFrame, text='Chaotic', command=chaos, width=25)
    bt4.grid(row=0, column=7, columnspan=2)

    root.mainloop()


if __name__ == '__main__':
    main()