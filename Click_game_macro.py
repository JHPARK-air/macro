import pyautogui as pag
import time


for _ in range(15):
    for i in range(1021, 1316):
        for j in range(482,761):
           if i%73==0 and j%69==0: 
               pag.click(i,j)


#https://simplegame.tistory.com/120