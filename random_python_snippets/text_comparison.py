import tkinter as tk
from tkinter import ttk
import difflib

root = tk.Tk()
root.title("Text Comparison")

# Create Text widget for pasting text 1
text1 = tk.Text(root, height=10, width=40)
text1.grid(row=0, column=0, padx=5, pady=5)

# Create Text widget for pasting text 2
text2 = tk.Text(root, height=10, width=40)
text2.grid(row=0, column=1, padx=5, pady=5)

# Make the columns dynamic
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create a function to compare texts and highlight differences


def compare_texts():
    text1_content = text1.get("1.0", "end-1c")
    text2_content = text2.get("1.0", "end-1c")

    # Use difflib to get the differences between the texts
    diff = difflib.ndiff(text1_content.splitlines(),
                         text2_content.splitlines())

    # Clear the second text widget
    text2.delete("1.0", tk.END)

    # Insert the compared text into the second text widget
    for line in diff:
        if line.startswith("-"):
            text2.insert(tk.END, line, "delete")
        elif line.startswith("+"):
            text2.insert(tk.END, line, "insert")
        else:
            text2.insert(tk.END, line)


# Create a Compare button
compare_button = ttk.Button(root, text="Compare", command=compare_texts)
compare_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Create a style for highlighting the differences
text2.tag_config("delete", background="red")
text2.tag_config("insert", background="green")

root.mainloop()
