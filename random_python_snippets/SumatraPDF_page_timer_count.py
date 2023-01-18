import time
import threading
import winsound
import subprocess


def run_sumatra():
    # Run Sumatra PDF in the background
    sumatra_process = subprocess.Popen(
        ["SumatraPDF.exe"], stdout=subprocess.PIPE)
    # Wait for Sumatra PDF to close
    sumatra_process.wait()


def track_pages():
    # This is the location of the Sumatra PDF log file
    log_file_path = "C:/Program Files/SumatraPDF/sumatrapdf.log"

    # Initialize the page count to 0
    page_count = 0

    # Initialize a dictionary to store the time spent on each page
    page_times = {}

    # Open the log file in read mode
    with open(log_file_path, "r") as log_file:
        # Iterate over the lines in the log file
        for line in log_file:
            # Check if the line indicates that a page was turned
            if "TurnToPage" in line:
                # Split the line by spaces and get the second item (the page number)
                page_num = int(line.split(" ")[1])
                # Get the current time
                current_time = time.time()
                # If the page number is not in the page_times dictionary, add it and set the start time to the current time
                if page_num not in page_times:
                    page_times[page_num] = {"start": current_time, "end": None}
                # Otherwise, set the end time for the previous page to the current time
                else:
                    page_times[page_num-1]["end"] = current_time
                # Add the page number to the page count
                page_count += 1
                # Play the ding sound effect
                winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)

    # Set the end time for the last page to the current time
    page_times[page_num]["end"] = current_time

    # Print the total number of pages read
    print(f"Total pages read: {page_count}")

    # Iterate over the page times and calculate the time spent on each page
    for page_num, page_time in page_times.items():
        start_time = page_time["start"]
        end_time = page_time["end"]
        time_spent = end_time - start_time
        print(f"Page {page_num}: {time_spent:.2f} seconds")


# Start the Sumatra PDF process in a separate thread
sumatra_thread = threading.Thread(target=run_sumatra)
sumatra_thread.start()

# Run the page tracking program in the main thread
track_pages()
