# AI-Gesture-Control (Scrolling of Shorts Using Computer Vision)


This project enables gesture-based control for scrolling through video shorts. Using a pre-trained YOLO model and computer vision techniques, the system recognizes hand gestures in real-time and simulates scrolling actions based on detected gestures. It provides a hands-free way to interact with video content.

## Features

- Real-time hand gesture recognition using YOLO.
- Detection of "up" and "down" gestures.
- Visualization of detected gestures with bounding boxes and       
  confidence scores.
- Simulated scrolling actions for gesture-based navigation.
- Adjustable region of interest for gesture validation.

## Requirements
- Python 3.x
- OpenCV (cv2)
- YOLOv5 model weights (v23.pt)
- ultralytics library
- numpy
- keyboard (for simulating key presses)

### How to install requirements
`
pip install -r requirements.txt
`
### How to run source code
`
python shortsrun.py
`

