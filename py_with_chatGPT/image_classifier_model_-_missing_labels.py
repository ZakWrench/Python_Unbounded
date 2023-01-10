import cv2
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# CODE MISSING LABELING.

image = cv2.imread("image2.jpg")
# Correct for lens distortion
k = np.array([[1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 0.0, 1.0]])
dist = np.array([0.0, 0.0, 0.0, 0.0])
image = cv2.undistort(image, k, dist)

# Enhance the contrast and sharpness
image = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
image = cv2.GaussianBlur(image, (5, 5), 0)
print(type(image), image)
# Save the preprocessed image
cv2.imwrite("image_preprocessed.jpg", image)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges using the Canny edge detector
edges = cv2.Canny(gray, 50, 100)

# Extract lines using the Hough transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50,
                        minLineLength=50, maxLineGap=10)

# Create a blank image to draw the lines on
blank_image = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)

# Draw the lines on the blank image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(blank_image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Extract points using the Harris corner detector
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Display the image with the extracted features
cv2.imshow("Edges", edges)
cv2.imshow("Corners", corners)
cv2.imshow("Lines", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#######
objects = []
for i in range(10):
    lines_count = len(lines[i])
    edges_count = np.count_nonzero(edges[i])
    corners_count = np.count_nonzero(corners[i])
    objects.append([lines_count, edges_count, corners_count])

# Train a classifier to recognize the objects based on their features
X = np.array(objects)
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
classifier = make_pipeline(StandardScaler(), SVC(gamma='auto'))
classifier.fit(X, y)

# Save the model to a file
joblib.dump(classifier, "model.joblib")
#model = joblib.load("model.joblib")
# Use the model to make predictions on new data
#predictions = model.predict(X_test)


# Test the classifier on a new image
new_image = cv2.imread("image2.jpg")
new_gray = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
new_lines = cv2.HoughLinesP(new_gray, 1, np.pi/180,
                            50, minLineLength=50, maxLineGap=10)
new_edges = cv2.Canny(new_gray, 50, 100)
new_corners = cv2.cornerHarris(new_gray, 2, 3, 0.04)
new_object = [len(new_lines), np.count_nonzero(new_edges),
              np.count_nonzero(new_corners)]
print(new_object)
prediction = classifier.predict([new_object])

class_names = ["1", "2", "3", "4", "5", "6", "7", "8", "Island", "plane"]
class_lookup = {i: class_name for i, class_name in enumerate(class_names)}
predicted_class_name = class_lookup[int(prediction)]

print("Predicted class:", predicted_class_name)

######
# As callable functions
'''
i# Set the directory containing the images
image_dir = "images/"
# Create an empty list to store the images
images = []


def preprocess_image(image):
    # Correct for lens distortion
    k = np.array([[1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0]])
    dist = np.array([0.0, 0.0, 0.0, 0.0])
    image = cv2.undistort(image, k, dist)

    # Enhance the contrast and sharpness
    image = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
    image = cv2.GaussianBlur(image, (5, 5), 0)

    return image


def extract_features(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges using the Canny edge detector
    edges = cv2.Canny(gray, 50, 100)

    # Extract lines using the Hough transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50,
                            minLineLength=50, maxLineGap=10)

    # Extract points using the Harris corner detector
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Count the number of lines, edges, and corners
    lines_count = len(lines)
    edges_count = np.count_nonzero(edges)
    corners_count = np.count_nonzero(corners)

    # Return the extracted features as a list
    return [lines_count, edges_count, corners_count]


def train_classifier(features):
    # Convert the features to a numpy array
    X = np.array(features)

    # Set the labels for the classes
    y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Create a pipeline to scale the features and train a classifier
    classifier = make_pipeline(StandardScaler(), SVC(gamma='auto'))

    # Train the classifier
    classifier.fit(X, y)

    return classifier


# Loop through the images in the directory
for file in os.listdir(image_dir):
    # Check that the file is an image
    if file.endswith(".jpg"):
        # Load the image
        image = cv2.imread(os.path.join(image_dir, file))
        # Preprocess the image (e.g., remove noise, enhance contrast)
        image = preprocess_image(image)
        # Add the image to the list
        images.append(image)
        # Extract features from the images
        features = extract_features(images)

        # Train the classifier
        classifier = train_classifier(features)
        print(classifier)

'''
