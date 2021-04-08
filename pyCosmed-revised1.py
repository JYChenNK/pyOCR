###
# Author：  JYChen
# Time:     20200121
# Vision:   3.0
###
import os
import sys
import time
import numpy as np
from PIL import Image
# import serial

# serialPort="COM6"   #串口
# baudRate=115200     #波特率
# ser=serial.Serial(serialPort,baudRate,timeout=0.5)

# 数字区域在电脑屏幕上的坐标

loc_VO2 = {'left_top_x': 1740, 'left_top_y': 460, 'right_buttom_x': 1850, 'right_buttom_y': 500}
loc_VCO2 = {'left_top_x': 1740, 'left_top_y': 590, 'right_buttom_x': 1850, 'right_buttom_y': 625}
loc_VE = {'left_top_x': 1740, 'left_top_y': 330, 'right_buttom_x': 1850, 'right_buttom_y': 375}
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

# 标准Hash码
hash_vals = {
    "0": "111000111000000110111100001111000011111000111110011111100111111001111110001111100011111000111100001111001001100111000011",
    "1": "111111001111000000000000001110001111100011111000111110001111100011111000111110001111100011111000111110001111100011111000",
    "2": "110001111000000101111100111111001111110011111100111110011111000111100011110011111001111100111111001111110000000000000000",
    "3": "110001111000000111111001111111011111110111111001111100111000011111111001111111001111110011111100111111000011000100000111",
    "4": "111111111111101111110011111100111110101111101011110010111101101110111011001110110000000000000000111110111111101111111011",
    "5": "111111111000000110111111101111111011111110111111100001110000000111111000111111001111110011111100111111010011000100000111",
    "6": "111100011100000110011111001111110011111100111111010000110001100100111100011111000111110000111100001111001001100111000011",
    "7": "111111110000000011111100111111011111100111111001111100111111001111110111111001111110011111101111110011111100111111001111",
    "8": "111001111000000100111101001111000011110010111101100000011000000100111100011111000111111001111110001111000001100111000011", 
    "9": "110001111000000100111001011111000111110001111100001111000011100010000000111111001111110011111101111110010010001100000111",
    ".": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110000000000000000"
}

def get_screenshot():
    from PIL import ImageGrab
    image_vo2 = ImageGrab.grab([loc_VO2['left_top_x'], loc_VO2['left_top_y'], loc_VO2['right_buttom_x'], loc_VO2['right_buttom_y']])
    image_vco2 = ImageGrab.grab([loc_VCO2['left_top_x'], loc_VCO2['left_top_y'], loc_VCO2['right_buttom_x'], loc_VCO2['right_buttom_y']])
    image_ve = ImageGrab.grab([loc_VE['left_top_x'], loc_VE['left_top_y'], loc_VE['right_buttom_x'], loc_VE['right_buttom_y']])
    image_hr = ImageGrab.grab([loc_HR['left_top_x'], loc_HR['left_top_y'], loc_HR['right_buttom_x'], loc_HR['right_buttom_y']])
    return image_vo2, image_vco2, image_ve,image_hr

def get_img(img):

    box_o2 = ([loc_VO2['left_top_x'], loc_VO2['left_top_y'], loc_VO2['right_buttom_x'], loc_VO2['right_buttom_y']]) 
    box_co2 = ([loc_VCO2['left_top_x'], loc_VCO2['left_top_y'], loc_VCO2['right_buttom_x'], loc_VCO2['right_buttom_y']]) 
    box_oe = ([loc_VE['left_top_x'], loc_VE['left_top_y'], loc_VE['right_buttom_x'], loc_VE['right_buttom_y']]) 
    box_hr = ([loc_HR['left_top_x'], loc_HR['left_top_y'], loc_HR['right_buttom_x'], loc_HR['right_buttom_y']]) 
    image_vo2 = img.crop(box_o2)
    image_vco2 = img.crop(box_co2)
    image_ve = img.crop(box_oe)
    image_hr = img.crop(box_hr)
    return image_vo2, image_vco2, image_ve,image_hr

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
    # print('px',px)  
    # print('py',py) 
    #  
    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(len(px)):
        if px[x] > 0:
            x0.append(x)
    # print('x0',x0)    

    y0 = []
    for y in range(len(py)):
        if py[y] > 1:
            y0.append(y)
    # print('y0',y0)

    # 找出边界
    cut_list = [x0[0]]
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            # if abs(x0[i-1] - cut_list[-1]) < 35:
            cut_list.extend([x0[i - 1]+1, x0[i]])
    cut_list.append(x0[-1]+1)
            # elif abs(x0[i-1] - cut_list[-1]) < 16:
            #     cut_list.extend([x0[i-1]+1, x0[i-1]+8])
            #     cut_list.extend([x0[i-1]+8, x0[i]])
            # elif abs(x0[i-1] - cut_list[-1]) < 24:
            #     cut_list.extend([x0[i-1]+1, x0[i-1]+8])
            #     cut_list.extend([x0[i-1]+8, x0[i-1]+16])
            #     cut_list.extend([x0[i-1]+16, x0[i]])
    
    # if abs(x0[-1] - cut_list[-1]) < 35:
    #     cut_list.append(x0[-1]+1)
    # elif abs(x0[-1] - cut_list[-1]) < 17:
    #     cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
    #     cut_list.append(x0[-1]+1)
    # elif abs(x0[-1] - cut_list[-1]) < 25:
    #     cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
    #     cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
    #     cut_list.append(x0[-1]+1)
    
    # print('cut_list',cut_list)

    cut_list_y = [y0[0]]
    cut_list_y.append(y0[-1]+1)

    # print('cut_list_y',cut_list_y)

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


def hamming(hash1, hash2):
    """计算汉明距离"""
    if len(hash1) != len(hash2):
        print('hash1: ', hash1)
        print('hash2: ', hash2)
        raise ValueError("Undefined for sequences of unequal length")  #异常
   #返回hash1[i]!=hash2[i]的个数 两个等长字符串s1与s2之间的汉明距离定义为将其中一个变为另外一个所需要作的最小替换次数。例如字符串“1111”与“1001”之间的汉明距离为2。
    return sum(i != j for i, j in zip(hash1, hash2)) 

def recognize(img):
    """识别部分"""
    img = binarize(img)
    chars = vertical_cut(img)
    # print ('chars',chars)
    # 相近度列表
    nearness = {}
    expr = ''
    for char in chars:
        hash_val = hashing(char)
        # print ('hash_val',hash_val)
        for h in hash_vals:
            nearness[h] = hamming(hash_val, hash_vals[h])
        expr += sorted(nearness.items(), key=lambda d: d[1])[0][0]
        # print('expr: ', sorted(nearness.items(), key=lambda d: d[1]))
       # sorted(d.items(), key=lambda x: x[1]) 中 d.items() 为待排序的对象；key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序
    return expr

if __name__ == '__main__':
    last_string = ''
    i=0
    while 1:
        
        #img=Image.open("C:\\Users\\Administrator\\Desktop\\4.0\\newpic\\capture\\12.png")
        Image_VO2,Image_VCO2,Image_VE,Image_HR=  get_screenshot()

        string_vo2 = recognize(Image_VO2)
        string_vco2 = recognize(Image_VCO2)
        string_ve = recognize(Image_VE)
        string_hr = recognize(Image_HR)
        string = string_vo2 + ',' + string_vco2  + ',' + string_ve + ',' + string_hr
           
        
        if string != last_string:
            time.sleep(0.05)
            mage_VO2,Image_VCO2,Image_VE,Image_HR=  get_screenshot()
            # i = i+1
            # Image_VO2.save(str(i)+".png")
            # i = i+1
            # Image_VCO2.save(str(i)+".png")

            string_vo2 = recognize(Image_VO2)
            string_vco2 = recognize(Image_VCO2)
            string_ve = recognize(Image_VE)
            string_hr = recognize(Image_HR)
            string = string_vo2 + ',' + string_vco2  + ',' + string_ve+ ',' + string_hr
            print(string)
            # ser.write((string+'\n').encode())
            last_string = string        
       
# ser.close()
        