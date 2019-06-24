import numpy as np
from itertools import product
from PIL import Image
class filter:
    def __init__(self, fsize): 
        self.moving_average_filter = np.ones((fsize, fsize, 3), np.float) / fsize ** 2
        self.ones_filter = np.ones((fsize, fsize, 3), np.float)
        self.high_pass_filter = np.zeros((fsize, fsize), np.float)
        self.high_pass_filter[:, 0] = -1
        self.high_pass_filter[:, -1] = 1

class conv2D(filter):
    def __init__(self, mat, window):
        self.mat = mat
        self.window = window
        self.target = target
        super().__init__(1 + 2 * window)
    
    def extend_mat(self):
        exmat = self.mat.copy()

    def moving_average(self, target):
        



    def moving_average(self, exmat)

def conv(mat, mode, window, terget):
    retmat = mat.copy()
    exmat = mat.copy()
    X, Y = mat.shape[:-1]
    fsize = 1 + 2 * window
    print(f'using {fsize} * {fsize} filter')

    exmat = np.concatenate(([exmat[0]] * window, exmat), axis=0)
    exmat = np.concatenate((exmat, [exmat[-1]] * window), axis=0)
    exmat = np.concatenate((np.array([exmat[:, 0]] * window).transpose(1, 0, 2), exmat), axis=1)
    exmat = np.concatenate((exmat, np.array([exmat[:, -1]] * window).transpose(1, 0, 2)), axis=1)

    filter = np.ones((fsize, fsize, 3), np.float) / fsize ** 2
    tmp_m = np.zeros_like(mat, np.float)
    
    for x, y in product(range(window, X + window), range(window, Y + window)):
        u, d, l, r = y - window, y + window + 1, x - window, x + window + 1
        tmp_m[y - window, x - window] = sum(sum(filter * exmat[u:d, l:r]))

    print(tmp_m)

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
