import sys
import colorutils

try:
    args = sys.argv[1:]
except:
    print ("unknown error")
    sys.exit(2)
for arg in args:  
    inputfile = arg
try:
    with open(inputfile) as f:
        content = f.readlines()
except:
    print('File could not be opened.')
    sys.exit(3)

content = [line.strip() for line in content]
for hexColor in content:
    if (hexColor!=""):
        hsvColor = colorutils.hex_to_hsv(hexColor.replace('#',''))
        mitScratchColor = round(hsvColor[0]*200/360)
        mitScratchSatur = round(100*(1-hsvColor[1])) - round(100*(1-hsvColor[2]))
        print(str(hexColor) + ' ' + str(mitScratchColor) + ' ' + str(mitScratchSatur)) 


