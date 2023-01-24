
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
from tkinter import filedialog
from docx import Document
import threading
from PIL import Image

stop_download = False
download_thread = None


def mp3(link):
    global stop_download, download_thread
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
            download_thread = threading.Thread(
                target=ydl.download, args=([link],))
            download_thread.start()
            download_thread.join()
    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


def stop_download_func():
    global stop_download
    stop_download = True
    download_thread.join()


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
#####


def browse():
    text_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    docx_file = text_file.replace('.txt', '.docx')

    txt_docx_browse_button.config(state='disable')
    txt_docx_progressbar.start()

    thread = threading.Thread(target=convert, args=(text_file, docx_file))
    thread.start()


def convert(text_file, docx_file):
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    doc = Document()
    doc.add_paragraph(text)
    doc.save(docx_file)

    txt_docx_progressbar.stop()
    txt_docx_progressbar.pack_forget()
    txt_docx_browse_button.config(state='normal')

######


def scale_image(im, percent):
    # Get the original size of the image
    width, height = im.size

    # Calculate the new size of the image
    new_width = int(width * percent)
    new_height = int(height * percent)

    # Resize the image
    im = im.resize((new_width, new_height), Image.ANTIALIAS)

    return im


def browse_file():
    filepath = filedialog.askopenfilename()
    im = Image.open(filepath)
    return im, filepath


def save_image(im, filepath):
    filename = filepath.split("/")[-1]
    im.save(f"{filename.split('.')[0]}_scaled.{filename.split('.')[1]}")


def scale_percentage():
    global filepath
    filepath = filedialog.askopenfilename()
    im = Image.open(filepath)
    scale = float(scale_entry.get())
    im = scale_image(im, scale/100)
    save_image(im, filepath)
########


def create_todo_list():
    todo_list_window = tk.Toplevel(root)
    todo_list_window.title("To Do List")

    tasks = []
    task_entry = []  # Make task_entry a list

    def add_entry():
        new_entry = ttk.Entry(todo_list_window)
        new_entry.grid(row=len(task_entry), column=0,
                       padx=5, pady=5, sticky="W")
        task_entry.append(new_entry)  # Append new entry to task_entry list

    add_entry_button = ttk.Button(
        todo_list_window, text="Add Entry", command=add_entry)
    add_entry_button.grid(row=0, column=2, padx=5, pady=5)
    add_entry()  # Initialize the first entry

    def add_task():
        # Get text from the last entry in the task_entry list
        task = task_entry[-1].get()
        tasks.append(task)
        task_var = tk.StringVar()
        task_var.set(task)
        task_label = ttk.Label(todo_list_window, textvariable=task_var)
        task_label.grid(row=len(tasks), column=0, padx=5, pady=5, sticky="W")

        task_done = tk.IntVar()
        task_check = ttk.Checkbutton(
            todo_list_window, variable=task_done, onvalue=1, offvalue=0)
        task_check.grid(row=len(tasks), column=1, padx=5, pady=5)
        task_check.set(0)

        delete_task_button = ttk.Button(
            todo_list_window, text="Delete Task", command=delete_task)
        delete_task_button.grid(row=len(tasks), column=2, padx=5, pady=5)

        def delete_task():
            tasks.remove(task)
            task_label.destroy()
            task_check.destroy()
            delete_task_button.destroy()


#########
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


txt_docx = tk.Label(root, text="Convert text to docx")
txt_docx.grid(row=6, column=0)

txt_docx_browse_button = tk.Button(root, text="Browse", command=browse)
txt_docx_browse_button.grid(row=6, column=1)
txt_docx_progressbar = ttk.Progressbar(
    root, orient="horizontal", length=100, mode="determinate")
txt_docx_progressbar.grid(row=6, column=2)


scale_label = tk.Label(root, text="Scale Image Down (0-100 percent):")
scale_label.grid(row=7, column=0)

scale_entry = tk.Entry(root)
scale_entry.insert(0, 50)
scale_entry.grid(row=7, column=1)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=7, column=2)
browse_button.grid_forget()

scale_button = tk.Button(root, text="Scale Down", command=scale_percentage)
scale_button.grid(row=7, column=2)

todo_button = tk.Button(root, text="To Do List", command=create_todo_list)
todo_button.grid(row=8, column=0)


root.mainloop()
