from math import e, pi, sin, cos, tan, asin, acos, atan, log, sqrt, degrees, radians
from numpy import sign
import pyperclip as pc
import re, sys

# Plot-Class
class Plot:
	def __init__(self, size, origin):
		self.size = size
		self.origin = origin
		self.grid = [ [ None for x in range(self.size[0]) ] for y in range(self.size[1]) ]
	
	# Draw function points
	def draw(self):
		pass
	
	# Print full plot
	def show(self):
		pass



# DDA (Draw Line Algorithm)
def line(xy0, xy1):
	if xy0 == (-1, -1) or xy1 == (-1, -1): return []
	
	lp = []
	dx, dy = xy1[0] - xy0[0], xy1[1] - xy0[1]
	steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
	xi, yi = dx / steps, dy / steps
	x, y = xy0[0], xy0[1]
	
	for j in range(steps):
		lp.append((round(x), round(y)))
		x += xi
		y += yi
	
	return lp

f = eval(f"lambda x: {x}")
