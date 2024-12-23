import cv2
import os

# Print OpenCV version
print(cv2.__version__)

# Define paths
cascade_src = 'cars.xml'
video_src = "C:\\Users\\user\\Desktop\\Edgematrix\\day3\\vehicle detection.mp4"
output_folder = "detected_cars"

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize video and cascade
cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

frame_count = 0  # Counter for saving unique images

while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        # Draw rectangle around the car
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)o

        # Save the cropped car image
        car_image = img[y:y + h, x:x + w]
        file_name = os.path.join(output_folder, f"car_{frame_count}.jpg")
        cv2.imwrite(file_name, car_image)
        frame_count += 1

    # Display the video
    cv2.imshow('video', img)

    # Exit the loop when 'Esc' key is pressed
    if cv2.waitKey(33) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
