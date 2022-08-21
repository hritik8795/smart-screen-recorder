from datetime import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from  win32api import GetSystemMetrics

width =GetSystemMetrics(0)
heigth =GetSystemMetrics(1)
#print(width,heigth)
time_stamp =datetime.now().strftime('%y-%m-%d-%H-%M-%S')
file_name =f'{time_stamp}.mp4'
fourcc =cv2.VideoWriter_fourcc('m','p','4','v')
captured_video =cv2.VideoWriter(file_name,fourcc,20.0,(width,heigth))

#abhi hum start karenge web cam ka code
webcam =cv2.VideoCapture(0)
#------------------------------------------------webcam end---
while True:
    img =ImageGrab.grab(bbox=(0,0,width,heigth))
    img_np =np.array(img)
    #yahan tak ke code me color differrencr dikha raha tha to abh use fix karte hai 
    img_final =cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #neeche ki line webcam ke frame ko read karne ke liye likha gay hai
    _, frame =webcam.read()
    fr_height,fr_width,_ =frame.shape
    img_final[0:fr_height,0:fr_width,:] =frame[0: fr_height,0:fr_width,:]
    #-------------------------------
    cv2.imshow('secret Capture', img_final)

    #cv2.imshow('webcam',frame)
    captured_video.write(img_final)
    if cv2.waitKey(10)==ord('q'):
        break
