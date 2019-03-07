from microbit import *
import music

# x 左右
#y  前进后退
#z   上下
while True:
  music.pitch(accelerometer.get_y(), 10)#获取y值 并播放10ms
  reading = accelerometer.get_x()
  if reading > 20:
    display.show("R")
  elif reading < -20:
    display.show("L")
  else:
    display.show("-")
 
    

