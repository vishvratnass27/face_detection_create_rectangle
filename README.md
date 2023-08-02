# face_detection_create_rectangle

Face Detection and Cropping
This repository contains a Python script that utilizes OpenCV to detect faces in images or videos captured from a webcam. It provides three services:

Detect and Show Image: The script captures an image from the webcam and uses a Haar Cascade classifier to detect faces. It then draws rectangles around the detected faces and displays the image.

Detect and Show Video: The script captures a continuous video stream from the webcam. It detects faces in each frame using the Haar Cascade classifier and displays the video with rectangles drawn around the detected faces.

Detect, Show Video, and Crop: Similar to the second service, but in addition to showing the video with rectangles around the detected faces, it crops the detected face region and displays it in a fixed-sized window on the video frame.

Dependencies
Python
OpenCV
matplotlib
numpy

How to Use
Clone the repository to your local machine.
Make sure you have Python installed along with the required dependencies listed above.
Run the "face_detection.py" script.
Choose one of the provided services (1, 2, or 3) by entering the corresponding number.
If you select option 1 or 2, the webcam will be activated, and faces will be detected in real-time.
If you select option 3, the video will be displayed with detected faces, and a cropped version of the detected face will be shown in a separate window.
Note
Please ensure that you have the "myhaarcascade_frontalface_default.xml" file in the same directory as the script. This file is a pre-trained Haar Cascade classifier used for face detection.

About Haar Cascade Classifier
The Haar Cascade classifier is an object detection algorithm used to identify objects in images or video. In this script, we use a pre-trained Haar Cascade classifier specifically designed for face detection.

Author
The script was created by [vishvratna shegaonkar].
