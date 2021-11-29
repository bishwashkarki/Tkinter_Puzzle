"""
in this file iam creating a fiel that has 2x2 frames that can be moved around a empty frame

"""

#imoprt modules
import tkinter
from PIL import ImageTk, Image

#tkinter settings
win=tkinter.Tk()
win.title("IMAGE PUZZLE")
win.resizable(False, False)
win.geometry("500x500")

#checking if the button works
def print_if_it_works():
    print("yes it works")


#creating a frame
#postion=x=700,y=100
frame1=tkinter.LabelFrame(win)
frame1.grid(row=1,column=0)
# 2 
frame2=tkinter.LabelFrame(win)
frame2.grid(row=1,column=0)
# 3
frame3=tkinter.LabelFrame(win)
frame3.grid(row=0,column=1)
# 4
frame4=tkinter.LabelFrame(win)
frame4.grid(row=1,column=1)

#image_size= 3126x5000
pic=Image.open("images/front_image1.gif")

#resizing the pic 
resized_pic=pic.resize((250,250), Image.ANTIALIAS)

running=True
while running:
    #setting up image to frame
    image1= ImageTk.PhotoImage(resized_pic)
    #button1
    button1= tkinter.Button(frame1, image=image1, command=print_if_it_works)
    button1.grid()
    #button2
    button1= tkinter.Button(frame2, image=image1, command=print_if_it_works)
    button1.grid()
    #button3
    button1= tkinter.Button(frame3, image=image1, command=print_if_it_works)
    button1.grid()
    #button4
    #button1= tkinter.Button(frame4, image=image1, command=print_if_it_works)
    #button1.grid()










win.mainloop()