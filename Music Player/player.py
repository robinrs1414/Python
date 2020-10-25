from tkinter import *
import pygame 
import os

# Music Player class
class MusicPlayer:

    # defining constructor
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")  # Title of window
        self.root.geometry("100x200+200+200")  # Window Geometry 
        pygame.init() # Initialize pygame
        pygame.mixer.init() # Initialize pygame mixer
        self.track = StringVar() # Declaring track variable
        self.status = StringVar() # Declaring status variable

        # creating track frame for song label
        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)

        # inserting song track label
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)

        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=400,height=200)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("F:\MUSIC") # where mp3 songs are saved
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
          self.playlist.insert(END,track)


    # Defining play song function
    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE)) # Displaying selected song title
        self.status.set("-Playing") # Displaying status 
        pygame.mixer.music.load(self.playlist.get(ACTIVE)) # Loading song
        pygame.mixer.music.play() #playing song

    def stopsong(self):
        self.status.set("-Stops") # Displaying status
        pygame.mixer.music.stop() # Stop playing

    def pausesong(self):
        self.status.set("-Pauses") # Displaying status
        pygame.mixer.music.pause() 

    def unpausesong(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()


root = Tk()
MusicPlayer(root)
root.mainloop()