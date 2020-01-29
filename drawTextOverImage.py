from PIL import Image, ImageDraw, ImageFont

img = Image.open('smiling.jpg')
draw = ImageDraw.Draw(img)
points = (500,1000)
string = "humara NONU"
fonts = ImageFont.truetype("arial.ttf",200)
draw.text(points, string, "red", font=fonts)
img.show()
