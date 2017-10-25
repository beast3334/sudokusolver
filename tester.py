from PIL import Image

size = 300,300

outfile = "output.png"

try:
    im = Image.open("my_screenshot.png")
    im.thumbnail(size,Image.ANTIALIAS)
    im.save(outfile,"PNG")
except IOError:
    print ("Can't do what you want.")
