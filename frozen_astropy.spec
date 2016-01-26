# -*- mode: python -*-

block_cipher = None

import astropy
import os
base_dir = os.path.dirname(astropy.__file__)


a = Analysis(['frozen_astropy.py'],
             pathex=['/Users/users/breddels/src/frozen_astropy'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='frozen_astropy',
          debug=False,
          strip=None,
          upx=True,
          console=True )


data_tree = Tree(base_dir, prefix='astropy')
print("adding %s as directory astropy" % (base_dir))
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               data_tree,
               strip=None,
               upx=True,
               name='frozen_astropy')
