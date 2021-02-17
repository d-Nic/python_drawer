import pyautogui
import time
import math
from PIL import Image
import sys

# class that handles the actual drawing process
class Drawer:
	
	strokeDuration = 1
	
	def __init__(self, sDuration):
		self.strokeDuration = sDuration
	
	def drawPoints(self, points):
		print("Drawing will start in 5 seconds ... tab into your canvas")
		print("Drag mouse to top-left corner to cancel drawing")
		
		time.sleep(5)
		
		for i in points:
			print("**Drawing", i)
			
			# these offsets are for a specific monitor, need to add config file to specify draw range to squeeze points into
			pyautogui.moveTo(i[0][1] + 210, i[0][0] + 210, duration=self.strokeDuration)
			pyautogui.dragTo(i[1][1] + 210, i[1][0] + 210, duration=self.strokeDuration)
		
		print("Drawing complete")