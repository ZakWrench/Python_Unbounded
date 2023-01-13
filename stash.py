
from datetime import timedelta
import time
import subprocess
import youtube_dl
import re
from pytube import YouTube
import tkinter as tk
import tkinter.messagebox
import urllib.parse
import sys


def mp3(link):
    try:
        yt = YouTube(link)
        video_title = yt.title

        # Check if the title has any characters that aren't allowed in filenames
        # and replace them with an underscore
        filename = re.sub(r'[^\w\-_\. ]', '_', video_title)

        # Download and convert the video
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
            ydl.download([link])
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


def start_download():
    link = link_entry.get()
    parsed_link = urllib.parse.urlparse(link)
    if parsed_link.scheme == "":
        link = "https://www.youtube.com/watch?v=" + parsed_link.path.strip("/")
    elif not parsed_link.netloc == "youtube.com" or not parsed_link.path.startswith("/watch"):
        tkinter.messagebox.showerror("Error", "Invalid YouTube link")
        return
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

root.mainloop()
