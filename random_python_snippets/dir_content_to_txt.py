import os

directory = "C:\\Users\\Fatihi\\Desktop\\Rust"

# get the filenames in the directory
filenames = os.listdir(directory)

# write the filenames without the extension to a text file
with open("filenames_without_extension.txt", "w") as file:
    for filename in filenames:
        # only remove the extension if there's a dot before it
        index = filename.rfind(".")
        if index != -1 and index > filename.rfind(os.sep):
            filename = filename[:index]
        file.write(filename + "\n")
