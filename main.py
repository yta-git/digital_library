from digital_library import *

np.set_printoptions(100)

if __name__ == '__main__':
    filter = filter(5)
    RGB = loadimg('lennaN.bmp')
    showimg(RGB)
        
    YCC = RGBtoYCC(RGB)
    r = median(YCC, 3)
    showimg(YCCtoRGB(r))
    
    #YCC = conv(RGBtoYCC(RGB), filter.gaussian_filter)
    #showimg(YCCtoRGB(YCC))