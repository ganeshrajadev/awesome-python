import os,constants
import math
from collections import Counter

LOCATION=constants.DOWNLOAD_PATH
LIST_NUMBER_OF_FILES=25
FILE_SIZE=6250000 #Approx 50 MB

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


files=[val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(LOCATION)] for val in sublist]


files=list(filter(lambda x: os.stat(x).st_size >FILE_SIZE,files))
c = Counter()
for f in files:
    c[f]=os.stat(f).st_size

for item in (sorted(c.items(), key=lambda i: i[1], reverse=True)[:]):
    print(os.path.split(item[0])[1]," - ",convert_size(item[1]))