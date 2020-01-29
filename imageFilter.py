from PIL import Image, ImageFilter

img = Image.open('girls.jpg')
img.filter(ImageFilter.BoxBlur(5)).show()
img.filter(ImageFilter.CONTOUR).show()
'''similarly many more filters can be used'''

