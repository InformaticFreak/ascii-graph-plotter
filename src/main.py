from math import e, pi, sin, cos, tan, asin, acos, atan, log, sqrt, degrees, radians
from numpy import sign
import pyperclip as pc
import re, sys

#-----------------------------------------------------------------------------------------#

__project__ = "ascii-graph-plotter"
__version__ = "2021.1"
__author__ = "InformaticFreak"
__description__ = "Plots the graph of a function with ASCII characters."

#-----------------------------------------------------------------------------------------#

# Weitere mathematische Funktionen
cot = lambda x: cos(x) / sin(x)
acot = lambda x: atan(1/x) if x > 0 else atan(1/x) + pi

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

# Anstieg am Punkt xy berechnen & passendes Zeichen zuordnen: █▓▒░
def draw(xy0, xy1, high_precision=True, ascii=False):
	if xy0 == (-1, -1) or xy1 == (-1, -1): return " "
	
	x0, y0 = xy0
	x1, y1 = xy1
	dx, dy = (x1 - x0), (y1 - y0)
	
	if high_precision:
		m = degrees(atan(dy / dx)) if dx != 0 else degrees(atan(dy / (dx + 1e-10)))
		if -90 <= m <= -60: char = "|"
		elif -60 <= m <= -30: char = "/"
		elif -30 <= m <= 30: char = "-"
		elif 30 <= m <= 60: char = "\\"
		elif 60 <= m <= 90: char = "|"
	
	else:
		char = "#" if ascii else "█"
	
	return char

#-----------------------------------------------------------------------------------------#

# main.py [function: str] [scale: float,float] [origin: int,int] [size: int,int] [discontinuous: bool] [precision: bool] [ascii: bool]

# Feldgröße definieren, Nullpunkt position setzen & Präzission festlegen
schemes = [r"\d+,\d+", r"_,\d+", r"_,_", r"\d+,_", r"(((\d+)?\.\d+)|(\d+\.?)),(((\d+)?\.\d+)|(\d+\.?))", r"_,(((\d+)?\.\d+)|(\d+\.?))", r"_,_", r"(((\d+)?\.\d+)|(\d+\.?)),_", r"1|(T|t)rue", r"_|0|(F|f)alse"]

# Skalierung
scale_default = (0.1, 10)
scale = scale_default
try:
	if   re.search(schemes[4], sys.argv[2]): scale = (float(sys.argv[2].split(",")[0]), float(sys.argv[2].split(",")[1]))
	elif re.search(schemes[5], sys.argv[2]): scale = (scale_default[0], float(sys.argv[2].split(",")[1]))
	elif re.search(schemes[6], sys.argv[2]): scale = scale_default
	elif re.search(schemes[7], sys.argv[2]): scale = (float(sys.argv[2].split(",")[0]), scale_default[1])
except: scale = scale_default

# Feldgröße
size_default = (81, 41)
size = size_default
try:
	if re.search(schemes[0], sys.argv[4]): size = (int(sys.argv[4].split(",")[0]), int(sys.argv[4].split(",")[1]))
	elif re.search(schemes[1], sys.argv[4]): size = (size_default[0], int(sys.argv[4].split(",")[1]))
	elif re.search(schemes[2], sys.argv[4]): size = size_default
	elif re.search(schemes[3], sys.argv[4]): size = (int(sys.argv[4].split(",")[0]), size_default[1])
except: size = size_default

# Nullpunkt
origin_default = (int((size[0] - 1) / 2), int((size[1] - 1) / 2))
origin = origin_default
try:
	if re.search(schemes[0], sys.argv[3]): origin = (int(sys.argv[3].split(",")[0]), int(sys.argv[3].split(",")[1]))
	elif re.search(schemes[1], sys.argv[3]): origin = (origin_default[0], int(sys.argv[3].split(",")[1]))
	elif re.search(schemes[2], sys.argv[3]): origin = origin_default
	elif re.search(schemes[3], sys.argv[3]): origin = (int(sys.argv[3].split(",")[0]), origin_default[1])
except: origin = origin_default

# Unstetige Darstellung
discontinuous_default = False
discontinuous = discontinuous_default
try:
	if re.search(schemes[4], sys.argv[5]): discontinuous = True
	elif re.search(schemes[5], sys.argv[5]): discontinuous = discontinuous_default
except: discontinuous = discontinuous_default

# Präzision
precise_default = False
precise = precise_default
try:
	if re.search(schemes[8], sys.argv[6]): precise = True
	elif re.search(schemes[9], sys.argv[6]): precise = precise_default
except: precise = precise_default

# ASCII Darstellung
ascii_default = False
ascii = ascii_default
try:
	if re.search(schemes[8], sys.argv[7]): ascii = True
	elif re.search(schemes[9], sys.argv[7]): ascii = ascii_default
except: ascii = ascii_default

#-----------------------------------------------------------------------------------------#

# Feld initialisieren
grid = [ [ None for x in range(size[0]) ] for y in range(size[1]) ]

# Achsen in Feld markieren
chars = "-|++A>+" if ascii else "─│┬┤▲▸┼"
for y in range(size[1]):
	grid[y][origin[0]] = chars[3] if y % 5 == 0 else chars[1]
grid[0][origin[0]] = chars[4]

for x in range(size[0]):
	grid[origin[1]][x] = chars[2] if x % 5 == 0 else chars[0]
grid[origin[1]][size[0]-1] = chars[5]

grid[origin[1]][origin[0]] = chars[6]	

# Alle Funktionen definieren
f = eval(f"lambda x: {sys.argv[1][5:] if sys.argv[1].startswith('f(x)=') else sys.argv[1]}")

# Funktionswerte ausrechnen und Position durch Nullpunkt Verschiebung ermitteln
xy = []
for x in range(size[0]):
	try: y = (-1) * round((f((x - origin[0]) * scale[0]) * scale[1]) - origin[1])
	except: y = -1
	if 0 < y < size[1]: xy.append((x, y))
	else: xy.append((-1, -1))

# Funktion approximieren (nicht unstetige Darstellung)
if not discontinuous:
	for i, c in enumerate(xy[:-1]): xy.extend(line(c, xy[i+1]))

# Funktion mit Anstieg in Feld markieren
for i, c in enumerate(xy[:-1]): grid[c[1]][c[0]] = draw(c, xy[i+1], precise, ascii)

# Feld in string konvertieren
output = [f"\nf(x)={sys.argv[1]} {scale[0]},{scale[1]} {origin[0]},{origin[1]} {size[0]},{size[1]} {'1' if discontinuous else '0'} {'1' if precise else '0'} {'1' if ascii else '0'}\n\n"]
for y in grid:
	for x in y:
		if x == None: output.append(" ")
		else: output.append(str(x))
	output.append("\n")
output_str = "".join(output)

# Feld plotten & in Zwischenablage kopieren
print(output_str)
pc.copy(output_str)
