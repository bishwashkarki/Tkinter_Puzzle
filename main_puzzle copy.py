"""
in this file iam creating a fiel that has 2x2 frames that can be moved around a empty frame

"""

#imoprt modules
import tkinter
from tkinter.constants import *
#from PIL import ImageTk, Image

#tkinter settings
win=tkinter.Tk()
win.title("IMAGE PUZZLE")
win.resizable(True, True)
win.geometry("520x520")

#checking if the button works
#def frame1_exchange(pos1,pos2):
#    #how to check postion
#    X = pos2.winfo_rootx()
#    Y = pos2.winfo_rooty()
#    X1 = pos2.winfo_rootx()
#    Y1 = pos2.winfo_rooty()
#    pos1.place(x=X,y=Y)
#    pos2.place(x=X1,y=Y1)


#checking if the button works
def frame1_exchange():
    #how to check postion
    X, Y = button4.winfo_rootx(), button4.winfo_rooty()
    X1, Y1 = button1.winfo_rootx(), button1.winfo_rooty()
    button1.place(x=X,y=Y)
    button4.place(x=X1,y=Y1)

def frame2_exchange():
    #how to check postion
    X, Y = button4.winfo_rootx(), button4.winfo_rooty()
    X1, Y1 = button2.winfo_rootx(), button2.winfo_rooty()
    button2.place(x=X,y=Y)
    button4.place(x=X1,y=Y1)

def frame3_exchange():
    #how to check postion
    X, Y = button4.winfo_rootx(), button4.winfo_rooty()
    X1, Y1 = button3.winfo_rootx(), button3.winfo_rooty()
    button3.place(x=X,y=Y)
    button4.place(x=X1,y=Y1)


#image_size= 500x500
"""
background=tkinter.PhotoImage(file="main_image.jpg")
"""
#setting images
image1=tkinter.PhotoImage(file="images/GIF/main_image_top_left.gif")
image2=tkinter.PhotoImage(file="images/GIF/main_image_top_right.gif")
image3=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image4=tkinter.PhotoImage(file="images/GIF/white250.gif")

#running=True
#while running:
#button1
button1= tkinter.Button(win, image=image1, command=frame1_exchange)
button1.grid(row=0,column=0)
#button2
button2= tkinter.Button(win, image=image2, command=frame2_exchange)
button2.grid(row=1,column=0)
#button3
button3= tkinter.Button(win, image=image3, command=frame3_exchange)
button3.grid(row=0,column=1)
#button4
button4= tkinter.Button(win, image=image4)
button4.grid(row=1,column=1)







win.mainloop()