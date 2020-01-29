from PIL import Image

img = Image.open('smiling.jpg')
img.convert('L').show()
