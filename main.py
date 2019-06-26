from digital_library import *

if __name__ == '__main__':
    f = filter(5)
    m = loadimg('lennaN.bmp')
    showimg(m)
    m = conv(m, f.gaussian_filter)
    showimg(m)

