# gopro-timelapse-conversion
A couple of Python utility files to resize all the gopro files in a folder, a tool for renaming with correctly formatted numbers, and then quick FFMPEG instructions

This is for people who either don't have the GoPro Timelapse Video automatic conversion option in their cam, or who accidentally created a regular timelapse of photos, at the default resolution of 4K. Many computers have memory problems using FFMPEG with 4K images, so this program reduces the size to 2,000 pixels. 

This is developed in Python 3.6 but works in other versions around this. 
To use the resizer, you'll need to install OpenCV: instructions here - https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html (you may need to use other methods too, depending on what Python you are running. 

First make sure to copy all GoPro image files into one folder (i.e. 104GOPRO, 105GOPRO, etc.)

Second, run the resizer python file, in the same directory as all the files.  It will create a folder called resized.  This is set to 2,000 pixels in width. 
you would type python resizeallima....py

Third, make sure all the coverted images are in a folder named "test"

Fourth, run the testrename python file (making sure that you confirm that you are one directory level above test). 
to do this you type python testren...py

Make sure you install FFMPEG, and set it in your PATH, so that you can use it anywhere in your computer
Then run FFMPEG using a command like this:
ffmpeg -f image2 -i G%4d.jpg convertedtimelapse1.mp4

The %4d will rename all the files, so they are sequential, starting with 01 (which FFMPEG requires). 

Then after a while you should see this mp4 file in this directory.   Good to go. 
