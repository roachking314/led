# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 20

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, bpp=4, brightness=1, auto_write=False, pixel_order=ORDER
)

def changeRed(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,255,0,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changeBlue(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,0,255,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changeGreen(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (255,0,0,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changeYellow(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (255,255,0,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changePurple(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (72,162,255,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changeOrange(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (127,255,0,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changePurple(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,139,255,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changePink(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (51,255,153,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changeSkyblue(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (255,0,255,0)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()
    
def changeWhite(delay):
    global pixels
    for z in range(num_pixels):
        pixels[z] = (0,0,0,255)
        pixels.show()
    time.sleep(int(delay))
    #turnOff()

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
    return (g, r, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (g, r, b, 0)


def wheel2(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 765:
        r = g = b = 0
    elif pos < 255:
        r = int(pos)
        g = int(255 - pos)
        b = 0
    elif pos < 510:
        pos = pos - 255
        r = int(255 - pos)
        g = 0
        b = int(pos)
    else:
        pos = pos - 510
        r = 0
        g = int(pos)
        b = int(255 - pos)
    return (g, r, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (g, r, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 255 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def rainbow_cycle2(wait):
    for j in range(765):
        for i in range(num_pixels):
            pixel_index = (i // num_pixels) + j
            pixels[i] = wheel2(pixel_index)
        pixels.show()
        time.sleep(wait)
        
def rainbow(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixels[i] = wheel((i // num_pixels)+j)
        pixels.show()
        time.sleep(wait)

def glow(num):
    for j in range(num):
        if j < num:
            for i in range(2000) :
                if i < 1000:
                    pixels.brightness = 0.001*i
                    pixels.show()
                elif i <2000:
                    i = i - 2000
                    pixels.brightness = 0.001*abs(i)
                    pixels.show()
        elif j == num :
            time.sleep(1)
            
def glow2(num):
    for j in range(num):
        if j < num:
            for i in range(1000) :
                if i < 500:
                    pixels.brightness = 0.002*i
                    pixels.show()
                elif i <1000:
                    i = i - 1000
                    pixels.brightness = 0.002*abs(i)
                    pixels.show()
        elif j == num :
            time.sleep(1)

def fastglow(num):
    for j in range(num):
        if j < num:
            for i in range(500):
                if i < 250:
                    pixels.brightness = 0.04*i
                    pixels.show()
                elif i < 500:
                    i = i - 500
                    pixels.brightness = 0.04*abs(i)
                    pixels.show()
        elif j == num :
            time.sleep(1)
            
def impact(num):
    for j in range(num):
        if j < num:
            for i in range(250):
                if i < 240:
                    pixels.brightness = 0.1
                    pixels.show()
                elif i < 250:
                    pixels.brightness = 1
                    pixels.show()
        elif j == num:
            time.sleep(1)
            
def impact2(num):
    for j in range(num):
        if j < num:
            for i in range(250):
                if i < 240:
                    pixels.brightness = 0.3
                    pixels.show()
                elif i < 250:
                    pixels.brightness = 1
                    pixels.show()
        elif j == num:
            time.sleep(1)
            
def impact3(num):
    for j in range(num):
        if j < num:
            for i in range(250):
                if i < 240:
                    pixels.brightness = 0.5
                    pixels.show()
                elif i < 250:
                    pixels.brightness = 1
                    pixels.show()
        elif j == num:
            sleep(1)

while True:
    changeSkyRed(0)