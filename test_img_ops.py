# Test script for checking img_move module

from img_ops import img_copy

# Sample img present
sample_img = "sample_img.jpg"

# Null img
null_img = None

# Non existent img
ne_img = "nonexistent.jpg"

# Non jpeg file
nj_file = "nonjpg"

# Sample destination file
dest_img = "sample_destn.jpg"

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

# Test 4
i += 1
try:
	img_copy(nj_file)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

# Test 5
i += 1
try:
	img_copy(sample_img, dest_img)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

# Test 6
i += 1
try:
	img_copy(sample_img, null_img)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

# Test 7
i += 1
try:
	img_copy(sample_img, ne_img)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

# Test 8
i += 1
try:
	img_copy(sample_img, nj_file)
except AssertionError as e:
	print "Test %d raised assertion." % i,
	print e
	pass

