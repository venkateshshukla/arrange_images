# A small script to arrange the images in the present folders and subfolders as
# per their time of capture. This would help easing their uploading to google
# plus photos, making a clean ordered library along the way.

from img_exif import get_unique_name
from img_iterator import ImageIterator
from img_ops import img_copy

img_iter = ImageIterator()
for img in img_iter:
	uniq_name = get_timestamp(img)
	filename = uniq_name + '.jpg'
	img_copy(img, filename)

