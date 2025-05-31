import tkinter

root = tkinter.Tk()

tmr = 0
def countUp():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(100, countUp)

root.title("타이머")
root.geometry("300x200")

label = tkinter.Label(text=tmr, font=("궁서체", 80))
label.pack()

root.after(100, countUp)

root.mainloop()