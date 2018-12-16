# Drive NeoPixels on the NeoPixels Block on Crickit FeatherWing
import time
import busio
import board
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel
import adafruit_amg88xx

# Line necessary to not get the PA23 pin in use error
amg = adafruit_amg88xx.AMG88XX(crickit.seesaw.i2c_device.i2c)

num_pixels = 64  # Number of pixels driven from Crickit NeoPixel terminal

# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixelss = NeoPixel(crickit.seesaw, 20,  num_pixels, brightness=0.05)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
ORANGE = (255, 125, 0)

#for i in range(1, 3): 
pixelss.fill(PURPLE)
pixelss.show()
    #print(i)
    #time.sleep(1)

a = 0

# Create one continuous servo on crickit servo port #1
left_wheel = crickit.dc_motor_1
# Create one continuous servo on crickit servo port #2
right_wheel = crickit.dc_motor_2


holder = amg.pixels
#print(holder)

while True:
	holder = amg.pixels
	a = 0
	for x in range(0, 8):
		for y in range(0, 8):
			
	
			if holder[x][y] < 22:
				pixelss[a] = BLUE
			elif holder[x][y] >= 22 and holder[x][y] < 24:
				pixelss[a] = GREEN
			elif holder[x][y] >= 24 and holder[x][y] < 28:
				pixelss[a] = ORANGE
			elif holder[x][y] >= 28:
				pixelss[a] = RED
				print(a)
				test = (a / 17)				
				test_right = (a / 52)
				if test == 1:
					print("left")					
					print(a)
					print(test)
					left_wheel.throttle = 0.5
    					right_wheel.throttle = 0.5
 
    					time.sleep(.1)  # move for 2 seconds...
    					
    					# Then stop both wheels
    					left_wheel.throttle = 0
    					right_wheel.throttle = 0
 					#test == 1
    					#time.sleep(.1)
								
				elif test_right == 1:
					print("right")					
					print(a)
					print(test_right)
					left_wheel.throttle = -0.5
    					right_wheel.throttle = -0.5
 
    					time.sleep(.1)  # move for 2 seconds...
    					
    					# Then stop both wheels
    					left_wheel.throttle = 0
    					right_wheel.throttle = 0
 					#test == 1
    					time.sleep(.1)

			a += 1
	

