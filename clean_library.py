# A small script to arrange the images in the present folders and subfolders as
# per their time of capture. This would help easing their uploading to google
# plus photos, making a clean ordered library along the way.

from img_exif import get_timestamp
from img_iterator import ImageIterator

img_iter = ImageIterator()
for img in img_iter:
	date = get_timestamp(img)
	print date



