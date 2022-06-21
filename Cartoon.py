# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:25:59 2021

@author: asus
"""
import cv2

def cartoon():
    input_img =input('原圖:')
    output_name = input('輸出檔名:')
    num_down = 2   #缩减像素采样的数目
    num_bilateral = 7 #定义双边滤波的数目
    img_rgb = cv2.imread(input_img)  #读取图片
 #用高斯金字塔降低取样
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
 #重复使用小的双边滤波代替一个大的滤波
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7)
 #升采样图片到原始大小
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)
 #转换为灰度并且使其产生中等的模糊
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
 #检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur,255,
          cv2.ADAPTIVE_THRESH_MEAN_C,
          cv2.THRESH_BINARY,
          blockSize=9,
          C=2)
 #转换回彩色图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_color = cv2.resize(img_color,(2320,3060))# 放大图像
    img_edge = cv2.resize(img_edge, (2320, 3060)) # 放大图像
    #統一圖片大小
    img_cartoon = cv2.bitwise_and(img_color, img_edge)
    cv2.imwrite(output_name, img_cartoon)

    
   

if __name__ == '__main__':
    cartoon()        
    

