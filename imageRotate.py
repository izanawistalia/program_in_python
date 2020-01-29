from PIL import Image

img = Image.open('smiling.jpg')
img.rotate(45).show()
