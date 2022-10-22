dest_path=r""
file_path=r""
name=r""
from PIL import Image

from resizeimage import resizeimage


for x in [16,32,48,128]:
    with open(file_path, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [x, x])
            cover.save(dest_path+name+str(x)+'.jpg', image.format)
            im = Image.open(dest_path+name+str(x)+'.jpg')
            im.save(dest_path+name+str(x)+'.png')
