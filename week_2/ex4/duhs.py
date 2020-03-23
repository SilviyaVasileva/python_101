import os
import sys

def duhs(arg = '.'):
	size = 0
	stat = os.statvfs(arg)
	"""
	try:
		stat = os.statvfs(arg)
	except UnicodeEncodeError:
		if not PY3 isinstance(path, unicode):
			try:
				arg = path.encode(sys.getfilesystemencoding())
			except UnicodeEncodeError:
				pass
			stat = os.statvfs(arg)
		else:
			raise
	"""
	size = stat.f_blocks * stat.f_frsize - stat.f_bavail * stat.f_frsize
	return size

def main():
	s = duhs(sys.argv[1])
	print((s/1024))

if __name__ == '__main__':
	main()