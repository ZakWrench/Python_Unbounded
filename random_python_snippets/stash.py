
from datetime import timedelta
import time
import subprocess
import youtube_dl
import re
from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import urllib.parse
import sys
import os

stop_download = False


def mp3(link):
    global stop_download
    try:
        yt = YouTube(link)
        video_title = yt.title

        filename = re.sub(r'[^\w\-_\. ]', '_', video_title)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': filename + '.%(ext)s',
            'threads': 4,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            while not stop_download:
                ydl.download([link])
                time.sleep(0.5)
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


def stop_download_func():
    global stop_download
    stop_download = True


def mp4(link):
    try:
        yt = YouTube(link)
        video_title = yt.title

        filename = re.sub(r'[^\w\-_\. ]', '_', video_title)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': filename + '.%(ext)s',
            'threads': 4
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


def start_download():
    global stop_download
    stop_download = False

    link = link_entry.get()
    parsed_link = urllib.parse.urlparse(link)
    if parsed_link.scheme == "":
        link = "https://www.youtube.com/watch?v=" + parsed_link.path.strip("/")
        mp3(link)
        return
    elif not (parsed_link.netloc == "youtube.com" or parsed_link.netloc == "www.youtube.com") or not (parsed_link.path.startswith("/watch") or parsed_link.path.startswith("/watch?v=")):
        tkinter.messagebox.showerror("Error", "Invalid YouTube link")
        return
    params = urllib.parse.parse_qs(parsed_link.query)
    if 'v' not in params:
        tkinter.messagebox.showerror("Error", "Invalid YouTube link")
        return
    video_id = params['v'][0]
    link = f"https://www.youtube.com/watch?v={video_id}"
    mp3(link)

#


is_hidden = True


def toggle_hidden_files():
    subprocess.run(
        'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Hidden" /t REG_DWORD /d 1 /f', shell=True)
    tkinter.messagebox.showinfo(
        "Info", "Hidden files and folders are now visible")


def toggle_hidden_files_off():
    subprocess.run(
        'reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "Hidden" /t REG_DWORD /d 2 /f', shell=True)
    tkinter.messagebox.showinfo(
        "Info", "Hidden files and folders are now invisible")


"""
def toggle_hidden_files():
    global is_hidden
    if is_hidden:

        hidden_files_button.config(
            text="Hide Files", command=toggle_hidden_files_off)
    else:
        hidden_files_button.config(
            text="Show Hidden Files", command=toggle_hidden_files)
    is_hidden = not is_hidden

"""
##


start_time = time.time()


def update_counter():
    elapsed_time = time.time() - start_time
    elapsed_time = timedelta(seconds=elapsed_time)
    counter_label.configure(text=str(elapsed_time))
    root.after(1000, update_counter)


def on_closing():
    elapsed_time = time.time() - start_time
    elapsed_time = timedelta(seconds=elapsed_time)
    tkinter.messagebox.showinfo("Info", f"Total time spent: {elapsed_time}")
    root.destroy()


###


def launch_ds3():
    subprocess.run(r'H://Dark Souls 3//Game//DarkSoulsIII.exe', shell=True)
    # subprocess.Popen(r'H://Dark Souls 3//Game//DarkSoulsIII.exe',
    #                 )


####

# Total number of lines written.
def count_lines(file_path):
    lines = 0
    multiline_comment = False
    with open(file_path, "r") as f:
        for line in f:
            if multiline_comment:
                if line.strip().endswith("\"\"\"") or line.strip().endswith("\'\'\'"):
                    multiline_comment = False
            elif line.strip().startswith("\"\"\"") or line.strip().startswith("\'\'\'"):
                multiline_comment = True
            elif not line.startswith("#") and not multiline_comment and line.strip() != "":
                lines += 1
    return lines


def total_lines():
    directory = "C:\\Users\\Fatihi\\Desktop\\python\\Quick_Python"
    lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                lines += count_lines(file_path)
    return lines


def update_lines():
    lines_var.set("Total lines: {}".format(total_lines()))
    root.after(1000, update_lines)


total_l = total_lines()

"""
def on_button_click():
    total = total_lines()
    current_total_lines.config(text="Total lines: {}".format(total))
"""

########
root = tk.Tk()
root.title("Zak's Stash")

counter_label = tk.Label(root, text="0:00:00")
counter_label.grid(row=0, column=1)
root.after(1000, update_counter)
root.protocol("WM_DELETE_WINDOW", on_closing)

link_label = tk.Label(root, text="YouTube Link:")
link_label.grid(row=1, column=0)

link_entry = tk.Entry(root)
link_entry.grid(row=1, column=1)

download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=1, column=2, pady=10)
stop_download_button = tk.Button(
    root, text="Stop Download", command=stop_download_func)
stop_download_button.grid(row=1, column=3)

hidden_files_button = tk.Button(
    root, text="Show Hidden Files", command=toggle_hidden_files)
hidden_files_button.grid(row=2, column=1)
hidden_files_button = tk.Label(root, text="---> ")
hidden_files_button.grid(row=2, column=0)

hidden_files_off_button = tk.Button(
    root, text="Hide Files", command=toggle_hidden_files_off)
hidden_files_off_button.grid(row=2, column=2)

'''
hidden_files_button = tk.Button(
    root, text="Hide Files", command=toggle_hidden_files)
hidden_files_button.grid(row=2, column=0)
'''

game_button = tk.Button(root, text="Dark Souls 3", command=launch_ds3)
game_button.grid(row=3, column=1, pady=10)
ds3_label = tk.Label(root, text="---> ")
ds3_label.grid(row=3, column=0)

"""
button = ttk.Button(root, text="Count Lines", command=on_button_click)
button.grid(row=4, column=1)
"""
root.after(1000, update_lines)
lines_var = tk.StringVar()
label = ttk.Label(root, textvariable=lines_var)
label.grid(row=5, column=0)
lines_var.set("Total lines: {}".format(total_lines()))
root.mainloop()
