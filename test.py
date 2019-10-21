import KernelConvolve as convolve
import numpy as np
import cv2

src = cv2.imread("demos/images/steam-engine.png")
src_gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

gaussian_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
edge = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

gaussian = convolve.convolve(src_gray, "float32", gaussian_kernel, True)
output = convolve.convolve(gaussian, "float32", edge, True)
cv2.imshow("steam-gray", src_gray)
cv2.imshow("steam-gaussian", gaussian)
cv2.imshow("steam-output", output)
cv2.waitKey(0)
