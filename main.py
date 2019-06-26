from digital_library import *

if __name__ == '__main__':
    filter = filter(9)
    RGB = loadimg('lennaN.bmp')
    showimg(RGB)

    r = RGBtoYCC(RGB)
    r = YCCtoRGB(r)

    r = median(r, 2)
    showimg(r)

