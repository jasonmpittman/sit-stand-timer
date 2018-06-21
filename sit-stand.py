#!/usr/bin/env python3

# Created on 06/19/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: a sit stand move timer for notifications at a standing desk
# Explanation: 
import time
import winsound

class StateTimer():
    def __init__(self):
        self.state_timer = time.time() + 2700
    
    def get_timer(self):
        return self.state_timer
    
    def set_timer(self, new_time):
        self.state_timer = new_time

class State():
    def __init__(self):
        self.state = "Sit"
        self.st = StateTimer()
    
    def change_state(self, new_state):
        self.state = new_state

        if self.state == "Stand":
            self.st = time.time() + 600
            return self.st

        if self.state == "Sit":
            self.st = time.time() + 2700
            return self.st
        
        if self.state == "Move":
            self.st == time.time() + 240
            return self.st

def main():
    
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS) #sit
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS) #stand
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) #move
    
    st = StateTimer()
    s = State()

main()