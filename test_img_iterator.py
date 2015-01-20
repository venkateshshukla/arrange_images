# Test script to check if class Image Iterator is working or not

from img_iterator import ImageIterator

img_iter = ImageIterator('.')

for img in img_iter:
	print img
