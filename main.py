from digital_library import *

if __name__ == '__main__':
    RGB = loadimg('lenna.bmp')
    # showimg(RGB)
    YCC = RGBtoYCC(RGB)

    YCC1 = conv(YCC, 1, 'Y')

    showimg(YCC1)

    # showimg(YCCtoRGB(YCC1))
    # nshowimg(YCCtoRGB(YCC2))
    # showimg(YCCtoRGB(YCC3))
