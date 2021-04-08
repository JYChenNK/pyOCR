###
#   基于Hash码的图像识别示例（原始图片）
###

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 二值化阈值
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
    "0": "110000111000000110011001100110000001100000111100001111000011110000111100001111000001100010011001100110011000000111000011",
    "1": "111000000000000000000000111110001111100011111000111110001111100011111000111110001111100011111000111110001111100011111000",
    "2": "100000111000000111110001111110011111100111111001111110011111000111110011111000111100011111001111100111110000000000000000",
    "3": "100000111000000111111000111111001111110011111001110000011100000111111000111111001111110011111100111110000000000110000011",
    "4": "111100011111000111100001111000011100100111001001100110011001100100111001000000000000000011111001111110011111100111111001",
    "5": "110000001100000010011111100111111001111110011111100000111000000011111000111111001111110011111100111110000000000100000011",
    "6": "111110011110000111000111110011111001111110011111000000010000000100011000001111000011110000011100100110001000000111000011",
    "7": "000000000000000011111001111110011111100111110011111100111111001111100111111001111100011111001111110011111000111110011111",
    "8": "111000111100000110011000100111001001110010001001110000011100000110001000100111000001110000011100100111001000000011000011", 
    "9": "110000111000000110011001000110000011110000111100000111001001100010000000111010001111100111110001111000111000011110001111",
    ".": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111000000000000011100000"
}

def get_img(index):
    """读取图像"""

    img = Image.open("img1\\"+str(index)+".png")
    return img

# 分析灰度直方图，从而选择合适的二值化阈值
# def gray_hist(img):
#     img_arr = np.array(img.convert('L'))    #  convert - 转换图像格式   L - 八位黑白像素
#                                             #  array - image格式转为array数组
#     plt.subplot(223)
#     plt.imshow(img_arr)

#     img_arr = img_arr.flatten()             #  flatten - 转化为一维数组
#     plt.subplot(222)
#     plt.hist(img_arr,bins=256)              #  hist - 绘制直方图  bins - 条形数
#     plt.ylim((0,50))

def binarize(img, threshold=threshold):
    """二值化"""

    img = img.convert('L')
    bin_img = img.point(bin_table, '1')
    return bin_img

def vertical_cut(img):
    """纵向切割"""
    
    px = list(np.sum(np.array(img) == 0, axis=0))
    py = list(np.sum(np.array(img) == 0, axis=1))

    # 列表保存像素累加值大于0的列
    x0 = []
    for x in range(len(px)):
        if px[x] > 0:
            x0.append(x)
    y0 = []
    for y in range(len(py)):
        if py[y] > 1:
            y0.append(y)

    # 找出边界
    cut_list = [x0[0]]
    for i in range(1, len(x0)):
        if abs(x0[i] - x0[i - 1]) > 1:
            if abs(x0[i-1] - cut_list[-1]) < 10:
                cut_list.extend([x0[i - 1]+1, x0[i]])
            elif abs(x0[i-1] - cut_list[-1]) < 16:
                cut_list.extend([x0[i-1]+1, x0[i-1]+8])
                cut_list.extend([x0[i-1]+8, x0[i]])
            elif abs(x0[i-1] - cut_list[-1]) < 24:
                cut_list.extend([x0[i-1]+1, x0[i-1]+8])
                cut_list.extend([x0[i-1]+8, x0[i-1]+16])
                cut_list.extend([x0[i-1]+16, x0[i]])
    if abs(x0[-1] - cut_list[-1]) < 10:
        cut_list.append(x0[-1]+1)
    elif abs(x0[-1] - cut_list[-1]) < 17:
        cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
        cut_list.append(x0[-1]+1)
    elif abs(x0[-1] - cut_list[-1]) < 25:
        cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
        cut_list.extend([cut_list[-1]+8, cut_list[-1]+8])
        cut_list.append(x0[-1]+1)

    cut_list_y = [y0[0]]
    cut_list_y.append(y0[-1]+1)

    cut_imgs = []
    # 切割顺利的话应该是整对
    if len(cut_list) % 2 == 0:
        for i in range(len(cut_list) // 2):
            cut_img = img.crop([cut_list[i * 2], cut_list_y[0], cut_list[i * 2 + 1], cut_list_y[1]])
            cut_imgs.append(cut_img)
        return cut_imgs
    else:
        print('Vertical cut failed.')
        return

def hashing(img):
    """计算哈希值"""
    img = img.resize((8, 15), Image.LANCZOS)
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
    """识别结果"""
    img = binarize(img)
    chars = vertical_cut(img)

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
    for i in range(50):
        img = get_img(i+1)
        char_num = recognize(img)
        plt.subplot(5,10,i+1)
        plt.imshow(img)
        plt.title(char_num)
        plt.xticks([])
        plt.yticks([])
    plt.show()
    # img = get_img(206)
    # char_num = hashing(img)
    # print(char_num)