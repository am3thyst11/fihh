import time
import os
import evdev
import subprocess
import pyautogui as p
from pynput import mouse
from PIL import Image, ImageChops
from evdev import UInput, ecodes as e, AbsInfo as a

def xd(*args):
    subprocess.run(["xdotool", *args])

ax, ay = "2760", "789" #where you want your mouse to be when you cast your fihhing rod (im not entirely sure if this matters because im faking controller input. pretend like it does)
bx1, by1 = 2529, 653 #top left corner of area you want to detect fihh
bx2, by2 = 2555, 662 #bottom right corner of area you want to detect fihh
bx3 = bx2 - bx1
by3 = by2 - by1

capabilities = {
    e.EV_KEY: [
        e.BTN_SOUTH,  
        e.BTN_EAST,
        e.BTN_NORTH,
        e.BTN_WEST,
        e.BTN_START,
        e.BTN_SELECT,
       ],
    e.EV_ABS: {
        e.ABS_X:  a(0, -32768, 32767, 0, 0, 0),
        e.ABS_Y:  a(0, -32768, 32767, 0, 0, 0),
        e.ABS_RX: a(0, -32768, 32767, 0, 0, 0),
           e.ABS_RY: a(0, -32768, 32767, 0, 0, 0),
    }
}

ui = UInput(
    capabilities,
    name="Xbox 360 Controller",
    vendor=0x045e,
    product=0x028e,
    version=0x0110,
    bustype=e.BUS_USB,
)

print("it might have made the controller fuck if i know check steam")

time.sleep(12)

xd("mousemove", ax, ay)
ui.write(e.EV_KEY, e.BTN_SOUTH, 1)
ui.syn()
time.sleep(0.12)
ui.write(e.EV_KEY, e.BTN_SOUTH, 0)
ui.syn()

ui.write(e.EV_KEY, e.BTN_SOUTH, 1)
ui.syn()
time.sleep(0.12)
ui.write(e.EV_KEY, e.BTN_SOUTH, 0)
ui.syn()

time.sleep(2)

def images_equal(path1, path2):
    try:
        with Image.open(path1) as img1, Image.open(path2) as img2:
            if img1.size != img2.size or img1.mode != img2.mode:
                return False
            return list(img1.get_flattened_data()) == list(img2.get_flattened_data())
    except EOFError:
        return False 
    
region = (bx1, by1, bx3, by3)
f1 = '/home/cheese/Documents/fihh/ss1.png'
f2 = '/home/cheese/Documents/fihh/ss2.png'

while True:
    p.screenshot(region=region).save(f1)
    p.screenshot(region=region).save(f2)
    if images_equal(f1, f2):
        print("no fihh :(")
    else:
        print("fihh detected!")
        ui.write(e.EV_KEY, e.BTN_SOUTH, 1)
        ui.syn()
        time.sleep(0.12)
        ui.write(e.EV_KEY, e.BTN_SOUTH, 0)
        ui.syn()

        ui.write(e.EV_KEY, e.BTN_SOUTH, 1)
        ui.syn()
        time.sleep(0.12)
        ui.write(e.EV_KEY, e.BTN_SOUTH, 0)
        ui.syn()
    for f in [f1, f2]:
        if os.path.exists(f):
            os.remove(f)
    time.sleep(4)
