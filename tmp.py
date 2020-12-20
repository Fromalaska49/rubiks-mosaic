from PIL import Image
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
for x in range(originalWidth):
    for y in range(originalHeight):
        print
        pixel = inputPixels[x, y]
        minDiff = maxDiff
        match = blue
        for color in colors:
            d = abs(pixel[r] - color[r]) + abs(pixel[g] - color[g]) + abs(pixel[b] - color[b])
            if d < minDiff:
                minDiff = d
                match = color
        outputPixels[x, y] = (match[r], match[g], match[b])
outputImage.show()