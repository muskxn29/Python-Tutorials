from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

root = Tk()
root.title("Music Player")
root.geometry('400x550')
root.configure(bg="#480982")

######################FUNCTIONS###########################

mixer.init() # initialiing mixer
# mixer.music.load("")

def resume_music():
    resumebtn.configure(text=" ▶ ")
    resumebtn.configure(command=pause_music)

def pause_music():
    resumebtn.configure(text=" || ")
    resumebtn.configure(command=resume_music)


#######################################################





headlab = Label(root, text="Music Player", font=("bold", 20, "italic"), bg="#480982", fg="white")
headlab.pack()


musicframe = Frame(root, bg="#821b09")

# lab = Label(musicframe, text="PLay a Music", bg="red", font=("bold", 15))
# lab.pack(side=BOTTOM, pady=(0, 10))

img = Image.open('musicimg.png')
resimg = img.resize((300, 300))
newimg = ImageTk.PhotoImage(resimg)

labimg = Label(musicframe, image=newimg, bg="#821b09")
labimg.pack(anchor=CENTER, pady=30)

musicframe.pack(pady=(10,35))
musicframe.pack_propagate(False)
musicframe.configure(height=300, width=350)


#################BUTTONS FRAME################
buttonframe = Frame(root, bg="white")

resume_frame = Frame(buttonframe,  highlightbackground='#480982', highlightthickness=1)
resumebtn = Button(resume_frame, text=" ▶ ", font=("bold", 17), command=pause_music)
resumebtn.pack()
resume_frame.place(x=155, y=50)

# pause_frame = Frame(buttonframe,  highlightbackground='#480982', highlightthickness=1)
# pausebtn = Button(pause_frame, text=" || ", font=("bold", 17)).pack()
# pause_frame.place(x=100, y=50)

rewind_frame = Frame(buttonframe,  highlightbackground='#480982', highlightthickness=1)
rewindbtn = Button(rewind_frame, text=" <<< ", font=("bold", 17)).pack()
rewind_frame.place(x=40, y=50)


next_frame = Frame(buttonframe,  highlightbackground='#480982', highlightthickness=1)
nextbtn = Button(next_frame, text=" >>> ", font=("bold", 17)).pack()
next_frame.place(x=250, y=50)

buttonframe.pack()
buttonframe.pack_propagate(False)
buttonframe.configure(height=160, width=350)
##############################################

root.mainloop()




