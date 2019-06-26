from digital_library import *

if __name__ == '__main__':
    f = filter(3)
    m = loadimg('lennaN.bmp')
    showimg(m)
    
    m = median(m, 3)
    m = median(m, 3)
    m = median(m, 3)
    showimg(m)

