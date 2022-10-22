import sys
from PIL import Image

image_list=[] #list of image paths
des_file_name=r"" # destination location

images = map(Image.open, image_list)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_image = Image.new('RGB', (total_width, max_height))
offset = 0
for im in image_list:
  i=Image.open(im)
  new_image.paste(i, (offset,0))
  offset += i.size[0]

new_image.save(des_file_name)