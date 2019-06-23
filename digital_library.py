import numpy as np
from itertools import product
from PIL import Image

def conv(m, t):
    m = m.copy()
    tmp_m = np.zeros_like(m, np.float)
    X, Y = m.shape[:-1]
    for x, y in product(range(X), range(Y)):
        sum = np.array([.0, .0, .0])
        n = 0
        for dx, dy in product(range(-1, 2), range(-1, 2)):
            if 0 < x + dx < Y and 0 < y + dy < Y:
                sum += m[y + dy][x + dx]
                n += 1
        tmp_m[y][x] = sum / n

    if 'all' in t:
        return tmp_m

    if 'Y' in t:
        m[:, :, 0] = tmp_m[:, :, 0]
    
    if 'Cb' in t:
        m[:, :, 1] = tmp_m[:, :, 1]
    
    if 'Cr' in t:
        m[:, :, 2] = tmp_m[:, :, 2]

    return m

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
