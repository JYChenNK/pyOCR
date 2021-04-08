
###
# 本示例用于从截图中提取有效数字
###

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import json

threshold = 150

def get_img(index):
    img = Image.open("E:\\Python\\PyCosmed\\v3.0\DIGIT2\\"+str(index)+".png")
    plt.subplot(221)
    plt.imshow(img)
    return img

# 分析灰度直方图，从而选择合适的二值化阈值
def gray_hist(img):
    img_arr = np.array(img.convert('L'))    #  convert - 转换图像格式   L - 八位黑白像素
                                            #  array - image格式转为array数组
    plt.subplot(223)
    plt.imshow(img_arr)

    img_arr = img_arr.flatten()             #  flatten - 转化为一维数组
    plt.subplot(222)
    plt.hist(img_arr,bins=256)              #  hist - 绘制直方图  bins - 条形数
    plt.ylim((0,50))

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
    plt.subplot(222)
    plt.imshow(bin_img)
    return bin_img

def vertical_cut(img):
    """纵向切割"""
    _, height = img.size
    print(height)
    
    px = list(np.sum(np.array(img) == 0, axis=0))
    py = list(np.sum(np.array(img) == 0, axis=1))

    # plt.subplot(223)
    # plt.plot(px)
    
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
            plt.subplot(2,6,i+7)
            plt.imshow(cut_img)
        return cut_imgs
    else:
        print('Vertical cut failed.')
        return
# if __name__ == '__main__':
#     img = get_img(17)
#     # gray_hist(img)
#     bin_img = binarize(img)
#     chars_img = vertical_cut(bin_img)
#     for imgs in chars_img:
#     #     imgs.save('E:\\Python\\PyCosmed\\v3.0\chars\\'+str(char_index)+'.png','png')
#     #     char_index += 1
#         print(imgs.size)
#     plt.show()

# if __name__ == '__main__':
#     char_index = 145
#     for img_index in range(75):
#         # if (img_index+1) % 3 == 0:
#         #     continue
#         img = get_img(img_index+1)
#         # gray_hist(img)
#         bin_img = binarize(img)
#         chars_img = vertical_cut(bin_img)
#         for char in chars_img:
#             char = char.resize((8, 15), Image.LANCZOS)
#             char.save('E:\\Python\\PyCosmed\\v3.0\chars\\'+str(char_index)+'.png','png')
#             char_index += 1
#         # print(chars_img[i].size)
#         # plt.show()

# if __name__ == '__main__':
#     for img_index in range(10):
#         img = Image.open("E:\\Python\\PyCosmed\\v3.0\chars\\"+str(img_index+1)+".png")
#         img = img.resize((8, 15), Image.LANCZOS)
#         img.save('E:\\Python\\PyCosmed\\v3.0\chars\\'+str(img_index+1)+'.png','png')

