# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from omxplayer.player import OMXPlayer
from pathlib import Path
import pygame
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 20

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, bpp=4, brightness=1, auto_write=False, pixel_order=ORDER
)


def turnOff():
    global pixels
    for z in range(20):
        pixels[z] = (0,0,0)
    pixels.show()

def changeRed():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,255,0,0)
        pixels.show()
    time.sleep(0.001)

    
def changeBlue():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,0,255,0)
        pixels.show()
    time.sleep(1)

    
def changeGreen():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (255,0,0,0)
        pixels.show()
    time.sleep(1)

    
def changeYellow():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (255,255,0,0)
        pixels.show()
    time.sleep(1)

    
def changePurple():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (72,162,255,0)
        pixels.show()
    time.sleep(1)

    
def changeOrange():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (127,255,0,0)
        pixels.show()
    time.sleep(1)

    
def changePurple():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,139,255,0)
        pixels.show()
    time.sleep(1)

    
def changePink():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (51,255,153,0)
        pixels.show()
    time.sleep(1)

    
def changeSkyblue():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (255,0,255,0)
        pixels.show()
    time.sleep(1)

    
def changeWhite():
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,0,0,255)
        pixels.show()
    time.sleep(1)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos*3)
        g = int(255 - pos *3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow(num):
    for i in range(num):
        for j in range(255):
            for k in range(num_pixels):
                pixels[k] = wheel((k // num_pixels)+j)
            pixels.show()
            time.sleep(0.01)

def rainbow2(num):
    for i in range(num):
        for j in range(255):
            for k in range(num_pixels):
                pixel_index = (k * 255 // num_pixels) + j
                pixels[k] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(0.01)


def glow(num):
    for i in range(num):
        for j in range(2000) :
            if j < 1000:
                pixels.brightness = 0.001*j
                pixels.show()
            elif j <2000:
                pixels.brightness = 0.001*abs(j-2000)
                pixels.show()
            
def glow2(num):
    for i in range(num):
        for j in range(1000) :
            if j < 500:
                pixels.brightness = 0.002*j
                pixels.show()
            elif j <1000:
                pixels.brightness = 0.002*abs(j-1000)
                pixels.show()

def fastglow(num):
    for i in range(num):
        for j in range(500) :
            if j < 250:
                pixels.brightness = 0.04*j
                pixels.show()
            elif j <500:
                pixels.brightness = 0.04*abs(j-500)
                pixels.show()
                
def impact(num):
    for i in range(num):
        for j in range(250):
            if j < 240:
                pixels.brightness = 0.1
                pixels.show()
            else:
                pixels.brightness = 1
                pixels.show()
            
def impact2(num):
    for i in range(num):
        for j in range(250):
            if j < 240:
                pixels.brightness = 0.3
                pixels.show()
            else:
                pixels.brightness = 1
                pixels.show()
            
def impact3(num):
    for i in range(num):
        for j in range(250):
            if j < 240:
                pixels.brightness = 0.5
                pixels.show()
            else:
                pixels.brightness = 1
                pixels.show()

def sound1():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound1.mp3')
    pygame.mixer.music.play()

def sound2():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound2.mp3')
    pygame.mixer.music.play()
    
def sound3():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound3.mp3')
    pygame.mixer.music.play()
    
def sound4():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound4.mp3')
    pygame.mixer.music.play()
    
def sound5():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound5.mp3')
    pygame.mixer.music.play()
    
def sound6():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound6.mp3')
    pygame.mixer.music.play()
    
def sound7():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound7.mp3')
    pygame.mixer.music.play()
    
def sound8():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound8.mp3')
    pygame.mixer.music.play()
    
def sound9():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound9.mp3')
    pygame.mixer.music.play()
    
def sound10():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound10.mp3')
    pygame.mixer.music.play()
    
def sound11():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound11.mp3')
    pygame.mixer.music.play()
    
def sound12():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound12.mp3')
    pygame.mixer.music.play()
    
def sound13():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound13.mp3')
    pygame.mixer.music.play()
    
def sound14():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/magicmarble/sound/sound14.mp3')
    pygame.mixer.music.play()