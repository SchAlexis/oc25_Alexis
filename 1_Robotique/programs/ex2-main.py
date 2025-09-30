''' 
Alexis Schmid 
21 aout 2025
code démonstration avec 10 programes
 bouton a : incrémenter le programme
 bouton b : executer
0 - dessine un coeur
1 - écrit "hi!"
2
3
4
5
6
7
8
9

'''


# Imports go at the top
from microbit import *
import music
import speech
import random
# programe 0 

p=0
# le bouton a choisi le programme 
while True:
    display.show(p)
    if button_a.was_pressed():
        p = p + 1
        if p == 10:
            p=0
# le bouton b execute
    if button_b.is_pressed():
        if p == 0:
            display.show(Image.HEART)
            sleep(1000)
        if p == 1:
            display.scroll('hi!')
        if p == 2:
            display.scroll('Random',50)
            display.show(random.randint(1, 6))
            sleep(1000)
        if p == 3:
            display.show(Image('90009:'
                               '99099:'
                               '94949:'
                               '94949:'
                               '09990'))
        if p == 4:
            speech.say('fantasic')
        if p == 5:
            music.play(music.CHASE)
        if p == 6:
            display.scroll('temperature', 50)
            display.scroll(temperature(),50)
        if p ==7:
            display.scroll('boussole', 50)
            display.scroll(compass.heading())
        if p == 8:
            display.show(Image.DUCK)
            sleep(1000)
        if p == 9:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
            sleep(1000)
