import os
import time
import signal
import getpass
from datetime import datetime
from PIL import ImageGrab

CAPTURE_INTERVAL = 30
SAVE_FOLDER = "screenshots"
LOG_FILE = "capture_log.txt"
STOP_PASSWORD = "secure123"

running = True

def initialize():
    os.makedirs(SAVE_FOLDER, exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def filepath():
    t = timestamp()
    return t, os.path.join(SAVE_FOLDER, f"screenshot_{t}.png")

def log(message):
    with open(os.path.join(SAVE_FOLDER, LOG_FILE), "a", encoding="utf-8") as f:
        f.write(message + "\n")

def capture():
    t, path = filepath()
    try:
        img = ImageGrab.grab()
        img.save(path, "PNG")
        log(f"{t} | CAPTURED | {path}")
    except Exception as e:
        log(f"{t} | ERROR | {str(e)}")

def handler(sig, frame):
    global running
    pw = getpass.getpass("Password required to stop: ")
    if pw == STOP_PASSWORD:
        running = False

def loop():
    while running:
        capture()
        time.sleep(CAPTURE_INTERVAL)

def main():
    initialize()
    signal.signal(signal.SIGINT, handler)
    log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | MONITOR STARTED")
    loop()
    log(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | MONITOR STOPPED")

if __name__ == "__main__":
    main()
