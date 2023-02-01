import time
import datetime
from PIL import ImageGrab
import random
import ctypes
import win32api
import win32con

# The code is a script that takes screenshots of the desktop and saves them to a specified folder.
# The screenshots are taken in two parts: the entire desktop and a portion of it. It uses the PIL library
# to capture the screenshots, and the `ctypes` library to display a message box after each screenshot is taken.
# The `datetime` and `time` libraries are used to keep track of the date and time for naming the screenshots.
# The `win32api` and `win32con` libraries are used to get the dimensions of the desktop and portion of the screen.
#  The `random` library is used to provide random sleep times between taking each screenshot.
# The script has two functions: `take_screenshot` and `screenshotter`.
# The `take_screenshot` function takes the screenshots and saves them to the specified folder.
# The `screenshotter` function calls the `take_screenshot` function repeatedly until the maximum number of screenshots is reached.
# The script sets the maximum number of screenshots to 10 and runs the `screenshotter` function.

width1, height1 = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
#width2, height2 = win32api.GetSystemMetrics(80), win32api.GetSystemMetrics(81)
#cursor_width = win32api.GetSystemMetrics(13)
#keydown = win32api.GetSystemMetrics(win32con.WM_KEYDOWN)
print(
    f'width1: {width1}, height1: {height1}, width2: {width2}, height2: {height2}')
counter = 0
screenshot_folder = 'C:\\Users\\Fatihi\\Pictures\\Loop\\Desktop_changes\\Screenshot\\'

current_date = time.strftime("%Y%m%d")
current_time = time.strftime("%H:%M:%S")
current_time = current_time.replace(':', '-')


def take_screenshot():
    global max_screenshots, counter
    # Take the screenshot
    img = ImageGrab.grab()
    img_2 = ImageGrab.grab(bbox=(width1, 0, width1 + width2, height2))

    # Save the screenshot to the specified folder
    screenshot_path = screenshot_folder + current_date + '-' + current_time + \
        '-screenshot_0' + str(counter) + '_a' + '.png'
    screenshot_2_path = screenshot_folder + current_date + '-' + current_time + \
        '-screenshot_0' + str(counter) + '_b' + '.png'
    img.save(screenshot_path)
    # img_2.save(screenshot_2_path)
    counter += 1
    max_screenshots -= 1
    print(f'Screenshot saved to {screenshot_path}')
    # Display a message box
    ctypes.windll.user32.MessageBoxW(
        0, f'Screenshot saved to {screenshot_path}', "Screenshot Taken", 0x40)


def screenshotter():
    global max_screenshots
    previous_day = datetime.datetime.now().day
    while max_screenshots > 0:
        time.sleep(random.randint(150, 350))
        current_day = datetime.datetime.now().day
        if current_day != previous_day:
            max_screenshots = 10
            previous_day = current_day
        take_screenshot()
        time.sleep(500)


max_screenshots = 10

screenshotter()
