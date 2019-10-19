import numpy as np


def kernal_convul(source=None, kernal=None):
    if source is None:
        raise Exception("Error: Source does not exist")

    if kernal is None:
        raise Exception("Error: Kernal does not exist")

    result = np.array([[0]])

    img_heignt, img_length = source.shape

    return
