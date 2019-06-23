from digital_library import *

if __name__ == '__main__':
    RGB = loadimg('lenna.bmp')
    showimg(RGB)
    YCC = RGBtoYCC(RGB)
    YCC1 = conv(YCC, 'Y')
    YCC2 = conv(YCC, 'Cb')
    YCC3 = conv(YCC, 'Cr')
    showimg(YCCtoRGB(YCC1))
    showimg(YCCtoRGB(YCC2))
    showimg(YCCtoRGB(YCC3))
