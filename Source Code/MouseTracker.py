### Importing the necessary libraries ####
import numpy as np
import matplotlib.pyplot as plt
import pyautogui

class MouseTracker:

 """
    Authors : Syrine Ben Driss,Juan Carlier ,and Felipe Aguilar.
    SpartaHack 8, MSU 
    Date: Jan 29,2023
 """
# -*- coding: utf-8 -*-
# PEP 8 Standard Python Documentation

 def __init__(self):
        """
          MouseTracker constructor that initilialize x-y
          coordinates to graph
        """
        self.x_coords = []
        self.y_coords = []

 def track(self):
        """
        this behavior uses pyautogui's method to collect the mouse
        movement and store them in the initialized lists
        :return: list of ints of self.x_coords and self.x_coords
        """
        while True:
                x, y = pyautogui.position()
                self.x_coords.append(x)
                self.y_coords.append(y)
                if pyautogui.confirm(text='Do you want to stop the recording?', title='Stop Recording',
                                     buttons=['Yes', 'No']) == 'Yes':
                    break

 def plot(self):
    """
           uses the return value of the track function to produce a graph
           :return: graphs in matplot's window
           """
    x_coords = np.array(self.x_coords)
    y_coords = np.array(self.y_coords)
    plt.plot(x_coords, y_coords)
    plt.show()


if __name__ == "__main__":
        mouse_tracker = MouseTracker()
        mouse_tracker.track()
        mouse_tracker.plot()


