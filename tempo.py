#!/usr/bin/python3

import os
import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


logTimeHeight = 310

logTimePoints = [Point(175, logTimeHeight), Point(395, logTimeHeight), Point(615, logTimeHeight), Point(835, logTimeHeight), Point(1055, logTimeHeight)]

def logTime():
    os.system("xdotool click 1")
    time.sleep(1)
    os.system("xdotool type 'tempo'")
    time.sleep(1)
    os.system("xdotool key Return")
    time.sleep(1)
    os.system("xdotool key Tab")
    time.sleep(1)
    os.system("xdotool key Tab")
    os.system("xdotool key Tab")
    os.system("xdotool key Tab")
    time.sleep(1)
    os.system("xdotool type 7,5")    
    os.system("xdotool key Return")
    time.sleep(1)
    os.system("xdotool key Tab")
    os.system("xdotool key Tab")
    os.system("xdotool key Return")


if __name__ == "__main__":
    for p in logTimePoints:
        os.system("xdotool mousemove {} {}".format(p.x,p.y))
        time.sleep(1)
        logTime()

