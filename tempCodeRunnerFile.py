        video = cv2.VideoCapture("Blue_line5.mp4")
        continue
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_blue = np.array([108, 30, 17])
    up_blue = np.array([208, 224, 63])
    mask = cv2.inRange(hsv, low_blue, up_blue)
    edges = cv2.Canny(mask, 75, 150)

    lines 