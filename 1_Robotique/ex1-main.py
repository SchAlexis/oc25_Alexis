# Imports go at the top
from microbit import *

# Code pour compter

n=0
while True:
    if button_a.was_pressed():
        n += 1
        display.scroll(n, 50)
        
    if button_b.was_pressed():
        n -=1
        display.scroll(n, 50)
   
    if accelerometer.was_gesture('shake'):
        n=0
        display.scroll(n,50)