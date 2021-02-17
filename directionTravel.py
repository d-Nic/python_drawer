import pyautogui
import time
import math
from PIL import Image
import sys

# A potential point classification method (inspired by image vectorisation)
class PointTravel:

	luminanceThresh = 0
	strideThresh = 1
	directionMap = {
		'Up': [0,strideThresh],
		'Down':[0,-strideThresh],
		'Left':[-strideThresh,0],
		'Right':[strideThresh,0],
		'TopL':[-strideThresh,strideThresh],
		'TopR':[strideThresh,strideThresh],
		'BotL':[-strideThresh,-strideThresh],
		'BotR':[strideThresh,-strideThresh]
	}
	
	def __init__(self, lumThresh):
		self.luminanceThresh = lumThresh
	
	# get brightness of a specific pixel (move this to seperate module?)
	def lumanise(self, pixel):
		if type(pixel) == int:
			return pixel
		# standard luminance formula
		return (0.2126*pixel[0] + 0.9512*pixel[1] + 0.0722*pixel[2])
	
	
	# start at x, y, travel in a direction until pixels weakens out, create vector 
	# if next vector in path is above luminosityThresh
	def travel(self, x, y, direction, width, height, pixels, drawnPixels):
		vecTravel = 0
		vecs = []
		travelVector = [[x,y], [x,y]]
		while True:
			# check if we are in the ranges of the next check 
			if (x + direction[0]) < height and (y + direction[1]) < width:
				if (x + direction[0]) >= 0 and (y + direction[1]) >= 0:
					luminosity = self.lumanise(pixels[y+direction[1], x+direction[0]])
					if luminosity < self.luminanceThresh:
						# build vector
						if (x*height + y) in drawnPixels:
							return [[x,y], [x,y]]
						vecTravel += 1
						x += direction[0]
						y += direction[1]
						travelVector[1][0] = x
						travelVector[1][1] = y
						drawnPixels[x*height + y] = True
					else:
						break
				else:
					break
			else:
				break
		return travelVector
		
	def getPoints(self, img):	
		imageVectors = []
		drawnPixels = {}
		fil = Image.open(img)
		fil.seek(0)
		pixels = fil.load()
		width, height = fil.size
		for x in range(width):
			print("Deriving points to draw = ", math.floor((x)/(width)*100), '%')
			pos = 0
			for y in range(height):
				if pos % 10 == 0:
					for val in self.directionMap:
						toAdd = self.travel(x, y, self.directionMap[val], width, height, pixels, drawnPixels)
						if toAdd[0] != toAdd[1]:
							imageVectors.append(toAdd)
				pos += 1
		
		return imageVectors
