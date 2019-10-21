import KernelConvolve2 as convolve
import numpy as np
import cv2

src = cv2.imread("demos/images/bee.jpg")
src_gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

gaussian_kernel = (1/16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
edge = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
gaussian = convolve.convolve(src_gray, "float32", gaussian_kernel)
gaussian_normal = gaussian/255
edge_out = convolve.convolve(gaussian_normal, "float32", edge)
gx_out = convolve.convolve(gaussian_normal, "float32", gx)
gy_out = convolve.convolve(gaussian_normal, "float32", gy)

print(src_gray)
print(gaussian)
print(gx_out)

cv2.imshow("steam-gray", src_gray)
cv2.imshow("steam-gaussian", gaussian_normal)
cv2.imshow("edge", edge_out)
cv2.imshow("gx_out", gx_out)
cv2.imshow("gy_out", gy_out)
cv2.imshow("sobel", gx_out * gy_out)
cv2.waitKey(0)

