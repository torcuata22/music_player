from tkinter import *
from tkinter import filedialog

root = Tk() #creates instance
root.title("MP3 Player")
root.geometry("500x500")

#Create add song function:
def add_song():
    song = filedialog.askopenfilename()
    pass
#Create add many songs function:
def add_many_song():
    pass




#list box to store playlist:
#Step 1define:
playlist_box = Listbox(root, bg="black", fg="blue", width=60)

#Place on the screen:
playlist_box.pack(pady=40, padx=20)

#Create button Frame (frame widget):
control_frame = Frame(root)
control_frame.pack(pady=20, padx=10)

#Button images (controls):
back_btn_img = PhotoImage(file = 'images/back_button.png').subsample(7) #need to find buttons that are 50px by 50px
fwd_btn_img = PhotoImage(file = 'images/forward_button.png').subsample(7)
play_btn_img = PhotoImage(file = 'images/play_button.png').subsample(7)
pause_btn_img = PhotoImage(file = 'images/pause_button.png').subsample(7)
stop_btn_img = PhotoImage(file = 'images/stop_button.png').subsample(7)

#Create buttons
back_button = Button(control_frame, image = back_btn_img, borderwidth = 0, highlightthickness=0)
forward_button = Button(control_frame, image = fwd_btn_img, borderwidth = 0, highlightthickness=0)
play_button = Button(control_frame, image = play_btn_img, borderwidth = 0, highlightthickness=0)
pause_button = Button(control_frame, image = pause_btn_img, borderwidth = 0, highlightthickness=0)
stop_button = Button(control_frame, image = stop_btn_img, borderwidth = 0, highlightthickness=0)
#borders still showing despite borderwidtj=0, highlightthickness = 0


# Set border color to the same gray as the canvas background --doesn't work either
border_color = control_frame.cget('bg')  # Get the background color of the frame
back_button.configure(highlightbackground=border_color, highlightcolor=border_color)
forward_button.configure(highlightbackground=border_color, highlightcolor=border_color)
play_button.configure(highlightbackground=border_color, highlightcolor=border_color)
pause_button.configure(highlightbackground=border_color, highlightcolor=border_color)
stop_button.configure(highlightbackground=border_color, highlightcolor=border_color)


back_button.grid(row = 0, column = 0)
forward_button.grid(row = 0, column = 1)
play_button.grid(row = 0, column = 2)
pause_button.grid(row = 0, column = 3)
stop_button.grid(row = 0, column = 4)

#Create Menu:
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdown
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
#Add one song to Playlist
add_song_menu.add_command(label="Add One Song to Playlist", command = add_song)
#Add many songs to Playlist:
add_song_menu.add_command(label="Add Songs to Playlist", command = add_many_song)






#create main loop:
root.mainloop()