__author__ = 'breddels'
print("frozen astropy")
import traceback
import inspect
import re
import sys
import os
import SimpleXMLRPCServer


if hasattr(sys, "_MEIPASS"): # we are frozen using PyInstaller
	# monkey patch inspect.getabsfile to play nicely with what PyInstaller assumes
	# Say our executable is in /foo/bar/myexecutable
	# But astropy was found in /usr/lib/python2.6/site-packages/astropy
	# inspect.getabsfile will return /usr/lib/python2.6/site-packages/astropy/__init__.pyc
	# and inspect.getmodule will not find that file in sys.modules, so we rewrite path
	# by replacing everything before astropy with sys._MEIPASS (which is /foo/bar/myexecutable)
	# in this example
	sys.path.insert(0, os.path.join(sys._MEIPASS, "astropy"))
	if 1:
		old_getabsfile = inspect.getabsfile
		def inspect_getabsfile_wrapper(*args, **kwargs):
			#return old_getabsfile(*args, **kwargs).replace("/Users/users/breddels/src/astropy", )
			path = old_getabsfile(*args, **kwargs)
			# replace everything before astropy with the sys._MEIPASS location
			# this is easier to do when the path is reversed
			last_part = re.sub("(.*?yportsa).*", r"\1", path[::-1])[::-1]
			return os.path.join(sys._MEIPASS, last_part)
		inspect.getabsfile = inspect_getabsfile_wrapper
try:
	import astropy
	import astropy.units
	import astropy.units.si
except:
	traceback.print_exc()
	import pdb
	pdb.set_trace()
if len(sys.argv) > 1:
	if sys.argv[1] == "test":
		astropy.test()
	if  sys.argv[1] == "debug":
		print("happy debugging!")
		import pdb
		pdb.set_trace()
print("frozen astropy works!")