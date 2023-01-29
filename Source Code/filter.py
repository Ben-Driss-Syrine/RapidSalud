import pyautogui
import keyboard
import time
import tkinter as tk
from PIL import Image, ImageTk


start = False
pyautogui.FAILSAFE=False


positions = []
FILTER_SIZE = 10


# Create a new Tkinter window and set the cursor to be invisible
root = tk.Tk()
root.config(cursor="none")


#give size of tkinter
(x,y) = pyautogui.size()


root = tk.Tk()
root.config(width=x, height=y)


# Create a new Tkinter label to hold the image  (doesn't work)
image = Image.open("/Users/User/Desktop/MSU/CSE 231/Parkinson's/cursor.png")
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=image)
label.pack()


def stabilize_mouse():
    global FILTER_SIZE
    x, y = pyautogui.position() #initial position
    positions.append((x, y))
    if len(positions) > FILTER_SIZE:
        positions.pop(0)


    #movement position
    smoothed_x = sum(x for x, y in positions) / len(positions)
    smoothed_y = sum(y for x, y in positions) / len(positions)
 # Move the label to the smoothed position
    label.place(x=smoothed_x, y=smoothed_y)


    if abs(x-smoothed_x) > 10 and abs(y-smoothed_y) > 10: #if the movement is to big, the repositioning will be bigger
        FILTER_SIZE = 30
    else:
        FILTER_SIZE = 10


    time.sleep(0.01)


# Run the Tkinter main loop to display the window and start the event loop
root.mainloop()


while not start:


    stabilize_mouse()


    if keyboard.is_pressed('esc'):
        print('Finish')
        start = True