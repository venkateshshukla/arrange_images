# A small script to arrange the images in the present folders and subfolders as
# per their time of capture. This would help easing their uploading to google
# plus photos, making a clean ordered library along the way.

from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from img_iterator import ImageIterator

def get_exif_dict(name):
	exif = {}
	img = Image.open(name)
	info = img._getexif()
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		exif[decoded] = value
	return exif

def get_time_exif(name):
	exif = get_exif_dict(name)
	time = exif['DateTimeOriginal']
	return time

def get_timestamp_exif(name):
	time = get_time_exif(name)
	date = datetime.strptime(time, "%Y:%m:%d %H:%M:%S")
	return int(date.strftime('%s'))

img_iter = ImageIterator()
for img in img_iter:
	date = get_timestamp_exif(img)
	print date



