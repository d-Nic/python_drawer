import pyautogui
import time
import math
from PIL import Image
import sys

import drawer
import directionTravel


# create a point travel class to extract points to draw
# create a drawer class to draw the points 

def main():
	args = sys.argv
	if len(args) != 3:
		print("Usage: ./main.py <file_to_draw> <luminance_thresh (0-255)>")
		return
	
	file = sys.argv[1]
	luminanceThresh = int(sys.argv[2])
	strokeDuration = 1
	
	pointMethod = directionTravel.PointTravel(luminanceThresh)
	points = pointMethod.getPoints(file)
	
	artist = drawer.Drawer(1)
	artist.drawPoints(points)
	
	
if __name__ == "__main__":
	main()