# -*- coding: utf-8 -*-
"""FER_demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cf-8Zvz-WR-aWqq-JYyqJIEVE-tC122-

## Facial Emotion Recognition
In this notebook file you can try the Facial expression recognition module which focuses on Video prediction in the cloud with Google Colaboratory GPU.

Ensure that you enable the Free GPU in Colab, and check it with the next cell.
"""

!pip install torch==2.3.0

!pip install torchaudio torchtext

!pip install torch==2.3.0 torchaudio torchtext

!pip install -q fer
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

# Upload your file
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from fer import Video
from fer import FER
import matplotlib.pyplot as plt
import os
import sys
# fn contains the video file name (Ensure that you only upload one file)
videofile = fn
# Face detection
detector = FER(mtcnn=True)
# Video predictions
video = Video(videofile)

# Output list of dictionaries
raw_data = video.analyze(detector, display=False)

# Convert to pandas for analysis
df = video.to_pandas(raw_data)
df = video.get_first_face(df)
df = video.get_emotions(df)

# Plot emotions
fig = df.plot(figsize=(15, 10), fontsize=26).get_figure()
# Filename for plot
fig.savefig('my_figure.png')