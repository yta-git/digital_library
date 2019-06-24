from digital_library import *

np.set_printoptions(100)

if __name__ == '__main__':
    RGB = loadimg('lennaN.bmp')
    showimg(RGB)
    YCC = RGBtoYCC(RGB)
    YCC = conv(YCC, 'average', 2, 'all')
    showimg(YCCtoRGB(YCC))
        
    #YCC1 = conv(YCC, 1, 'Y')

    #showimg(YCC1)

    #showimg(YCCtoRGB(YCC1))
    # nshowimg(YCCtoRGB(YCC2))
    # showimg(YCCtoRGB(YCC3))
