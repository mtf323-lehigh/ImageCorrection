import cv2
import numpy as np

def adjust_gamma(image, gamma=2.0):
    inv_gamma = 1.0 / gamma

    # build lookup table, based on corrected values
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

# video capture
video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()

final = adjust_gamma(frame)
cv2.imshow("Gamma", final)
cv2.waitKey(5000)