# Module to safely move a file from a folder to another
# The main aim is to not touch the original images and not to have any
# overwritten data.

import os
import shutil
from img_iterator import is_jpeg

def get_filename(path):
	'''
	Give the filename of provided path to a file. Use python os.path.split
	:param path: path of the file whose name is to be returned
	'''
	src_path, fl_name = os.path.split(path)
	return fl_name

def is_present(name, dest):
	'''
	Check if a file of given name (included as path) is present in the given
	directory
	:param name: name of the file (may contain whole path. last term is considered)
	:param dest: destination folder where check is to be performed.
	'''
	img_name = get_filename(name)
	filename = os.path.join(dest, img_name)
	return os.path.isfile(filename)

def img_copy(src = None, dest = None, dest_path = "out/", dupl_path = "out/duplicates/"):
	'''
	Copies img from src to dest putting duplicates in dupl.
	All paths are relative to path of the file.
	:param src: path to image file.
	:param dest: name of the final image file without path. By default src.
	:param dest_path: destination folder where the file should be put.
	:param dupl_path: folder where duplicates, if found, may be put.
	'''

	# Sanity checks
	assert src is not None, "src path cannot be None"
	assert dest is not None, "dest name cannot be None"
	assert dest_path is not None, "dest path cannot be None"
	assert dupl_path is not None, "dupl path cannot be None"
	assert os.path.isfile(src), "src is not present"
	assert is_jpeg(src), "src is not a jpeg"
	assert is_jpeg(dest), "dest is not a jpeg"

	src_filename = get_filename(src)
	dest_filename = get_filename(dest)

	path = os.path.abspath(os.path.dirname(__file__))

	dest_dir = os.path.join(path, dest_path)
	dupl_dir = os.path.join(path, dupl_path)
	ddupl_dir = os.path.join(dupl_dir, 'duplicates')

	if not os.path.isdir(dest_dir):
		os.makedirs(dest_dir)
	if not os.path.isdir(dupl_dir):
		os.makedirs(dupl_dir)

	if is_present(src, dest_dir):
		img_copy(src, dest, dest_path = dupl_dir, dupl_path = ddupl_dir)
	else:
		final_path = os.path.join(dest_dir, dest_filename)
		shutil.copy(src, final_path)

