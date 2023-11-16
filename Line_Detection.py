import cv2
import numpy as np
import paho.mqtt.client as mqtt


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Line Detected")
client.connect(mqttBroker)

video = cv2.VideoCapture("Blue_line5.mp4")

while True:
    ret, orig_frame = video.read()

    if not ret:
        video = cv2.VideoCapture("Blue_line5.mp4")
        continue
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_blue = np.array([108, 30, 17])
    up_blue = np.array([208, 224, 63])
    mask = cv2.inRange(hsv, low_blue, up_blue)
    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, maxLineGap=75)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            while True:
                detected = cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                if detected is True:
                    push = 1
                client.publish("Line", 1)
                cv2.putText(frame, "Line Detected", (110, 250), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
                print("Line Detected")
                break

    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    key = cv2.waitKey(25)

    if key == 27:
        break
video.release()
cv2.destroyAllWindows()