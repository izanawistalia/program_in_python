from PIL import Image


size = height,width = (300,300)
img = Image.new('RGB', size, 'blue')
img.show()
''' Image.new('there're different modes available', give any size, 'rgb(23,54,52)')

Image.new('any mode', size, 'rgb(20%,40%,40%)')

Image.new('any mode', size, 'hex value')
