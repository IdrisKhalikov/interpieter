from ProgramSource import ProgramSource
from PIL import Image

def get_program(source, codel_size):
    with Image.open(source) as im:
        converted = im.convert("RGB")
    pixels = converted.load()
    width, height = im.size
    image_rgb = []
    x = 0
    y = 0
    while y < height:
        image_rgb.append([])
        while x < width:
            r,g,b = pixels[x,y]
            color = (((r << 8) | g) << 8) | b 
            image_rgb[-1].append(color)
            x += codel_size
        x = 0
        y += codel_size
    converted.close()
    return ProgramSource(image_rgb)