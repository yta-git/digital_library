from digital_library import *

if __name__ == '__main__':
    filter = filter(3)
    print(filter.high_pass_filter)
    RGB = loadimg('lenna.bmp')
    showimg(RGB)    
    r = RGBtoYCC(RGB)
    r[:, :, (1, 2)] = 128
    r = YCCtoRGB(r)

    r = conv(r, filter.high_pass_filter)

    #r = conv(r, filter.high_pass_filter)

    showimg(r)

