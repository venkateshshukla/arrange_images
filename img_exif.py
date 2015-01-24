# Extract the timestamp from jpeg images using the exif data present in them

from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_exif_dict(name):
	''' Gives back a dictionary of exif name-values of image
	:param name: path of the jpeg file
	'''
	exif = {}
	img = Image.open(name)
	info = img._getexif()
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		exif[decoded] = value
	return exif

def get_time(name):
	''' Gives back the original time associated with image
	:param name: path of the jpeg file
	'''
	exif = get_exif_dict(name)
	if 'DateTimeOriginal' not in exif.keys():
		return None
	time = exif['DateTimeOriginal']
	return time

def get_timestamp(name):
	''' Gives back the timestamp of the image
	:param name: path of the jpeg file
	'''
	time = get_time(name)
	if time is None:
		return None
	date = datetime.strptime(time, "%Y:%m:%d %H:%M:%S")
	return int(date.strftime('%s'))

def get_unique_name(name):
	'''
	Gives back unique name depending upon date and time and timestamp.
	This name would also give useful information to user regarding date and
	time of taking image and would help sorting the images in right order.
	:param name: path of the jpeg file
	'''
	time = get_time(name)
	date = datetime.strptime(time, "%Y:%m:%d %H:%M:%S")
	ts6 = date.strftime("%s")[4:]
	dt = date.strftime("%Y_%m_%d_")
	flname = dt + ts6
	return flname

