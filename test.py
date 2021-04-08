import os
import sys
import time
import numpy as np
from PIL import Image

# 数字区域在电脑屏幕上的坐标
location_HR = {'left_top_x': 1645, 'left_top_y': 206, 'right_buttom_x': 1720, 'right_buttom_y': 244}
loc_VO2 = {'left_top_x': 0, 'left_top_y': 0, 'right_buttom_x': 111, 'right_buttom_y': 144}
loc_VCO2 = {'left_top_x': 1645, 'left_top_y': 430, 'right_buttom_x': 1720, 'right_buttom_y': 462}

# 二值化阈值，自定义阈值为150, 小于150的是白色0 大于的是黑色1
threshold = 150
# 二值化对照表
bin_table = []
for i in range(256):
    if i < threshold:
        bin_table.append(0)
    else:
        bin_table.append(1)

def get_screenshot():
    from PIL import ImageGrab
    image_vo2 = ImageGrab.grab([loc_VO2['left_top_x'], loc_VO2['left_top_y'], loc_VO2['right_buttom_x'], loc_VO2['right_buttom_y']])
    image_vco2 = ImageGrab.grab([loc_VCO2['left_top_x'], loc_VCO2['left_top_y'], loc_VCO2['right_buttom_x'], loc_VCO2['right_buttom_y']])
    return image_vo2,image_vco2

if __name__ == '__main__':
     from PIL import ImageGrab
     im=Image.open("E:\\HANH\\PyCosmed\\v3.0\\img1\\7.png") 
     im = im.convert('L')
     bin_img = im.point(bin_table, '1')
     print(bin_img.size)

     bin_img1=np.array(bin_img)
     print('bin_img1', bin_img1)

     px = list(np.sum(np.array(bin_img) == 0, axis=0)) #列
     py = list(np.sum(np.array(bin_img) == 0, axis=1)) #行
     print('px',px)
     print('py',py)
     # 列表保存像素累加值大于0的列
     x0 = []
     for x in range(len(px)):
        if px[x] > 0:
            x0.append(x)
     print('x0',x0)

     y0 = []
     for y in range(len(py)):
        if py[y] > 1:
            y0.append(y)
     print('y0',y0)


     

    
     
     

    
