import numpy as np
from itertools import product
from PIL import Image

class filter:
    def __init__(self, fsize, sigma=1.3): 
        if not fsize % 2:
            raise ValueError(f'fsize(={fsize}) should be odd value')

        print(f'using {fsize} * {fsize} filter')
        self.moving_average_filter = np.ones((fsize, fsize, 3), np.float) / fsize ** 2

        self.high_pass_filter = np.zeros((fsize, fsize, 3), np.float)
        self.high_pass_filter[:, 0] = -1
        self.high_pass_filter[:, -1] = 1

        self.laplacian_filter = np.zeros((fsize, fsize,3), np.float)
        self.laplacian_filter[fsize // 2, :] = 1
        self.laplacian_filter[:, fsize // 2] = 1
        self.laplacian_filter[fsize // 2, fsize // 2] = -4

        self.gaussian_filter = np.zeros((fsize, fsize, 3), np.float)
        for x, y in product(range(fsize), range(fsize)):
            self.gaussian_filter[y, x] = 1/2/np.pi/sigma**2 * np.exp(-(((x-fsize//2)**2 + (y-fsize//2)**2) / 2 / sigma**2))

def extend(mat, grid):
    exmat = mat.copy()
    exmat = np.concatenate(([exmat[0]] * grid, exmat), axis=0)
    exmat = np.concatenate((exmat, [exmat[-1]] * grid), axis=0)
    exmat = np.concatenate((np.array([exmat[:, 0]] * grid).transpose(1, 0, 2), exmat), axis=1)
    exmat = np.concatenate((exmat, np.array([exmat[:, -1]] * grid).transpose(1, 0, 2)), axis=1)
    return exmat

def conv(mat, filter):
    X, Y = mat.shape[:-1]
    grid = (filter.shape[0] - 1) // 2
    exmat = extend(mat, grid)

    retm = np.zeros_like(mat, np.float)
    for x, y in product(range(grid, X + grid), range(grid, Y + grid)):
        u, d, l, r = y - grid, y + grid + 1, x - grid, x + grid + 1
        retm[y - grid, x - grid] = sum(sum(filter * exmat[u:d, l:r]))

    return retm

def median(mat, fsize):
    X, Y = mat.shape[:-1]
    grid = (fsize - 1) // 2
    exmat = extend(mat, grid)

    retm = np.zeros_like(mat, np.float)
    for x, y in product(range(grid, X + grid), range(grid, Y + grid)):
        u, d, l, r = y - grid, y + grid + 1, x - grid, x + grid + 1
        retm[y - grid, x - grid] = np.median(np.median(exmat[u:d, l:r], axis=0), axis=0)

    return retm

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
