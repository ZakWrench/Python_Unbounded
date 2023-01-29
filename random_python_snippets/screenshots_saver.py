import time
import datetime
from PIL import ImageGrab
import random
import ctypes
import win32api
import win32con

width1, height1 = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
width2, height2 = win32api.GetSystemMetrics(78), win32api.GetSystemMetrics(79)
#cursor_width = win32api.GetSystemMetrics(13)
#keydown = win32api.GetSystemMetrics(win32con.WM_KEYDOWN)
print(
    f'width1: {width1}, height1: {height1}, width2: {width2}, height2: {height2}')
max_screenshots = 10
counter = 0
screenshot_folder = 'C:\\Users\\Fatihi\\Desktop\\test\\'

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
    #img_2.save(screenshot_2_path)
    counter += 1
    max_screenshots -= 1
    print(f'Screenshot saved to {screenshot_path}')
    # Display a message box
    ctypes.windll.user32.MessageBoxW(
        0, f'Screenshot saved to {screenshot_path}', "Screenshot Taken", 0x40)


def screenshotter():
    previous_day = datetime.datetime.now().day
    while max_screenshots > 0:
        time.sleep(random.randint(675, 888))
        current_day = datetime.datetime.now().day
        if current_day != previous_day:
            max_screenshots = 10
            previous_day = current_day
        take_screenshot()
        time.sleep(2888)


screenshotter()
