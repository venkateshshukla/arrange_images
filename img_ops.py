# Module to safely move a file from a folder to another
# The main aim is to not touch the original images and not to have any
# overwritten data.

import os
import shutil
from img_iterator import is_jpeg

def is_present(name, dest):
	'''
	Check if a file of given name (included as path) is present in the given
	directory
	:param name: name of the file (may contain whole path. last term is considered)
	:param dest: destination folder where check is to be performed.
	'''
	src_path, img_name = os.path.split(name)
	filename = os.path.join(dest, img_name)
	return os.path.isfile(filename)

def img_copy(src, dest = "out/", dupl = "out/duplicates/"):
	'''
	Copies img from src to dest putting duplicates in dupl.
	:param src: path to image file.
	:param dest: destination folder where the file should be put.
	:param dupl: folder where duplicates, if found, may be put.
	'''

	# Sanity checks
	assert src is not None, "src path cannot be None"
	assert dest is not None, "dest path cannot be None"
	assert dupl is not None, "dupl path cannot be None"
	assert os.path.isfile(src), "src is not present"
	assert is_jpeg(src), "src is not a jpeg"

	path = os.path.abspath(os.path.dirname(__file__))

	dest_dir = os.path.join(path, dest)
	dupl_dir = os.path.join(path, dupl)
	ddupl_dir = os.path.join(dupl_dir, 'duplicates')

	if not os.path.isdir(dest_dir):
		os.makedirs(dest_dir)
	if not os.path.isdir(dupl_dir):
		os.makedirs(dupl_dir)

	if is_present(src, dest_dir):
		img_copy(src, dest = dupl_dir, dupl = ddupl_dir)
	else:
		shutil.copy(src, dest_dir)

