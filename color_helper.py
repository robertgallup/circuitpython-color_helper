# A helper class for CircuitPython colors
class Color(object):

	# Standard colors
	BLACK = (0, 0, 0)
	GRAY = (128, 128, 128)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	YELLOW = (255, 150, 0)
	GREEN = (0, 255, 0)
	CYAN = (0, 255, 255)
	BLUE = (0, 0, 255)
	PURPLE = (180, 0, 255)
	AMBER = (255, 80, 0)

	# Calculate a color based on a position (0-255)
	# 0-255 is divided into 3 regions. In each region
	# R, G, and B are rising or falling between 0-255
	# The color range begins and ends on red to create
	# a smooth transition from 255 back to zero
	@staticmethod
	def rainbow (position):
		intensity = abs(position) % 256
		edge = intensity // 85
		intensity = 3 * (intensity % 85)
		if edge is 0: return (255 - intensity, intensity, 0)
		if edge is 1: return (0, 255 - intensity, intensity)
		return (color, 0, 255 - intensity)
	
	# Averages two color tuples
	@staticmethod
	def blend (a,b):
		return tuple(map(lambda x: sum(x)//2, zip(a, b)))
	
	# Multiples a color by a constant (used to adjust brightness)
	@staticmethod
	def scale (a, b):
	    return tuple(map((lambda x:max(min(round(x*b),255),0)),a))

	# Packs a color tuple into a big integer
	@staticmethod
	def pack (rgb):
		return rgb[0]*65536 + rgb[1]*256 + rgb[2]

	# Unpacks an integer color into a tuple
	@staticmethod
	def unpack (i):
		return ((i>>16) & 0xFF, (i>>8) & 0xFF, i & 0xFF)


