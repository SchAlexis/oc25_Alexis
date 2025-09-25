from microbit import *
from machine import time_pulse_us
import KitronikMOVEMotor
import music
import radio

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

    if prog == 3:
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