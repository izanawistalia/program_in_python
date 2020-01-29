from PIL import Image

img = Image.open('smiling.jpg')
print(img.height)
print(img.width)
print(img.size)
print(img.format)
print(img.mode)

