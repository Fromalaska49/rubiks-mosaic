from PIL import Image
import statistics
import math
import time
import random
blue = [0,0,255]
white = [255,255,255]
yellow = [255,255,0]
green = [0,128,0]
orange = [255,165,0]
red = [255,0,0]
r, g, b = 0, 1, 2
colors = (blue, white, yellow, green, orange, red)
image = Image.open("test.jpg")
originalWidth, originalHeight = image.size
newWidth, newHeight = originalWidth, originalHeight
inputPixels = image.load()
outputImage = Image.new(mode = "RGB", size = (newWidth, newHeight))
outputPixels = outputImage.load()
maxDiff = 255 * 3
area = originalWidth * originalHeight
monitor = 0
startTime = time.time()
lastTime = time.time()
for x in range(originalWidth):
    for y in range(originalHeight):
        pixel = inputPixels[x, y]
        minDiff = maxDiff
        match = blue
        colorDiffs = []
        colorDiffs.extend([maxDiff, maxDiff, maxDiff, maxDiff, maxDiff, maxDiff])
        colorDiffSquares = []
        colorDiffSquares.extend([maxDiff**2, maxDiff**2, maxDiff**2, maxDiff**2, maxDiff**2, maxDiff**2])
        #colorProbabilities[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        colorIndex = 0
        for color in colors:
            d = abs(pixel[r] - color[r]) + abs(pixel[g] - color[g]) + abs(pixel[b] - color[b])
            colorDiffs[colorIndex] = d
            colorDiffSquares[colorIndex] = d ** 4
            colorIndex += 1
        '''
        meanDiff = statistics.mean(colorDiffs)
        meanDiffSquare = meanDiff ** 2
        stdDev = stdev(colorDiffs)
        '''
        invSquares = []
        for val in colorDiffSquares:
            invSquares.append(1 / (val + 1))
        sumSquares = sum(invSquares)
        colorProbabilities = [0, 0, 0, 0, 0, 0]
        for i in range(6):
            colorProbabilities[i] = invSquares[i] / sumSquares
        for i in range(6):
            rand = random.uniform(0, 1)
            for color in range(6):
                rand -= colorProbabilities[color]
                if rand <= 0:
                    outputPixels[x, y] = (colors[color][r], colors[color][g], colors[color][b])
                    break
            if rand <= 0:
                break
        #outputPixels[x, y] = (match[r], match[g], match[b])
        monitor += 1
        t = time.time()
        if t > lastTime + 5:
            s = (t - startTime) / (monitor/area) * (1-monitor/area)
            print("{:.1%}".format(monitor/area) + ' done with ' + str(int(s)) + 's remaining')
            lastTime = t
outputImage.show()