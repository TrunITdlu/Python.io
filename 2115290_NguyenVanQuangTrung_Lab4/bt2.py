from tkinter import Tk, Label, BOTH,Frame
from tkinter.ttk import Style
from PIL import Image, ImageTk

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open(r"D:\2115290_NguyenVanQuangTrung_Lab4\landscape-photography_1645.jpg")
        bard = bard.resize((100,100), Image.LANCZOS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)



root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()