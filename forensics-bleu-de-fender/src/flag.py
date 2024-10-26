import sys
import os
from PIL import Image, ImageDraw, ImageFont

text = sys.argv[1]
output_dir = sys.argv[2]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(len(text)):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/firacode/FiraCode-Bold.ttf", size=250)
    draw.text((80,0), text=text[i], fill=(0, 0, 0), font=font)
    img.save(output_dir + "/" + str(i) + ".png")
