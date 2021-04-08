import os
import sys
import time
import numpy as np
from PIL import Image
#import serial
import json
from config import threshold
from config import threshold1
from config import location_VO2 as loc_VO2
from config import location_VCO2 as loc_VCO2
from config import location_HR as loc_HR

#serialPort="COM6"   #串口
baudRate=115200       #波特率
#ser=serial.Serial(serialPort,baudRate,timeout=0.5)

def get_screenshot():
    from PIL import ImageGrab
    image_vo2 = ImageGrab.grab([loc_VO2['left_top_x'], loc_VO2['left_top_y'], loc_VO2['right_buttom_x'], loc_VO2['right_buttom_y']])
    image_vco2 = ImageGrab.grab([loc_VCO2['left_top_x'], loc_VCO2['left_top_y'], loc_VCO2['right_buttom_x'], loc_VCO2['right_buttom_y']])
    image_hr = ImageGrab.grab([loc_HR['left_top_x'], loc_HR['left_top_y'], loc_HR['right_buttom_x'], loc_HR['right_buttom_y']])
    return image_vo2,image_vco2,image_hr

def get_screenshot_VCO2():
    from PIL import ImageGrab
    image_vco2 = ImageGrab.grab([loc_VCO2['left_top_x'], loc_VCO2['left_top_y'], loc_VCO2['right_buttom_x'], loc_VCO2['right_buttom_y']])
    image_vco2.show()
    return image_vco2

def binarize(img, threshold=threshold):
    """二值化"""
    img = img.convert('L')
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    bin_img = img.point(table, '1')
    return bin_img


def binarize1(img, threshold=threshold1):
    """二值化"""
    img = img.convert('L')
    table = []
    for i in range(256):
        if i < threshold1:
            table.append(0)
        else:
            table.append(1)
    bin_img = img.point(table, '1')
    return bin_img

def vertical_cut(img):
    """纵向切割"""
    _, height = img.size
    px = list(np.sum(np.array(img) == 0, axis=0))
    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(len(px)):
        if px[x] > 1:

            x0.append(x)
    # 找出边界
    cut_list = [x0[0]]
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            cut_list.extend([x0[i - 1]+1, x0[i]-1])
    cut_list.append(x0[-1]+1)

    cut_imgs = []
    # 切割顺利的话应该是整对
    if len(cut_list) % 2 == 0:
        for i in range(len(cut_list) // 2):
            cut_img = img.crop([cut_list[i * 2], 0, cut_list[i * 2 + 1], height])
            cut_imgs.append(cut_img)
        return cut_imgs
    else:
        print('Vertical cut failed.')
        return

def hashing(img):
    """计算哈希值"""
    img = img.resize((20, 30), Image.LANCZOS).convert("L")
    px = np.array(img).flatten()
    hash_val = (px > px.mean()).astype(int)
    hash_val = ''.join(str(e) for e in hash_val)
    return hash_val


def hamming(hash1, hash2):
    """计算汉明距离"""
    if len(hash1) != len(hash2):
        print('hash1: ', hash1)
        print('hash2: ', hash2)
        raise ValueError("Undefined for sequences of unequal length")

    return sum(i != j for i, j in zip(hash1, hash2))

def recognize(img):
    """输入：经过裁剪的只含有算式的区域图像"""
    img = img.convert('L')
    img = binarize(img)

    chars = vertical_cut(img)

    with open('hash.json', 'r') as fp:
        hash_vals = json.load(fp)

    # 相近度列表
    nearness = {}
    expr = ''
    for char in chars:
        hash_val = hashing(char)
        #print (hash_val)
        for h in hash_vals:
            nearness[h] = hamming(hash_val, hash_vals[h])
        expr += sorted(nearness.items(), key=lambda d: d[1])[0][0]

    return expr

def recognize1(img):
    """输入：经过裁剪的只含有算式的区域图像"""
    img = img.convert('L')
    img = binarize1(img)

    chars = vertical_cut(img)

    with open('hash1.json', 'r') as fp:
        hash_vals = json.load(fp)

    # 相近度列表
    nearness = {}
    expr = ''
    for char in chars:
        hash_val = hashing(char)
        #print (hash_val)
        for h in hash_vals:
            nearness[h] = hamming(hash_val, hash_vals[h])
        expr += sorted(nearness.items(), key=lambda d: d[1])[0][0]

    return expr

if __name__ == '__main__':
    last_string = ''
    i=0
    j=0
    while 1:
        Image_VO2,Image_VCO2,Image_HR = get_screenshot()

        string_vo2 = recognize(Image_VO2)
        string_vco2 = recognize(Image_VCO2)
        string_hr = recognize1(Image_HR)
        string = string_vo2 + ',' + string_vco2 + ',' + string_hr

        if string != last_string:
            time.sleep(0.05)
            Image_VO2,Image_VCO2,Image_HR  = get_screenshot()

            i = i+1
            Image_VO2.save("img\\"+str(i)+".png")
            i = i+1
            Image_VCO2.save("img\\"+str(i)+".png")
            j = j+1
            Image_HR.save("img\\HR"+str(j)+".png")

            string_vo2 = recognize(Image_VO2)
            string_vco2 = recognize(Image_VCO2)
            string_hr = recognize1(Image_HR)
            string = string_vo2 + ',' + string_vco2 + ',' + string_hr
            print(string)
            #ser.write((string+'\n').encode())
            last_string = string

#ser.close()
