from tkinter import *

root = Tk() #creates instance
root.title("MP3 Player")
root.geometry("500x400")

#list box to store playlist:
#Step 1define:
playlist_box = Listbox(root, bg="black", fg="blue", width=60)

#Place on the screen:
playlist_box.pack(pady=20, padx=20)




#create main loop:
root.mainloop()