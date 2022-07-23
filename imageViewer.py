from tkinter import *
from PIL import ImageTk, Image
from pyparsing import col

root=Tk()
root.title("Image Viewer")

img1 = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/Image Viewer App/index.jpg"))
img2 = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/Image Viewer App/kapt3.png"))
img3 = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/Image Viewer App/AdobeStock.jpeg"))


image_list = [img1,img2,img3]

my_label = Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)


def forward(image_num):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])

    btn_forward = Button(root,text=">>",command=lambda: forward(image_num+1))
    btn_back = Button(root,text="<<",command=lambda: back(image_num-1))

    if image_num == 3:
        btn_forward=Button(root,text=">>",state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)

    btn_back.grid(row=1,column=0)
    btn_forward.grid(row=1,column=2)

def back(image_num):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])

    btn_forward = Button(root,text=">>",command=lambda: forward(image_num+1))
    btn_back = Button(root,text="<<",command=lambda: back(image_num-1))

    my_label.grid(row=0,column=0,columnspan=3)

    if image_num == 1:
        btn_back=Button(root,text="<<",state=DISABLED)

    btn_back.grid(row=1,column=0)
    btn_forward.grid(row=1,column=2)


btn_back = Button(root,text="<<",command=back(2))
btn_exit = Button(root,text="EXIT",command=root.quit)
btn_forward = Button(root,text=">>",command=lambda: forward(2))

btn_back.grid(row=1,column=0)
btn_exit.grid(row=1,column=1)
btn_forward.grid(row=1,column=2)

root.mainloop()