# GpuTest
GPU stress test and OpenGL benchmark
Geeks3D GpuTest - GPU stress test and OpenGL benchmark.
Copyright (c) 2012-2014 Geeks3D, All rights reserved.

Homepage: http://www.Geeks3D.com/GpuTest/

***************************************************
THIS SOFTWARE IS PROVIDED 'AS-IS', WITHOUT ANY 
EXPRESS OR IMPLIED WARRANTY. IN NO EVENT WILL 
THE AUTHOR BE HELD LIABLE FOR ANY DAMAGES ARISING 
FROM THE USE OF THIS SOFTWARE.
***************************************************

GpuTest Linux 64-bit
--------------------
1 - Unzip the archive where you want. 

2 - Open a terminal in GpuTest folder.

3 - Launch a test by typing for example:
$ sh ./start_furmark_windowed_1024x640.sh
or 
$ sh ./start_tessmark_benchmark_fullscreen_1920x1080.sh



A GUI (graphical user interface made with Python / tkinter) is 
available since GpuTest 0.6.0+. To launch the GUI, run the following
command:

$ python gputest_gui.py  #for python2
or
$ python3 gputest_gui.py  #for python3


Under some Linux distributions, you might need to install the 
Tk package otherwise you will have:
-----------------------------------------------------------------------
Traceback (most recent call last):
  File "madshaders.py", line 4, in <module>
    import Tkinter as tk # gives tk namespace
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 42, in <module>
    raise ImportError, str(msg) + ', please install the python-tk package'
ImportError: No module named _tkinter, please install the python-tk package
-----------------------------------------------------------------------

To install the python-tk package, just enter in command line:

$ sudo apt-get install python-tk
or
$ sudo apt-get install python3-tk



GpuTest Linux, random notes
---------------------------

- If needed, you can change the permissions of GpuTest.exe to make it executable:
  $ chmod u+x GpuTest.exe

- GpuTest 0.7.0 for Linux has been compiled under Linux Mint 16 64-bit with
  gcc version 4.8.1 (Ubuntu/Linaro 4.8.1-10ubuntu9).

- GpuTest 0.5.0 for Linux has been compiled under Linux Mint 15 64-bit with
  g++ 4.7.3 (Ubuntu/Linaro 4.7.3-1ubuntu1).

- All command line parameters can be found here:
  http://www.geeks3d.com/forums/index.php/topic,3092.0.html
