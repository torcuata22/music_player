from tkinter import *

root = Tk() #creates instance
root.title("MP3 Player")
root.geometry("500x400")

#list box to store playlist:
#Step 1define:
playlist_box = Listbox(root, bg="black", fg="blue", width=60)

#Place on the screen:
playlist_box.pack(pady=20, padx=20)

#Create button Frame (frame widget):
control_frame = Frame(root)
control_frame.pack(pady=20, padx=20)

#Create buttons
back_button = Button(control_frame, text="Back")
forward_button = Button(control_frame, text="Forward")
play_button = Button(control_frame, text="Play")
pause_button = Button(control_frame, text="Pause")
stop_button = Button(control_frame, text="Stop")

back_button.grid(row = 0, column = 0)
forward_button.grid(row = 0, column = 1)
play_button.grid(row = 0, column = 2)
pause_button.grid(row = 0, column = 3)
stop_button.grid(row = 0, column = 4)



#create main loop:
root.mainloop()