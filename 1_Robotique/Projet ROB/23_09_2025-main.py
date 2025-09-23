from microbit import *
from machine import time_pulse_us
import KitronikMOVEMotor
import neopixel
import random

trigger = pin13
echo = pin14

robot = KitronikMOVEMotor.MOVEMotor()
robot.move(0, 0)

trigger.write_digital(0)
echo.read_digital()

v = 4


def distance_cm():
    left = pin1.read_analog()
    right = pin2.read_analog()
    d = (left - right)
    d = d // 10
    robot.move(10 - d, 10 + d)
    trigger.write_digital(1)
    trigger.write_digital(0)
    distance = time_pulse_us(echo, 1)/58.
    return round(distance)




while True:

    d = distance_cm()
    for i in range(25):
        if i < d:
            display.set_pixel(i//5, i%5, 9)
        else:
            display.set_pixel(i//5, i%5, 0)
    
    if d <= 10:
        robot.move(0, 0, 1000)
        robot.move(-60, -60, 500)#faire plus reculer
        robot.move(60, -60, 1250)
        robot.move(-60, -60, 500)
        robot.move(0, 0)
        robot.goToPosition(1, 160)
        sleep(1000)
        robot.goToPosition(1, 20)



