import time
from picozero import Button
from neopixel import Neopixel


pause = False
start = True

def do_pause():
    global pause
    pause = not pause
    print(f"pause set to {pause}")
    
def do_start():
    global start
    start = not start
    print(f"start set to {start}")

pause_button = Button(18)
pause_button.when_pressed = do_pause
start_button = Button(19)
start_button.when_pressed = do_start

numpix = 432
strip = Neopixel(numpix, 0, 28, "GRB")

brightness = 100




red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

colors = colors_rgb



def startUp():
    strip.brightness(brightness)
    step = round(numpix / len(colors))
    current_pixel = 0
    
    for color1, color2 in zip(colors, colors[1:]):
        strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
        current_pixel += step

    strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, red)

def stopDown():
    strip.fill((0,0,0))
    strip.brightness(0)
    strip.show()

def stall():
    time.sleep(1/15)

def flow_cycle():
    strip.rotate_right(1)
    strip.show()


while __name__ == "__main__":
    if start:
        startUp()
        while start:
            if pause:
                stall()
            else:
                flow_cycle()
        stopDown()
    stall()
    

