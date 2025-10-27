import cv2
import numpy as np
import collections

drawing_points = collections.deque(maxlen=1024)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cv2.waitKey(1000)

lower_blue = np.array([100, 100, 100])
upper_blue = np.array([120, 255, 255])

print("Starting Air Painter...")
print("Move a blue object to draw.")
print("Press 'c' to clear the screen.")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                
                drawing_points.appendleft(center)

    for i in range(1, len(drawing_points)):
        if drawing_points[i - 1] is None or drawing_points[i] is None:
            continue
            
        cv2.line(frame, drawing_points[i - 1], drawing_points[i], (0, 255, 0), 5)

    cv2.imshow("Air Painter", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    
    if key == ord("c"):
        drawing_points.clear()

cap.release()
cv2.destroyAllWindows()