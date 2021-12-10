import sys
import os
from PIL import Image

os.mkdir('.\new')
while True:
    img = Image.open('./Pokedex')
    img.save('png')

    break

image_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
print(image_folder, output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')
