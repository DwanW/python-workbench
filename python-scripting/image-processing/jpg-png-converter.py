import sys
import os
from PIL import Image

#grab first n second arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if new folder exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop though folder
#convert img to png
# save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{output_folder}{clean_name[0]}.png', 'png')

#python jpg-png-converter.py example-img/ new/