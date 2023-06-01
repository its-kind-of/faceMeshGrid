# Face Detection using OpenCV and MediaPipe

This Python script demonstrates face detection using OpenCV and MediaPipe libraries. It can detect faces in a video feed or webcam input.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

Install the required dependencies using pip:

``` 
pip install opencv-python
pip install mediapipe 
```


## Usage

1. Clone the repository or download the Python script.

2. Run the script using the following command:

``` python face_detection.py ```

1. The script will use the default webcam as the video source. If you want to use a video file, uncomment the line that initializes the `cap` variable with the video file path.

2. The script will display the video feed with detected faces and the frames-per-second (FPS) information.

## Customization

You can modify the code to suit your needs:

- Adjust the `minDetectionCon` parameter in the `FaceDetector` class constructor to control the minimum confidence threshold for face detection.
- Modify the `fancyDraw` method in the `FaceDetector` class to customize the drawing of bounding boxes around the detected faces.
- Explore other functionalities provided by OpenCV and MediaPipe for further customization.

Feel free to experiment and integrate this face detection code into your own proj