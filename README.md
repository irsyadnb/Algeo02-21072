# Linear Aljebra and Geometry Project
Face Recognition using Eigenface with PCA Algorithm.

(KOMUKEIGEN) :
  - Irsyad Nurwidianto Basuki (13521072)
  - Muhammad Zaydan Athallah (13521104)

## Table of Contents
* [General Information](#general-information)
* [Technology Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Acknowledgements](#acknowledgements)

## General Information
This program can match a person's face image with another face image (Face Recognition). Face Recognition in this program is made using the OpenCV library to process images into matrices. The matrix will be processed in such a way and later compared with the matrix of other images using the eigenfaces method. The program will produce the most similar image from the test image given by the user.

The outline of the algorithm used is by reducing dimensions and using linear algebra concepts to recognize faces. Starting with processing a large dataset and then processed using covariance matrices and QR decomposition to obtain eigenvalues and eigenvectors. Next is the processing of the generated eigenfaces and obtaining weights from each eigenface. For face recognition, it can be done by calculating the Euclidean distance.

> Note: This program is not 100% accurate, so there are often mismatches between the tested image and the resulting most similar image.


## Technology Used
Programming Language : 
- Python

Libraries : 
- OpenCV
- Numpy
- Os
- Pathlib
- Tkinter
- PIL


## Features
1. Import dataset from GUI
2. Import test image from GUI
3. Real-time face recognition
4. Output closest picture similarity


## Setup
Here are the steps for installing each libraries ;
- pip install opencv-python
- pip install numpy (Numpy)
- pip install tk (Tkinter)
- pip install --upgrade Pillow (PIL)

Here are the steps to use the program:

Run gui.py in the terminal (with Python3 installed).
1. Click the "Choose File" button under the "INSERT YOUR DATASET" text to select the dataset folder.
2. Click the "Choose File" button under the "INSERT YOUR IMAGE" text to select the image you want to test.
3. Make sure the image displayed in the "TEST IMAGE" section is the one you want to test.
4. Click the "START" button to start processing the image.
5. Wait for the image processing to complete.
6. The program will display the resulting matched image and the processing time.

Here are the steps to use the real-time program:
1. Click the "Choose File" button under the "INSERT YOUR DATASET" text to select the dataset folder.
2. Click the "Real-Time" button to use the camera feature.
3. Press 'a' on the keyboard to scan a face.
4. Press 'q' on the keyboard to view the scanned face result.
5. You can press 'a' multiple times to rescan before pressing 'q'.
Note: For macOS users, please replace the two backslashes (\) with one forward slash (/) in gui.py.
