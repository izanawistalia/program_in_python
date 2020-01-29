from PIL import Image

img = Image.open('girls.jpg')

new_size = (400, 150)
img.thumbnail(new_size)
img.save('girls_resized.jpg')
