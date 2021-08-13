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
    xDoToolCommands = ["xdotool click 1",
        "xdotool type 'tempo'",
        "xdotool key Return",
        "xdotool key Tab", 
        "xdotool key Tab",
        "xdotool key Tab",
        "xdotool key Tab",
        "xdotool type 7,5",
        "xdotool key Return",
        "xdotool key Tab",
        "xdotool key Tab",
        "xdotool key Return"]
    for c in xDoToolCommands:
        os.system(c)
        time.sleep(0.2)


if __name__ == "__main__":
    for p in logTimePoints:
        os.system("xdotool mousemove {} {}".format(p.x,p.y))
        logTime()
        time.sleep(1)


