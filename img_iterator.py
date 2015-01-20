# Class to iterate all jpeg images present in the subfolder

import os

class ImageIterator:
	def __init__(self, root = '.'):
		self.root = root
		self.filelist = []
		for root, dirs, files in os.walk(root):
			for f in files:
				self.filelist.append(os.path.join(root, f))
		self.count = len(self.filelist)
		self.current = 0

	def __iter__(self):
		return self

	def next(self):
		if self.current >= self.count:
			raise StopIteration
		else:
			self.current += 1
			return self.filelist[self.current - 1]

