# frozen_astropy
Test project for testing out astropy in a frozen environment (pyinstaller/py2app/py2exe)
# build using PyInstaller (linux)
Make sure you have PyInstaller installed (`pip install --user pyinstaller`)
* run `$ pyinstaller -y frozen_astropy.spec`

# testing frozen_astropy
* simply test importing: `$ python frozen_astropy.py`
* run all unittests: `$ python frozen_astropy.py test`
* enter debugger: `$ python frozen_astropy.py debug`
