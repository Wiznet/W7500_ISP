# Install wxpython
## Ubuntu Environment
$ sudo apt-get install libgtk-3-dev build-essential checkinstall

$ sudo apt-get install python-wxtools

$ sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n

$ sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n libwxgtk2.8-dev libgtk2.0-dev


## Windows Environment
http://www.wxpython.org/download.php

# Install XMODEM Library
Download link : https://pypi.python.org/pypi/xmodem

## Ubuntu Environment
$ tar -xvf xmodem-0.4.1.tar.gz

$ sudo cp -rf  ~/xmodem-0.4.1/xmodem /usr/lib/python2.7/dist-packages/

## Windows environment
After unzip download file, copy xmodem directory to
Python2.7/Lib/site-packages/


# How to make exe file for windows environment
Download link(py2exe) : http://www.py2exe.org/

$ python setup_20150820_Lucid.py py2exe

# How to run
## Ubuntu Environment

$ python W7500_ISP_20150820_Lucid.py

## Windows Environment
## Method 1 : Using Python

$ python W7500_ISP_20150820_Lucid.py

## Method 2 : Making EXE binary
Download and install py2exe : http://www.py2exe.org/

$ python setup_20150820_Lucid.py py2exe


