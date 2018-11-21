import datetime
import time
import picamera
import RPi.GPIO as gpio


t = datetime.datetime.now()
led = 18
door = 4

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(led,gpio.OUT)
gpio.setup(door,gpio.IN,pull_up_down=gpio.PUD_UP)
                                                                                                                                                              
output = ""

def take_picture():
    global output
    output = t.strftime("%m-%d-%Y %H:%M:%S")+'.png'
    with picamera.PiCamera() as camera:
        camera.hflip = True
        camera.capture(output)

def unauth_picture():
    global output
    output = "/home/pi/Desktop/UnauthorizedAccess/"+t.strftime("%m-%d-%Y %H:%M:%S")+'.png'
    with picamera.PiCamera() as camera:
        camera.hflip = True
        camera.capture(output)
        

def blink(led):
    gpio.output(led,True)
    time.sleep(1)
    gpio.output(led,False)
    time.sleep(1)
    return

#def cardswipe():
#    while True:
#        card = input()
#        f.write("Harvard ID Number: " + card[1:17] + " Time: " + t.strftime("%m-%d-%Y %H:%M:%S"))
#        f.write('\n')
        #f.write(';')
#        f.close()
#        take_picture()
#        time.sleep(1)
        #return

#gpio.cleanup()

#while True:
#    cardswipe()

while True:
    if gpio.input(door):
        time.sleep(1)
        unauth_picture()
        f = open("Unauthorized Access Log"+'.txt','a')
        f.write("Storage Unit Box Opened : " + " Time: " + t.strftime("%m-%d-%Y %H:%M:%S"))
        f.write('\n')
        f.write(';')
        f.close()
        for i in range(0,5):
            blink(led)
            
gpio.cleanup()
