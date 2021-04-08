import os
import sys
import time
import numpy as np
from PIL import Image

# 数字区域在电脑屏幕上的坐标
loc_VO2 = {'left_top_x': 1740, 'left_top_y': 460, 'right_buttom_x': 1850, 'right_buttom_y': 500}
loc_VCO2 = {'left_top_x': 1740, 'left_top_y': 590, 'right_buttom_x': 1850, 'right_buttom_y': 625}
loc_VO2_kg = {'left_top_x': 1740, 'left_top_y': 720, 'right_buttom_x': 1850, 'right_buttom_y': 750}
loc_HR = {'left_top_x': 1740, 'left_top_y': 970, 'right_buttom_x': 1850, 'right_buttom_y': 1005}

# 二值化阈值，自定义阈值为150, 小于150的是白色0 大于的是黑色1
threshold = 150
# 二值化对照表
bin_table = []
for i in range(256):
    if i < threshold:
        bin_table.append(0)
    else:
        bin_table.append(1)

def get_screenshot(img):

    box = ([loc_HR['left_top_x'], loc_HR['left_top_y'], loc_HR['right_buttom_x'], loc_HR['right_buttom_y']]) 
    region = img.crop(box)
    return region

def binarize(img, threshold=threshold):
    """二值化""" 
    # 图像的二值化，就是将图像上的像素点的灰度值设置为0或255，也就是将整个图像呈现出明显的只有黑和白的视觉效果。

    img = img.convert('L')  #模式“L” 为灰色图像,它的每个像素用8个bit表示,0表示黑,255表示白,其他数字表示不同的灰度。
     #img.point 返回图像的副本，参数1：每个像素通过给定的bin_table表映射。该表应包含图像中每个波段的256个值。
     #                         参数2：仅当源图像的模式为“L”或“P”且输出的图像模式为“1”或源图像的模式为“I”且输出模式为“L”时，才可以使用此选项
    bin_img = img.point(bin_table, '1')
    return bin_img

def vertical_cut(img):
    """纵向切割"""
    
    # 黑白反转
    px = list(np.sum(np.array(img) == 0, axis=0)) #列 像素累加值
    py = list(np.sum(np.array(img) == 0, axis=1)) #行 像素累加值
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

    # 找出边界
    cut_list = [x0[0]]
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            # if abs(x0[i-1] - cut_list[-1]) < 35:
            cut_list.extend([x0[i - 1]+1, x0[i]])
            # elif abs(x0[i-1] - cut_list[-1]) < 16:
            #     cut_list.extend([x0[i-1]+1, x0[i-1]+8])
            #     cut_list.extend([x0[i-1]+8, x0[i]])
            # elif abs(x0[i-1] - cut_list[-1]) < 24:
            #     cut_list.extend([x0[i-1]+1, x0[i-1]+8])
            #     cut_list.extend([x0[i-1]+8, x0[i-1]+16])
            #     cut_list.extend([x0[i-1]+16, x0[i]])
    cut_list.append(x0[-1]+1)
    # if abs(x0[-1] - cut_list[-1]) < 35:
    #     cut_list.append(x0[-1]+1)
    # elif abs(x0[-1] - cut_list[-1]) < 17:
    #     cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
    #     cut_list.append(x0[-1]+1)
    # elif abs(x0[-1] - cut_list[-1]) < 25:
    #     cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
    #     cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
    #     cut_list.append(x0[-1]+1)
    
    print('cut_list',cut_list)

    cut_list_y = [y0[0]]
    cut_list_y.append(y0[-1]+1)

    print('cut_list_y',cut_list_y)

    cut_imgs = []
    # 切割顺利的话应该是整对
    if len(cut_list) % 2 == 0:
        for i in range(len(cut_list) // 2):   #每张图片的左右边界
            cut_img = img.crop([cut_list[i * 2], cut_list_y[0], cut_list[i * 2 + 1], cut_list_y[1]])
            cut_imgs.append(cut_img)
        return cut_imgs
    else:
        print('Vertical cut failed.')
        return

def hashing(img):
    """计算哈希值"""
    # img.resize((width, height),Image.ANTIALIAS)  第二个参数：Image.NEAREST ：低质量 Image.BILINEAR：双线性 Image.BICUBIC ：三次样条插值 Image.ANTIALIAS：高质量
    img = img.resize((8, 15), Image.LANCZOS)
    px = np.array(img).flatten()     #flatten()把数组降到一维，默认是按行的方向降
    hash_val = (px).astype(int)
    hash_val = ''.join(str(e) for e in hash_val) #以''作为分隔符，将hash_val所有的元素合并成一个新的字符串，返回值：返回一个以分隔符''连接各个元素后生成的字符串
    return hash_val


if __name__ == '__main__':

    img=Image.open("E:\\HANH\\PyCosmed\\v3.0\\newpic\\capture\\10.png")
    width, height=img.size
    print(img.size)
    reg_img = get_screenshot(img)
    i=27
    # reg_img.show()
    bin_img = binarize(reg_img)
    # bin_img.show()
    chars = vertical_cut(bin_img)
    for char in chars:
        newName = "./newpic/chars/" + str(i) + ".jpg"
        char.save(newName)
        hash_val = hashing(char)
        print ('hash_val',hash_val)
        i=i+1

    
