# Hello World!
# hello world!

print('hello world')
#####
# Big Integer
# bignum

print(1 << 1000)
#####
# Assembly
# inline assembler

@micropython.asm_thumb
def asm_add(r0, r1):
    add(r0, r0, r1)
print(asm_add(1, 2))
#####
# Switch
# push the USR button on the pyboard to flash the LEDs!
# try using the reset button on the pyboard to quit this script!
# switch callback not yet supported.

import time
import pyb

while True:
    if pyb.Switch().value():
        pyb.LED(1).on()
    else:
        pyb.LED(1).off()
    time.sleep_ms(50)

#####
# LEDs
# four LEDS numbered 1 to 4

import time
import pyb

for i in range(1000):
    pyb.LED((i%4) + 1).toggle()
    time.sleep_ms(100)
#####
# Time
# the time module is utime, a specialized MicroPython library
# sleep will break the clock speed
# dates not yet supported

import time

print(time.ticks_ms())

time.sleep_ms(1000)

print(time.ticks_us())

time.sleep_us(1000000)
#####
# Math
# a subset of the Python Math library

import math
import cmath

print(math.sqrt(5))
print(math.log10(100))
print(math.sin(12345) ** 2 + math.cos(12345) ** 2)
print(math.cosh(1) ** 2 - math.sinh(1) ** 2)
print(cmath.polar(1 + 1j))
#####
# Pin LED
# Using a Pin with micropython
# Make sure you have the LED checkbox marked!

import machine

# The LED is connected to our virtual pin Y12
y12 = machine.Pin('Y12')

y12(0 if y12() else 1)
#####
# ADC
# Using the ADC (Analogue to Digital Converter)
# Make sure you have the ADC checkbox marked!

import machine
import pyb

# The slider is connected to pin Y4, try adjusting it
y4 = machine.Pin('Y4')

adc = pyb.ADC(y4)

print(adc.read())
#####
# Using the Servo
# Make sure you have the Servo checkbox marked!

import machine
import pyb

# The pyboard has four simple servo connections
servo = pyb.Servo(1)

servo.angle(90, 5000)
#####
# Mandelbrot Set
# A python Mandelbrot set courtesy of 
# http://warp.povusers.org/MandScripts/python.html
# Try your own Python3 scripts on MicroPython!

minX = -2.0
maxX = 1.0
width = 60
height = 28
aspectRatio = 2

chars = ' .,-:;i+hHM$*#@ '

yScale = (maxX-minX)*(float(height)/width)*aspectRatio

for y in range(height):
    line = ''
    for x in range(width):
        c = complex(minX+x*(maxX-minX)/width, y*yScale/height-yScale/2)
        z = c
        for char in chars:
            if abs(z) > 2:
                break
            z = z*z+c
        line += char
    print(line)
