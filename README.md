# Python Automated Screenshot Capture

A simple Python tool that automatically captures screenshots at fixed time intervals and stores them for documentation or compliance records.

## Features

- Automatic full-screen screenshot capture
- Timestamp-based filenames
- Continuous monitoring loop
- PNG image storage
- Silent background operation
- Log file for capture events
- Password required to stop program (Ctrl+C)

## Requirements

Python 3.8 or newer

Python packages:
- Pillow

## Installation

1. Install Python if it is not already installed.

2. Install dependencies.

pip install -r requirements.txt

## Files

screenshot_monitor.py
requirements.txt
README.md

## Running the Program

Run the script from the terminal:

python screenshot_monitor.py

The program will:

- Create a folder named `screenshots`
- Capture the full screen
- Save screenshots with timestamps
- Repeat every configured interval

Example filenames:

screenshot_2026-03-09_21-14-10.png  
screenshot_2026-03-09_21-14-40.png  

## Folder Structure

screenshots/
    screenshot_YYYY-MM-DD_HH-MM-SS.png
    capture_log.txt

## Stopping the Program

Press:

CTRL + C

The program will ask for a password.

Enter the configured password to stop the program.

If the password is incorrect, the program will continue running.

## Configuration

Inside the script you can modify:

CAPTURE_INTERVAL

Example:

CAPTURE_INTERVAL = 30

This means screenshots will be captured every 30 seconds.

Other examples:

5   = every 5 seconds  
60  = every 1 minute  
300 = every 5 minutes

You can also change the stop password in the script.

STOP_PASSWORD = "yourpassword"

## Log File

Every screenshot event is recorded in:

capture_log.txt

Example:

2026-03-09_21-14-10 | CAPTURED | screenshots/screenshot_2026-03-09_21-14-10.png
2026-03-09_21-14-40 | CAPTURED | screenshots/screenshot_2026-03-09_21-14-40.png

If an error occurs it will also be recorded.

## Use Case

This program can be used for:

- automated documentation
- visual audit trails
- system monitoring
- compliance logging
- automated visual record keeping
