from distutils.core import setup
import py2exe, sys, os
from glob import glob

sys.argv.append('py2exe')
sys.path.append("D:\Program Files\Microsoft Visual Studio 10.0\VC\redist\x86\Microsoft.VC100.CRT")

#data_files = [("Microsoft.VC100.CRT", glob(r'D:\Program Files\Microsoft Visual Studio 10.0\VC\redist\x86\Microsoft.VC100.CRT\*.*'))]

setup(
	options = {'py2exe':{'bundle_files':1}},
	windows = [{'script':'W7500_ISP.py'}],
	zipfile = None,
)

