import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma

    # build lookup table, based on corrected values
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

# video capture
video_capture = cv2.VideoCapture(0)

g = 1.0
while (True):
	ret, frame = video_capture.read()
	final = adjust_gamma(frame, g)
	cv2.imshow("Gamma", final)
	k = cv2.waitKey(33)
	if k == ord('.'):
		g += 0.2
		print("Gamma: %.1f" % g)
	if k == ord(','):
		g -= 0.2
		print("Gamma: %.1f" % g)
	if k == ord('q'):
		exit()	
