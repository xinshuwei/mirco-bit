from microbit import *
compass.calibrate()#校准指南针  让设备倾斜，使他最外面一圈为红点

while True:
    needle = ((15 - compass.heading()) // 30) % 12  #heading 返回0-360的角度（0为北边，顺时针）
    display.show(Image.ALL_CLOCKS[needle])#取12的余数 并以钟表的形式显示
    print("磁场强度"+compass.get_field_strength())#返回磁场强度
