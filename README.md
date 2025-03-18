# Real-Time Finger and Thumb Counter with MediaPipe

This project demonstrates real-time finger and thumb counting using MediaPipe's hand tracking capabilities and OpenCV. It identifies extended fingers and the thumb, visually highlights their tips, and displays a dynamic count.

## Features

* **Real-time Hand Tracking:** Utilizes MediaPipe's hand landmark detection to identify hand landmarks.
* **Finger and Thumb Extension Detection:** Analyzes landmark positions to determine if fingers and the thumb are extended.
* **Visual Feedback:** Draws circles at the tips of detected fingers and the thumb for clear visualization.
* **Dynamic Counting:** Continuously updates and displays the count of extended fingers and the thumb.
* **OpenCV Integration:** Uses OpenCV for video capture and frame processing.

## Prerequisites

* Python 3.x
* MediaPipe
* OpenCV
  
## Installation

* Install the required libraries:

    ```bash
    pip install requirements.txt
    ```

## Usage

1.  Ensure you have a webcam connected or a video file available.

2.  Run the Python script:

    ```bash
    python main.py "C:\Users\YourName\Pictures\image.png" "D:\Videos\MyVideos\video.avi" False
    ```

3.  The application will open a window displaying the live video feed with hand tracking and finger counting.

4.  To use a video file instead of a webcam, change the `cv2.VideoCapture()` line in the `hand_counter.py` file to include the file path. For example: `cap = cv2.VideoCapture('your_video.mp4')`.

5.  Press 'q' to exit the application.

## Code Structure

* `hand_counter.py`: Main Python script that performs hand tracking and finger counting.

## Implementation Details

* The script uses MediaPipe's `Hands` model to detect hand landmarks.
* It then analyzes the relative positions of the landmarks to determine if a finger or thumb is extended.
* Circles are drawn at the fingertip and thumb tip locations using OpenCV's `cv2.circle()` function.
* The count of extended fingers and thumb is displayed on the video feed using `cv2.putText()`.

## Potential Improvements

* Implement gesture recognition based on finger combinations.
* Improve the accuracy of finger extension detection in challenging lighting conditions.
* Add user interface elements for controlling the application.
* Add the ability to track multiple hands.
* Optimize the code for better performance.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes or feature requests.

## License

[Your License (e.g., MIT License)]
