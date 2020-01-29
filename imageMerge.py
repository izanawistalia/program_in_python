
img1 = Image.open('girls_resized.jpg')
img2 = Image.open('smiling_resized.jpg')

imgBlended = Image.blend(img1, img2, 0.7)
imgBlended.show()
