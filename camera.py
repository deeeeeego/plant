from picamera import PiCamera
from time import sleep
from os import system

camera = PiCamera()

for i in range(5):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(1)
system('convert -delay 10 -loop 0 image*.jpg animation.gif')
print('done')
