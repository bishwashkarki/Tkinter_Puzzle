"""
in this file iam creating a fiel that has 2x2 frames that can be moved around a empty frame

"""

#imoprt modules
import tkinter
#from PIL import ImageTk, Image

#tkinter settings
win=tkinter.Tk()
win.title("IMAGE PUZZLE")
win.resizable(True, True)
win.geometry("520x520")

#checking if the button works
def print_if_it_works():
    print("yes it works")


#creating a frame
#postion=x=700,y=100
frame1=tkinter.LabelFrame(win)
frame1.place(x=0,y=0)
# 2 
frame2=tkinter.LabelFrame(win)
frame2.place(x=0,y=250)
# 3
frame3=tkinter.LabelFrame(win)
frame3.place(x=250,y=0)
# 4
frame4=tkinter.LabelFrame(win)
frame4.place(x=250,y=250)

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
button1= tkinter.Button(frame1, image=image1, command=print_if_it_works)
button1.place()
#button2
button1= tkinter.Button(frame2, image=image2, command=print_if_it_works)
button1.place()
#button3
button1= tkinter.Button(frame3, image=image3, command=print_if_it_works)
button1.place()
#button4
#button1= tkinter.Button(frame4, image=image4, command=print_if_it_works)
#button1.place()










win.mainloop()
