from PIL import Image

img = Image.open('smiling.jpg')
area = (857,241,3057,2081)
imgCropped = img.crop(area)
imgCropped.show()
#to save the rotated image
#imgCropped.save()
