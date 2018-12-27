
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter.filedialog import askopenfilename
from PIL import ImageTk
from PIL import  Image as IM
from tkinter import *
import classifier.vgg.classify as classify
import classifier.vgg.segment as segment
import pathlib
from tkinter import messagebox
from colorize.reference.pb_colorizer import colorize as CL

class ColorizeMain:

    def __init__(self):
        self.top = tkinter.Toplevel()
        menu = Menu(self.top)
        self.top.config(menu=menu)

        file = Menu(menu)

        file.add_command(label='Open', command=self.open_file)
        file.add_command(label='colorize', command=self.colorize)
        file.add_command(label='classify', command=self.classify)
        file.add_command(label='Exit', command=lambda: exit())

        menu.add_cascade(label='File', menu=file)
        self.top.mainloop()
    def open_file(self):
            self.name = askopenfilename(initialdir="../images",
                                   filetypes =(("image", "*.jpg"),("All Files","*.*")),
                                   title = "Choose a file."
                                   )
            pi = IM.open(self.name)
            pi = pi.resize((300, 200), IM.ANTIALIAS)
            self.originalImage = pi
            img = ImageTk.PhotoImage(pi)
            panel = tkinter.Label(self.top, image=img)
            panel.image = img
            panel.pack(side="bottom", fill="both", expand="yes")
            self.imgl = panel;


    def colorize(self):

        colorized = CL(self.name, self.originalImage)
        img = ImageTk.PhotoImage(IM.open(colorized))
        panel = tkinter.Label(self.top, image=img)

        panel.image = img
        panel.pack(side="bottom", fill="both", expand="yes")
    def classify(self):
        url = pathlib.Path(self.name).as_uri()
        rst = classify.classify(url)

        messagebox.showinfo('result: ', rst)

    def segment(self):
        url = pathlib.Path(self.name).as_uri()
        rst = segment.segmentIt(url)
# colorizer = colorizer.Colorizer()
# colorizer.exportModel()
# cls = CLS.VggClassifier()
# url = ("https://upload.wikimedia.org/wikipedia/commons/d/d9/"
#            "First_Student_IC_school_bus_202076.jpg")
#
# pos, name = cls.classify(url)
ColorizeMain()
#This is where we lauch the file manager bar.
