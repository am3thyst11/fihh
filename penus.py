import pyautogui as p
from pynput import mouse

print("click somewhere and it will paste the mouse coords")
def on_click(x, y, button, pressed):
    if pressed:
        coord_text = f"{x}, {y}"
        print(f"you clicked at: {coord_text}")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()