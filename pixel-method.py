from PIL import Image
import statistics
import math
import time
blue = [0,0,255]
white = [255,255,255]
yellow = [255,255,0]
green = [0,128,0]
orange = [255,165,0]
red = [255,0,0]
r, g, b = 0, 1, 2
colors = (blue, white, yellow, green, orange, red)
colorCombinations = [] # should be a set
for cA in colors:
    for cB in colors:
        for cC in colors:
            for cD in colors:
                colorCombinations.append([int(statistics.mean([cA[r], cB[r], cC[r], cD[r]])), int(statistics.mean([cA[g], cB[g], cC[g], cD[g]])), int(statistics.mean([cA[b], cB[b], cC[b], cD[b]]))])
print('color combos generated')
image = Image.open("portraittest.jpg")
originalWidth, originalHeight = image.size
newWidth, newHeight = originalWidth, originalHeight
inputPixels = image.load()
outputImage = Image.new(mode = "RGB", size = (newWidth, newHeight))
outputPixels = outputImage.load()
maxDiff = 255 * 3
area = originalWidth * originalHeight
i = 0
startTime = time.time()
lastTime = time.time()
for x in range(originalWidth):
    for y in range(originalHeight):
        pixel = inputPixels[x, y]
        minDiff = maxDiff
        match = blue
        for color in colorCombinations:
            d = abs(pixel[r] - color[r]) + abs(pixel[g] - color[g]) + abs(pixel[b] - color[b])
            if d < minDiff:
                minDiff = d
                match = color
        outputPixels[x, y] = (match[r], match[g], match[b])
        i += 1
        t = time.time()
        if t > lastTime + 10:
            s = (t - startTime) / (i/area) * (1-i/area)
            print("{:.1%}".format(i/area) + ' done with ' + str(int(s)) + 's remaining')
            lastTime = t
outputImage.show()