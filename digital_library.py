import numpy as np
from itertools import product
from PIL import Image

def conv(mat, window, terget):
    retmat = exmat = mat.copy()
    X, Y = mat.shape[:-1]
    print(f'using {1 + 2 * window} * {1 + 2 * window} filter')

    exmat = np.concatenate(([exmat[0]] * window, exmat), axis=0)
    exmat = np.concatenate((exmat, [exmat[-1]] * window), axis=0)
    exmat = np.concatenate((np.array([exmat[:, 0]]).transpose(1,0,2), exmat), axis=1)
    exmat = np.concatenate((exmat, np.array([exmat[:, -1]]).transpose(1,0,2)), axis=1)

    filter = np.ones((3, 3, 3), np.float) / 9
    tmp_m = np.zeros_like(mat, np.float)

    for x, y in product(range(window, X), range(window, Y)):
        u, d, l, r = x - window, x + window + 1, y - window, y +  window + 1
        tmp_m[x, y] = np.sum(filter[:, :] * exmat[u:d, l:r])

    if 'all' in terget:
        return tmp_m

    if 'Y' in terget:
        retmat[:, :, 0] = tmp_m[:, :, 0]
    
    if 'Cb' in terget:
        retmat[:, :, 1] = tmp_m[:, :, 1]
    
    if 'Cr' in terget:
        retmat[:, :, 2] = tmp_m[:, :, 2]

    return retmat


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
