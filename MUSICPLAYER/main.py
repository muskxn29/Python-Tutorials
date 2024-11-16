from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("music player ")
root.geometry('400x550')
root.configure(bg="#a8325f")


heading1 = Label(root, text="welcome", font=("bold", 12 , "italic", "underline" ), bg="#a8325f" , fg="white")
heading1.pack()



musicframe = Frame(root, bg="#a8325f")

lab1= Label(musicframe, text="------MUSIC PLAYER------ ", bg="#a8325f", fg="white", font=("arial", 20, ))
lab1.pack( pady=(0, 10))

img = Image.open("music.jpg")
resimg = img.resize((300, 300))
newimg = ImageTk.PhotoImage(resimg)

labimg = Label(musicframe, image=newimg, bg="#a8325f")
labimg.pack( pady=30)


musicframe.pack(pady=(10,35))
musicframe.pack_propagate(False)
musicframe.configure(height=400, width=450)



root.mainloop()




