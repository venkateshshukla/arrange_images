# Test script for checking img_move module

from img_ops import img_copy

# Sample img present
sample_img = "sample_img.jpg"

# Null img
null_img = None

# Non existent img
ne_img = "nonexistent.jpg"

#Test counter
i = 0

# Test 1
i += 1
try:
	img_copy(sample_img)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

# Test 2
i += 1
try:
	img_copy(null_img)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

# Test 3
i += 1
try:
	img_copy(ne_img)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

