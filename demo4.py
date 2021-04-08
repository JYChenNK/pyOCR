###
#   基于PCA的图像识别示例（数据集）
###

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def creatDataSet():
    TrainDataSet = np.array([[]])
    TestDataSet = np.array([[]])
    for i in range(300):
        img = Image.open("chars\\"+str(i+1)+".png")
        img_data = np.array(img).flatten()
        if i == 0:
            TrainDataSet = img_data
        else:
            TrainDataSet = np.row_stack((TrainDataSet,img_data))
    for i in range(100):
        img = Image.open("chars\\"+str(i+301)+".png")
        img_data = np.array(img).flatten()
        if i == 0:
            TestDataSet = img_data
        else:
            TestDataSet = np.row_stack((TestDataSet,img_data))
    np.savez('data.npz',train=TrainDataSet,test=TestDataSet)
    return TrainDataSet,TestDataSet

def loadDataSet():
    data=np.load('data.npz')
    label=np.load('label.npz')
    TrainDataSet = data['train']
    TestDataSet = data['test']
    TrainLabel = label['train']
    TestLabel = label['test']
    return TrainDataSet,TrainLabel,TestDataSet,TestLabel

if __name__ == '__main__':
    TrainDataSet,TrainLabel,TestDataSet,TestLabel = loadDataSet()
    pca = PCA(3)
    compress_data = pca.fit_transform(TrainDataSet)
    compress_data = compress_data + np.random.randn(300,3)/10
    index_1,index_2 = 0,2

    for i in [1,4,12,0,8,7,2,10,42,13,145]:
        if TrainLabel[i] == '0':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='black')
        elif TrainLabel[i] == '1':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='gray')
        elif TrainLabel[i] == '2':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='brown')
        elif TrainLabel[i] == '3':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='orange')
        elif TrainLabel[i] == '4':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='olive')
        elif TrainLabel[i] == '5':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='green')
        elif TrainLabel[i] == '6':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='cyan')
        elif TrainLabel[i] == '7':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='blue')
        elif TrainLabel[i] == '8':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='purple')
        elif TrainLabel[i] == '9':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='pink')
        elif TrainLabel[i] == '.':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='red')


    for i in range(300):
        if TrainLabel[i] == '0':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='black')
        elif TrainLabel[i] == '1':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='gray')
        elif TrainLabel[i] == '2':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='brown')
        elif TrainLabel[i] == '3':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='orange')
        elif TrainLabel[i] == '4':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='olive')
        elif TrainLabel[i] == '5':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='green')
        elif TrainLabel[i] == '6':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='cyan')
        elif TrainLabel[i] == '7':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='blue')
        elif TrainLabel[i] == '8':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='purple')
        elif TrainLabel[i] == '9':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='pink')
        elif TrainLabel[i] == '.':
            plt.scatter(compress_data[i][index_1],compress_data[i][index_2],c='red')


    plt.legend(['0','1','2','3','4','5','6','7','8','9','.'],loc="center right")
    plt.xlabel('First Principal Component')
    plt.ylabel('Sencond Principal Component')
    plt.show()

    # pca = PCA(n_components=2)
    # pca.fit(trainSet)