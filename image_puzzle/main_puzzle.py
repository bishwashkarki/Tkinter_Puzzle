"""
in this file iam creating a fiel that has 2x2 frames that can be moved around a empty frame

"""

#imoprt modules
import tkinter
from tkinter.constants import INSIDE
#from PIL import ImageTk, Image

#tkinter settings
win=tkinter.Tk()
win.title("IMAGE PUZZLE")
win.resizable(False, False)
win.geometry("520x520")

#checking if the button works
def frame1_exchange():
    #how to check postion
    X, Y = frame4.winfo_rootx(), frame4.winfo_rooty()
    X1, Y1 = frame1.winfo_rootx(), frame1.winfo_rooty()
    frame1.place(x=X,y=Y)
    frame4.place(x=X1,y=Y1)

def frame2_exchange():
    #how to check postion
    X, Y = frame4.winfo_rootx(), frame4.winfo_rooty()
    X1, Y1 = frame2.winfo_rootx(), frame2.winfo_rooty()
    frame1.place(x=X,y=Y)
    frame4.place(x=X1,y=Y1)

def frame3_exchange():
    #how to check postion
    X, Y = frame4.winfo_rootx(), frame4.winfo_rooty()
    X1, Y1 = frame3.winfo_rootx(), frame3.winfo_rooty()
    frame1.place(x=X,y=Y)
    frame4.place(x=X1,y=Y1)




#creating a frame
#postion=x=700,y=100
frame1=tkinter.LabelFrame(win)
frame1.place(x=0,y=0,bordermode=INSIDE,height=260, width=260)
# 2 
frame2=tkinter.LabelFrame(win)
frame2.place(x=0,y=250,bordermode=INSIDE,height=260, width=260)
# 3
frame3=tkinter.LabelFrame(win)
frame3.place(x=250,y=0,bordermode=INSIDE,height=260, width=260)
# 4
frame4=tkinter.LabelFrame(win)
frame4.place(x=250,y=250,bordermode=INSIDE,height=260, width=260)

#image_size= 500x500
"""
background=tkinter.PhotoImage(file="main_image.jpg")
"""
#setting images
image1=tkinter.PhotoImage(file="images/GIF/main_image_top_left.gif")
image2=tkinter.PhotoImage(file="images/GIF/main_image_top_right.gif")
image3=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image4=tkinter.PhotoImage(file="images/GIF/main_image_bottom_right.gif")

#running=True
#while running:
#button1
button1= tkinter.Button(frame1, image=image1, command=frame1_exchange)
button1.grid()
#button2
button2= tkinter.Button(frame2, image=image2, command=frame2_exchange)
button2.grid()
#button3
button3= tkinter.Button(frame3, image=image3, command=frame3_exchange)
button3.grid()
#button4
button4= tkinter.Button(frame4, image=image4)
button4.grid()







win.mainloop()
