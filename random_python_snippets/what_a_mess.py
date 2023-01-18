#import tkinter as tk
import random
import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
#import csv
import datetime
import time
import winsound
import cv2
from sklearn import svm


def extract_features(image):
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # resize image
    resized_image = cv2.resize(gray, (200, 200))
    # Detect and extract facial features using Haar cascades
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
        resized_image, scaleFactor=1.3, minNeighbors=5)
    # Extract the facial features and resize them to a fixed size
    for (x, y, w, h) in faces:
        face_features = resized_image[y:y+h, x:x+w]
        face_features = cv2.resize(face_features, (50, 50))
    return face_features


# gather datasets of facial images for eligible and non-eligible users
eligible_images = []
non_eligible_images = []

# extract features from images
eligible_features = []
for image in eligible_images:
    features = extract_features(image)
    eligible_features.append(features)

non_eligible_features = []
for image in non_eligible_images:
    features = extract_features(image)
    non_eligible_features.append(features)

# create labels for the two classes
labels = [1] * len(eligible_features) + [0] * len(non_eligible_features)

# combine the features and labels into a single dataset
data = eligible_features + non_eligible_features

# create an SVM classifier and fit it to the data
classifier = svm.SVC()
classifier.fit(data, labels)


def get_current_date():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    return date_str


current_date = get_current_date()
message = "Welcome, today's date is: " + current_date


def animate_text(text):
    for letter in message:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colored_letter = f"\033[38;2;{red};{green};{blue}m{letter}\033[0m"
        print(colored_letter, end="")
        time.sleep(0.1)


animate_text(current_date)

print()


def print_secret_message(result):
    if result == 42:
        print("42 is the lost number")


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def cosine(x):
    return math.cos(x)


def sine(x):
    return math.sin(x)


def log_natural(x):
    return math.log(x, math.e)


def fft(x):
    # convert the input sequence to an array
    x = np.array(x)
    # calculate the FFT of the input sequence
    y = np.fft.fft(x)
    # return the real and imaginary parts of the FFT as a tuple
    return y.real, y.imag


def area_of_circle(radius):
    # use formula for the area of a circle (pi * r^2)
    area = math.pi * radius**2
    return area


def log_likelyhood(data, params):
    # calculate the logodd value
    log_likelihood = 0
    for x, p in zip(data, params):
        log_likelihood += math.log(scipy.stats.norm.pdf(x, p))
    print(type(log_likelyhood))
    print(repr(log_likelyhood))
    return log_likelihood


def calculate_result(x, y, radius):
    sum_xy = operations["+"](x, y)
    # calculate the logn of the sum
    log_sum = operations["logn"](sum_xy)
    # calculate area
    area = operations["area"](radius)
    # multiply logn with area
    result = log_sum * area
    print_secret_message(result)
    return result


# create a dictionary to map operations to functions
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "sin": sine,
    "cos": cosine,
    "fft": fft,
    "area": area_of_circle,
    "logn": log_natural,
    "area-2.0": calculate_result,
    "logodd": log_likelyhood,
}


def calculator():
    winsound.Beep(400, 1000)
    winsound.PlaySound("untitled.wav", winsound.SND_FILENAME)

    operation = input(
        "\nEnter an operation(+ - * / sin cos fft area logn area-2.0 logodd): ")
    type(operation)
    func = operations.get(operation)
    if func is None:
        print("invalid operation")
        return

    if operation in ["sin", "cos", "fft"]:
        x = []
        while True:
            value = input("Enter a number (enter 'done' when finished): ")
            if value == "done":
                break
            x.append(float(value))
        if operation in ["sin", "cos"]:
            # apply the function to each value in the input sequence
            result = [func(val) for val in x]
            print(result)
        else:
            # calculate FFT and print real and imaginary parts
            result = func(x)
            print(result[0])
            print(result[1])

    elif operation == "area":
        # prompt the user for the radisu of the circle
        radius = float(input("Enter the radius of the circle: "))
        # calc the area of circle
        result = func(radius)
        print(result)
    elif operation == "logn":
        x = float(input("Enter the value to calculate the natural logarithm of: "))
        # apply the log_natural function
        result = func(x)
        print(result)
    elif operation == "area-2.0":
        x = float(input("Enter the first value: "))
        y = float(input("Enter the second value: "))
        radius = float(input("Enter the radius of the circle: "))
        result = calculate_result(x, y, radius)
        print(result)
    elif operation == "logodd":
        # prompt the user for the data and model parameters
        data = []
        while True:
            value = input("Enter a data point (enter 'done' when finished): ")
            if value == "done":
                break
            data.append(float(int(value)))
        params = []
        while True:
            value = input(
                "Enter a model parameter (enter 'done' when finished): ")
            if value == "done":
                break
            params.append(float(value))
        # caluclate logodd
        result = log_likelyhood(data, params)
        print("Log likelihood: ", result)
        plt.plot(result)
        plt.show()
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = func(num1, num2)
        print(result)


calculator()


'''
# read data
with open("names.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

# create count dict
name_counts = {}

# loop through the rows and add up the counts of each name
for row in rows:
    name = row[0]
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

# find the most common name
most_common_name = None
highest_count = 0
for name, count in name_counts.items():
    if count > highest_count:
        most_common_name = name_counts
        highest_count = count

print("The most common name is: ", most_common_name)
'''
