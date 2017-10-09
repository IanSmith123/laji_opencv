## 0x00 
> 笔记[地址](http://note.youdao.com/noteshare?id=39bc391ff241b5e339ad09b241a88146&sub=2AB358FAA018465E8A5C2E10407D8196)



学习一下opencv的函数的用法

Refer: 
- [很简单的入门](http://blog.csdn.net/u012005313/article/details/49365487)
- [还是很简单的知乎专栏](https://zhuanlan.zhihu.com/p/24425116)
- [Robomaster官方给的参考思路](http://mp.weixin.qq.com/s/1IhRLRV2oPopXC-sz4oS-w)
- [提取轮廓](http://baoxizhao.com/2017/03/18/python%20openCV%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86%E4%B9%8B%E6%8F%90%E5%8F%96%E8%BD%AE%E5%BB%93/)
- [处理像素点](http://python.jobbole.com/85254/)
- [稍微全面点的segmentfault](https://segmentfault.com/a/1190000003742422)
## 0x01 
```python
import cv2
```

打开文件，保存文件
```python
img = cv2.imread("test.png")
cv2.imwrite("test.jpg", img)
```


```python
type(img)
# output: <type 'numpy.ndarray'>
```

转换成为灰度图
```
img = cv2.imread("test.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
现在得gray就是一个灰度图了，使用方式和`img`一样


## 0x02 视频
可以直接打开本机摄像头或者读取视频
```python
cap = cv2.VideoCapture(0)
while True:
  ret, im = cap.read()
  cv2.imshow("camera", im)
  cv2.waitKey(100)
  if not os.path.exists('cap.png'):
    cv2.imwrite("cap.png", im)
```
逻辑上有点问题，但是大概是这个意思， `ret`是一个`Bool`值，表示操作成功或者失败， `im`是某一帧图像

```python
cap = cv2.VideoCapture("test.mp4")
```
其他的和上面打开本机摄像头操作一样了

## 0x03 提取图片轮廓

```python

def filter_carrot(im):
    '''
    type(im) = ndarray of a pic
    return null
    '''
    
    after = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # convert gray pic to binary
    ret, binary = cv2.threshold(after, 120, 255, cv2.THRESH_BINARY)
    print(ret)
    
    # find border line
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    # draw border line in source pic
    cv2.drawContours(im, contours, -1, (0,222,255), 2)
    
    
    cv2.imshow("img", im)
    cv2.waitKey()
    cv2.imwrite("bin.png", binary)

```


