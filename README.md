# Face-Detector-Emotion-Recognizer
Welcome to the Face Detector &amp; Emotion Recognizer project! This repository integrates deep learning techniques to provide accurate face recognition and facial emotion detection. Leveraging usage of OpenCV for robust image processing, TensorFlow/Keras for model training and inference, and Dlib for precise facial landmark detection.

### Face Recognition with Video Processing
This project implements face recognition using the face_recognition library in Python. It captures video frames, processes them to detect and recognize known faces, and displays the results in real-time.

Here's a  workflow for the face recognition project :-

1)Setup Environment: Install necessary libraries like dlib, face_recognition, and opencv-python-headless.

2)Upload Video: Use Google Colab's file upload feature to upload a video for processing.

3)Load Known Faces: Load images of known faces and encode them using face_recognition.

4)Process Video Frames: Read each frame from the uploaded video, detect faces, and compare them with the known faces. If a match is found, label the face with the corresponding name.

5)Display Results: Display the processed frames with bounding boxes and labels for recognized faces.

6)End Processing: Stop processing frames when the video ends or when the user interrupts the process.

### Facial Emotion Recognition
This project uses the fer library to analyze a video file, detecting faces and recognizing emotions such as happiness, sadness, anger, etc. It utilizes a deep learning model for facial emotion recognition and outputs the results in a pandas DataFrame for further analysis and visualization.

Here's a workflow for facial emotion recognition using :-

1)Environment Setup: Install necessary libraries (torch, torchaudio, torchtext, fer).

2)Upload Video: Use Google Colab to upload a video file.

3)Face Detection and Emotion Recognition:

Use the FER class from fer to analyze the video for faces and emotions.Obtain raw data on face locations and detected emotions.

4)Data Processing:

Convert the raw data into a pandas DataFrame for easier manipulation.Extract information about the first detected face and its emotions.

5)Visualization:

Plot the emotions detected in the video using matplotlib.Save the plot as an image file for further analysis.

![111](https://github.com/Priyancy15/Face-Detector-Emotion-Recognizer/assets/173549133/cdfaf008-03fe-4d82-8280-e87fb2ed0046)

