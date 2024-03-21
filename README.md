# mitScratchColors

Convert colors in hex format into MIT Scratch's (modified HSV format) Color and Brightness.

Pre-requisites: install https://pypi.org/project/colorutils/

Usage:
python hex2hsv <input file> 

Where input file is a text file with a list of one or more colors in hex format, one per line.

Color in hex format example: #00FF00

output: #00FF00 67 0
Where
67: MIT Scratch color effect (from 0 to 200)
0: MIT Scratch's brightness effect (from -100 to 100)
