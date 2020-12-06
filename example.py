#!/usr/bin/env python3
from tkinter import *
from auzoom import ZoomClient

z = ZoomClient()
root = Tk()
root.resizeable = False
z = ZoomClient()

meeting = Button(root, text="start meeting", padx=40, pady=20, command=z.start_meeting)
mic = Button(root, text="mute / unmute", padx=40, pady=20, command=z.mic)
camera = Button(root, text="camera on / off", padx=40, pady=20, command=z.camera)

meeting.pack()
mic.pack()
camera.pack()
root.mainloop()
