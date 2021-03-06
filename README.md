```python
# Drive NeoPixels on the NeoPixels Block on Crickit FeatherWing based on input from AMG8833
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
current_pixel = NeoPixel(crickit.seesaw, 20,  num_pixels, brightness=0.05)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
ORANGE = (255, 125, 0)

#  Make pixels purple at startup
current_pixel.fill(PURPLE)
current_pixel.show()

#  Create one continuous servo on crickit servo port #1
left_wheel = crickit.dc_motor_1

#  Create one continuous servo on crickit servo port #2
right_wheel = crickit.dc_motor_2

#  Main loop for driving the robot
while True:

    #  Grabs the 2d array for the upcoming loop
	holder_2d_array = amg.pixels
	a = 0

    #  loops through the x and then the y of holder_2d_array
    #  think of it like a pandas dataframe where you iterate through rows and columns
	for x in range(0, 8):
		for y in range(0, 8):
			
            #  Set the pixel colors based on temperature received
			if holder_2d_array[x][y] < 18:
				current_pixel[a] = BLUE
			elif holder_2d_array[x][y] >= 18 and holder_2d_array[x][y] < 22:
				current_pixel[a] = CYAN
			elif holder_2d_array[x][y] >= 22 and holder_2d_array[x][y] < 24:
				current_pixel[a] = GREEN
			elif holder_2d_array[x][y] >= 24 and holder_2d_array[x][y] < 26:
				current_pixel[a] = YELLOW
			elif holder_2d_array[x][y] >= 26 and holder_2d_array[x][y] < 28:
				current_pixel[a] = ORANGE
			elif holder_2d_array[x][y] >= 28:
				current_pixel[a] = RED
				
                # determine if we should go left, right, or forward
				go_left = (a / 17)				
				go_right = (a / 52)
				go_forward = (a / 30)

				#  Turn left
				if go_left == 1:
					print("left")					
					print(a)
					print(go_left)
					left_wheel.throttle = 0.5
    					right_wheel.throttle = 0.5 
    					time.sleep(0.1)  # move for 0.1 seconds...
    					left_wheel.throttle = 0
    					right_wheel.throttle = 0

				# Turn right				
				elif go_right == 1:
					print("right")					
					print(a)
					print(go_right)
					left_wheel.throttle = -0.5
    					right_wheel.throttle = -0.5 
    					time.sleep(.1)  # move for 0.1 seconds...
    					left_wheel.throttle = 0
    					right_wheel.throttle = 0
    					time.sleep(.01)
				
				#  Go forward
				elif go_forward == 1:
					print("forward")					
					print(a)
					print(go_forward)
					left_wheel.throttle = 0.5
    					right_wheel.throttle = -0.5 
    					time.sleep(.1)  # move for 0.1 seconds...
    					left_wheel.throttle = 0
    					right_wheel.throttle = 0
    					time.sleep(.01)
            
            #  Move on to the next loop
			a += 1
	
```
## heat_tracking_robot

Components:
* Feather M0 Express
* AMG8833 featherwing
* 8x8 Neopixel Matrix
* 5V 2A AC power supply (for now)


![Screenshot](https://github.com/jeffreycoen/heat_tracking_robot/blob/master/thumbs_up.png "thumbs_up")
