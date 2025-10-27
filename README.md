# -Air-Painter-using-OpenCV
A fun and simple Python project that uses OpenCV to turn your webcam into an interactive drawing canvas. This program allows you to draw on the screen simply by moving a colored object (like a pen cap) .
✨ Features
Real-Time Drawing: See your lines appear instantly on the video feed.

Color Tracking: Uses HSV color space to accurately isolate and track a specific color.

Smooth Lines: Employs a deque (double-ended queue) to store a series of points, resulting in smooth, connected lines.

Easy Controls:

Press 'c' to clear the canvas and start over.

Press 'q' to quit the application.
🛠️ Technology Stack
Python 3

OpenCV: For video capture, color space conversion, contour detection, and drawing.

NumPy: For efficient array manipulation (handling video frames).
🚀 How to Use
1. Prerequisites
Ensure you have Python and pip installed on your system.

2. Installation
Install the required libraries using pip:

Bash

pip install opencv-python numpy
3. Run the Program
Save the code to a file (e.g., air_painter.py) and run it from your terminal:

Bash

python air_painter.py
(You may need to use py air_painter.py or python3 air_painter.py depending on your system setup.)

4. Start Drawing!
The program will open your webcam.

Hold a blue object (the default color) in front of the camera.

Move it around to draw. A red circle will track the object when detected.

Press 'c' to clear the drawing or 'q' to quit.

🎨 Changing the Tracked Color
If you want to use a different color (like green or red), you need to adjust the HSV (Hue, Saturation, Value) range in the code.

Modify these lines:

Python

# Default values for Blue
lower_color = np.array([100, 100, 100])
upper_color = np.array([120, 255, 255])

# Example for Green:
# lower_color = np.array([40, 100, 100])
# upper_color = np.array([80, 255, 255])
You will also need to update the cv2.inRange function call to use your new variable names.
