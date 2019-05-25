#Simplified RainbowLED on ESP32 with micropython (C) 25.05.19 DrRetro (MIT-License)
# function "hsvtorgb" Copyright (C) 01.09.2009 Michael Fogleman (MIT-License)


import machine
import time
import math


PinRED = machine.Pin(2)
PinGREEN = machine.Pin(4)
PinBLUE = machine.Pin(5)


pwmRED = machine.PWM(PinRED)
pwmGREEN = machine.PWM(PinGREEN)
pwmBLUE = machine.PWM(PinBLUE)


def hsvtorgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1: 
        r, g, b = q, v, p
    elif hi == 2: 
        r, g, b = p, v, t
    elif hi == 3: 
        r, g, b = p, q, v
    elif hi == 4: 
        r, g, b = t, p, v
    elif hi == 5: 
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def setPWM(Red, Green, Blue):
    pwmRED.duty(Red)
    pwmGREEN.duty(Green)
    pwmBLUE.duty(Blue)


def rgbtopwm(rgbarray):
    return rgbarray[0]*2, rgbarray[1]*2, rgbarray[2]*2


while True:
    for color in range(0,360):
        pwmarray = rgbtopwm(hsvtorgb(color, 1, 1))
        setPWM(pwmarray[0],pwmarray[1],pwmarray[2])
        time.sleep(0.05)
