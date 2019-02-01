import math
format = "P3"
col = "501"
row = "501"
max = "255"
f = open("picm.ppm","w")

def writeHeading(file):
    f.write(format + " " + col + " " + row + " " + max + "\t")

def findCenter(r,c):
    return (r-1)/2,(c-1)/2

def distance (x0,y0,x1,y1):
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) **2)

def draw(file):
    center = findCenter(int(row),int(col))
    sumCenter = center[0] + center[1]
    for r in range(int(row)):
        for c in range(int(col)):
            radiusSq = 200 ** 2
            circleForm = ((r - center[0]) ** 2 + (c -center[1]) ** 2)
            thicknessScaler = 8000
            red = 0
            green = 0
            blue = 0
            if (circleForm >= radiusSq - thicknessScaler and circleForm <= radiusSq + thicknessScaler):
                scaler = (distance(r,c,center[0],center[1]) / 200) ** 8
                green = int(200 * scaler ** 2)
                blue = int(255 * scaler)
            if (distance(r,c,center[0],center[1]) > 218):
                scaler = (distance(r,c,center[0],center[1]))/300
                blue = int(50 * scaler)
            if (distance(r,c,center[0],center[1]) < 180):
                scaler = (distance(r,c,center[0],center[1]))/300
                green = int(46 * scaler)
                blue = int(135 * scaler)
            f.write(str(red) + " " + str(green) + " " + str(blue) + " ")

writeHeading(f)
draw(f)
