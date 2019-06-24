import numpy as np
from itertools import product
from PIL import Image

def conv(mat, window, terget):
    mat = mat.copy()
    
    mat = np.concatenate(([mat[0]] * window, mat), axis=0)
    mat = np.concatenate((mat, [mat[-1]] * window, mat), axis=0)
    mat = np.concatenate((np.array([mat[0]] * window).T, mat), axis=1)
    

    tmp_m = np.zeros_like(mat, np.float)

    
    X, Y = mat.shape[:-1]

    filter = np.ones((3, 3, 3), np.float) / 9

    



    for x, y in product(range(X), range(Y)):
        u = max(0, x - window)
        d = min(X, x + window + 1)
        l = max(0, y - window)
        r = min(Y, y +  window + 1)

        tmp_m = sum(filter[:, :] * mat[u:d, l:r, :])

    if 'all' in terget:
        return tmp_m

    if 'Y' in terget:
        mat[:, :, 0] = tmp_m[:, :, 0]
    
    if 'Cb' in terget:
        mat[:, :, 1] = tmp_m[:, :, 1]
    
    if 'Cr' in terget:
        mat[:, :, 2] = tmp_m[:, :, 2]

    return mat


def RGBtoYCC(RGB):
    YCC = np.zeros_like(RGB, np.float)

    YCC[:, :, 0] = 0.299 * RGB[:, :, 0] + 0.587 * RGB[:, :, 1] + 0.144 * RGB[:, :, 2]
    YCC[:, :, 1] = - 0.168736 * RGB[:, :, 0] - 0.331264 * RGB[:, :, 1] + 0.5 * RGB[:, :, 2] + 128
    YCC[:, :, 2] = 0.5 * RGB[:, :, 0] - 0.418688 * RGB[:, :, 1] - 0.081312 * RGB[:, :, 2] + 128

    return YCC

def YCCtoRGB(YCC):
    RGB = np.zeros_like(YCC, np.float)
    YCC = YCC.copy()
    YCC[:, :, (1, 2)] -= 128

    RGB[:, :, 0] = 1.0 * YCC[:, :, 0] + 0 * YCC[:, :, 1] + 1.402 * YCC[:, :, 2]
    RGB[:, :, 1] = 1.0 * YCC[:, :, 0] - 0.344136 * YCC[:, :, 1] - 0.714136 * YCC[:, :, 2]
    RGB[:, :, 2] = 1.0 * YCC[:, :, 0] + 1.772 * YCC[:, :, 1] + 0 * YCC[:, :, 2]

    return RGB

def loadimg(path):
    return np.array(Image.open(path).convert('RGB'), np.float)

def showimg(RGB):
    Image.fromarray(RGB.astype(np.uint8)).show()
