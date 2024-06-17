from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

while(True):
    keyboard.press(Key.page_down)
    keyboard.release(Key.page_down)
    time.sleep(0.7)