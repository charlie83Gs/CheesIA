import tkinter
from tkinter import *
from PIL import ImageTk, Image


class data:
    def __init__(self):
        self.title = "ChessIA"
        self.resolution = "1000x800"
        self.logopath = "./ChessArt/logo.jpg"
        self.backgroundColor = "white"

class mainUiApp:
    def run(self):
        window = tkinter.Tk()
        self.data = data()
        window.title(self.data.title)
        window.geometry(self.data.resolution)
        window.configure(background=self.data.backgroundColor)

        img = ImageTk.PhotoImage(Image.open(self.data.logopath))
        panel = Label(window, image=img)
        panel.place(x=315, y=5, width=370, height=206)
        window.mainloop()




if __name__ == '__main__':
        app = mainUiApp()
        app.run()