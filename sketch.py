# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:13:05 2021

@author: asus
"""
from PIL import Image
import numpy as np
import cv2 


def Sketch():
    input_image = input('原圖:')
    output_name =input('素描檔名:')
    img = cv2.imread(input_image) 
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, ksize=(81,81),sigmaX=0, sigmaY=0)#81,81
    img_out = cv2.divide(img_gray, img_blur, scale=255)
    
    cv2.imwrite(output_name, img_out)
    '''
    cv2.imshow('input_image', img)
    cv2.imshow('output_image', img_out)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    '''
    
def Sketch2():
    input_image = input('原檔路徑:')
    output_name = input('存檔:')
    try:
   
        a = np.asarray(Image.open(input_image)
                       .convert('L')).astype('float')#將影象轉化為灰度圖
        depth = 10.  # 浮點數，預設深度值為10
        grad = np.gradient(a)  # 取影象灰度的梯度值
        grad_x, grad_y = grad  # 分別取橫縱影象的梯度值
        grad_x = grad_x * depth / 100.  # 根據深度調整 x 和 y 方向的梯度值
        grad_y = grad_y * depth / 100.
        A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)  # 構造x和y軸梯度的三維歸一化單位座標系
        uni_x = grad_x / A
        uni_y = grad_y / A
        uni_z = 1. / A
    
        vec_el = np.pi / 2.2  # 光源的俯視角度，弧度值
        vec_az = np.pi / 4.  # 光源的方位角度，弧度值
        dx = np.cos(vec_el) * np.cos(vec_az)  # 光源對 x 軸的影響，np.cos(vec_el)為單位光線在地平面上的投影長度
        dy = np.cos(vec_el) * np.sin(vec_az)  # 光源對 y 軸的影響
        dz = np.sin(vec_el)  # 光源對 z 軸的影響

        b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 梯度與光源相互作用，將梯度轉化為灰度
        b = b.clip(0, 255)  # 為避免資料越界，將生成的灰度值裁剪至0‐255區間
        im = Image.fromarray(b.astype('uint8'))  # 重構影象
        im.show()
        im.save(output_name)
    
    except(OSError, NameError):
        print('OSError',OSError)
        
 


      

    

if __name__ == '__main__':
    act = input('指令:')
    if act =="1":
        Sketch()
    if act == "2":
        Sketch2()
  