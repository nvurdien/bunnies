from PIL import Image
from subprocess import call

def resize(path):
    basewidth = 400
    try:
        img = Image.open(path)
    except:
        print("file is not an image, check the format")
        call(["file", path])
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(path)
