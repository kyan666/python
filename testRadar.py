# encoding: utf8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimage
from PIL import Image
import sys

plt.rcParams['font.sans-serif'] = ['SimHei']

name = ['Chinese','Math','English','Physical','Chemical']   #标签
theta = np.linspace(0,2*np.pi,len(name),endpoint=False)    #将圆根据标签的个数等比分
value = np.random.randint(50,100,size=5)   #在60-120内，随机取5个数
theta = np.concatenate((theta,[theta[0]]))  #闭合
value = np.concatenate((value,[value[0]]))  #闭合

ax = plt.subplot(111,projection = 'polar')      #构建图例
ax.plot(theta,value,'m-',lw=1,alpha = 0.75)    #绘图
ax.fill(theta,value,'m',alpha = 0.75)           #填充
ax.set_thetagrids(theta*180/np.pi,name)         #替换标签
ax.set_ylim(0,110)                          #设置极轴的区间
ax.set_theta_zero_location('N')         #设置极轴方向
ax.set_title('Radar',fontsize = 20)   #添加图描述
#plt.show()

plt.savefig("radar.png")

im = Image.open('radar.png','r')
print(im)

im2 = mpimage.imread('radar.png')
print(type(im2))
print(bytes(im2))

# import io
# im3 = io.BinaryIO