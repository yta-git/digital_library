# digital_library

課題で作った画像にフィルタをかけるスクリプト

畳み込み，ぼかし，ノイズ除去などができる．

## 利用例
```python
from digital_library import *

if __name__ == '__main__':
    f = filter(3)
    m = loadimg('lennaN.bmp')
    showimg(m)
    
    m = median(m, 3)
    m = median(m, 3)
    m = median(m, 3)
    showimg(m)
```
