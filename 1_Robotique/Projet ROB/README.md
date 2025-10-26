# Projet robotique
option complémentaire en informatique du gymnase du Bugnon

## Description
Dans ce projet nous programmons le robot Kitronik MOVE avec une parite obligatoire et une partie libre.

![](images/images.jpg)
Entièreter du code ci-dessous :
```
from microbit import *
from machine import time_pulse_us
import KitronikMOVEMotor
import music
import radio
import random 

g = 7
display.scroll(g)
radio.on()
radio.config(group=g)

trigger = pin13
echo = pin14

robot = KitronikMOVEMotor.MOVEMotor()
robot.move(0, 0)

trigger.write_digital(0)
echo.read_digital()
robot.move(0, 0)

prog = 0 
display.show(prog)

def avancer():
    robot.move(-60,-60,500)
def reculer():
    robot.move(60,60,500)
def droite():
    robot.move(60,-60,500)
def gauche():
    robot.move(-60,60,500)
def ouvre():
    robot.goToPosition(1, 160)
def ferme():
    robot.goToPosition(1, 20)

def distance_cm():
    left = pin1.read_analog()
    right = pin2.read_analog()
    d = (left - right)
    d = d // 10
    robot.move(15 - d, 15 + d)
    trigger.write_digital(1)
    trigger.write_digital(0)
    distance = time_pulse_us(echo, 1)/58.
    return round(distance)

    
while True:
    
    if button_a.was_pressed():
        robot.move(0, 0)
        prog = (prog + 1) % 10
        display.show(prog, 1000)
        music.pitch(440, 20)

    if prog == 0:
        msg = radio.receive()
        if msg:
            display.show(msg)
            if msg == '0':
                robot.move(0, 0)
            elif msg == 'u':
                robot.move(-80, -80)
            elif msg == 'r':
                robot.move(80, -80)
            elif msg == 'l':
                robot.move(-80, 80)
            elif msg == 'd':
                robot.move(80, 80)
            elif msg == '2':
                robot.goToPosition(1, 20)
            elif msg == '1':
                robot.goToPosition(1, 160)

    
    if prog == 1:

        d = distance_cm()
        for i in range(25):
            if i < d:
                display.set_pixel(i//5, i%5, 9)
            else:
                display.set_pixel(i//5, i%5, 0)
    
        if d <= 10:
            robot.move(0, 0, 1000)
            robot.move(-60, -60, 500)
            robot.goToPosition(1, 160)
            robot.move(60, -60, 1250)
            robot.move(-60, -60, 750)
            display.show(Image('09090:'
                           '09090:'
                           '00000:'
                           '90009:'
                           '09990'))

            #audio.play(Sound.SPRING)
            robot.move(0, 0)
            sleep(1000)
            robot.goToPosition(1, 20)
            robot.move(60, -60, 1250)

    if prog == 2:
        msg = radio.receive()
        if msg:
            display.show(msg)
            if msg == '0':
                robot.move(0, 0)
            elif msg == 'u':
                music.play('c')
            elif msg == 'r':
                music.play('d')
            elif msg == 'l':
                music.play('e')
            elif msg == 'd':
                music.play('f')
            elif msg == '2':
                music.play('g')
            elif msg == '1':
                music.play('a')

    if prog == 3:
        while True:
            display.show(4)
            mouvement = random.randint(0,5)

            if mouvement ==0:
                avancer()
            if mouvement ==1:
                reculer()
            if mouvement ==2:
                gauche()
            if mouvement ==3:
                droite()
            if mouvement ==4:
                ouvre()
            else:
                ferme()
```
## Partie obligatoire
Dans ce mini-projet le robot

- commence le parcours à une position A
- va suivre une ligne
- va detecter un objet avec le capteur ultrason (position B variable)
- va tourner de 180°
- va attraper l'objet avec la pince
- va ramener l'objet à la positon A

## Partie libre
le robot fonctionne sous forme de programme.
Chaque programme avec un code différent pour réaliser différentes choses.
- P0 Télécomander
- P1 Partie obligatoire
- P2 Musique
- P3 Dance


### Programme 0
Le programme 0 est le premier et fait que le robot est télécommender.
```
if prog == 0:
        msg = radio.receive()
        if msg:
            display.show(msg)
            if msg == '0':
                robot.move(0, 0)
            elif msg == 'u':
                robot.move(-80, -80)
            elif msg == 'r':
                robot.move(80, -80)
            elif msg == 'l':
                robot.move(-80, 80)
            elif msg == 'd':
                robot.move(80, 80)
            elif msg == '2':
                robot.goToPosition(1, 20)
            elif msg == '1':
                robot.goToPosition(1, 160)
  ```
Il régit grace au code implémenté dans la télécomande.
```
# télécommande avec kitronik GAME controller
from microbit import *
import radio
import music

# choisissez comme groupe le numéro de votre kit (1-15)
g = 1
display.scroll(g)

radio.config(group=g)
radio.on()

VIB = pin1
BUZZER = pin2
UP = pin8
LEFT = pin12
RIGHT = pin13
DOWN = pin14
FIRE1 = pin15
FIRE2 = pin16

def vibrate(t):
    VIB.write_digital(1)
    sleep(t)
    VIB.write_digital(0)

msg = '0'   # le message à envoyer, juste une lettre

# Code in a 'while True:' loop repeats forever
while True:
    if UP.read_digital() == 0:
        msg = 'u'
    
    elif LEFT.read_digital() == 0:
        msg = 'l'
             
    elif RIGHT.read_digital() == 0:
        msg = 'r'
        
    elif DOWN.read_digital() == 0:
        msg = 'd'

    elif FIRE1.read_digital() == 0:
        if msg == '0':
            music.pitch(440, 20, pin=BUZZER)
        msg = '1'
        
    elif FIRE2.read_digital() == 0:
        if msg == '0':
            vibrate(50)
        msg = '2'
        
    else:
        msg = '0'

    display.show(msg)
    radio.send(msg)
    sleep(100)
```
### Programme 2
Ensuite nous avons le programme 2 car le 1 est celui pour la pratie obligatioire du projet.
Qui lui aussi fonctionne avec la télécomande mais cette fois-ci pour jouer de la musique.

Les notes sont égales à des lettres dans le système Anglo-Saxon qui est utilisé pour le code.

En savoir plus sur: https://jeretiens.net/traduction-du-systeme-de-notation-c-d-e-f-g-a-b-c/
```
 if prog == 2:
        msg = radio.receive()
        if msg:
            display.show(msg)
            if msg == '0':
                robot.move(0, 0)
            elif msg == 'u':
                music.play('c')
            elif msg == 'r':
                music.play('d')
            elif msg == 'l':
                music.play('e')
            elif msg == 'd':
                music.play('f')
            elif msg == '2':
                music.play('g')
            elif msg == '1':
                music.play('a')
```
### Programme 3
Et pour le programme 3 nous avons ajouter une dance du robot mais en alléatoire.
```
  if prog == 3:
        while True:
            display.show(4)
            mouvement = random.randint(0,5)

            if mouvement ==0:
                avancer()
            if mouvement ==1:
                reculer()
            if mouvement ==2:
                gauche()
            if mouvement ==3:
                droite()
            if mouvement ==4:
                ouvre()
            else:
                ferme()
```

- liste avec puces et numéroté
- des formules mathématiques

set_all(color) -essayer
