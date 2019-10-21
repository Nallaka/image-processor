import numpy as np
import cv2


def convolve(source=None, data_type=None, kernel=None, blur=None):
    if source is None:
        raise Exception("Error: Source does not exist")

    if kernel is None:
        raise Exception("Error: Kernel does not exist")

    src_height, src_width = np.shape(source)
    kernel_height, kernel_width = np.shape(kernel)

    kernel_size = kernel_height * kernel_width

    img_padd = (kernel_width - 1) // 2

    src_with_padd = cv2.copyMakeBorder(source, img_padd, img_padd, img_padd, img_padd, cv2.BORDER_REPLICATE)

    output = np.zeros((src_height, src_width), dtype=data_type)

    for y in range(img_padd, src_height + img_padd):
        for x in range(img_padd, src_width + img_padd):
            src_roi = src_with_padd[y - img_padd: y + img_padd + 1, x - img_padd:x + img_padd + 1]

            calc_roi = src_roi * kernel

            if blur:
                output[y - img_padd, x - img_padd] = (calc_roi.sum())/kernel_size
            else:
                output[y - img_padd, x - img_padd] = (calc_roi.sum())

    return output
