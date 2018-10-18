##################################################
# IINI4014 Python for programmers (2018 HØST)
# Nadine Obwaller
# Exercise 7: Finding format of specified image type
##################################################

import sys
import binascii
import os
import shutil

   
def printFormat(image):
	(img, type) = image
	newdir = "sorted/"+type
	#print the file and its type
	print("File "+ img + " is of type " + type)

	#create a new folder for every newly found filetype
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	#move the file to the subfolder - replace existing file
	shutil.move(os.path.join('.', img), os.path.join(newdir, img))


def findFormat(files):
	img_signatures = [
    	binascii.unhexlify(b'FFD8FFE0'), #jpeg
    	binascii.unhexlify(b'49492A00'), #tiff
    	binascii.unhexlify(b'474946383961'), #GIF89a
    	binascii.unhexlify(b'89504E470D0A1A0A') #png
	]

	list_of_files = files

	#create "sorted" folder
	if not os.path.exists("sorted"):
		os.makedirs("sorted")

	#check every image file in file list
	for image in list_of_files:
		try:
			#open file in binary format
			with open(image, 'rb') as file:
				#read first 4 bytes of every file
				first_four_bytes = file.read(4)
				for i, v in enumerate(['jpg', 'tif', 'gif', 'png']):
					if first_four_bytes in img_signatures[i]:
						#if first four bytes are found in either gif or png the additional bytes has to be read 
						#in order to verify the files
						if i == 2:
							#read additional 2 bytes to verify that it's a gif
							additional_two_bytes = file.read(2)
							if first_four_bytes+additional_two_bytes in img_signatures[i]:
								printFormat((image, v))
						elif i == 3:
							#read additional 4 bytes to verify that it's a png
							additional_four_bytes = file.read(4)
							if first_four_bytes+additional_four_bytes in img_signatures[i]:
								printFormat((image,v))
						#file is either a jpeg or a tiff
						else: 
							printFormat((image, v))
						
						
		except FileNotFoundError:
			print("File '"+image + "' not found!")
			pass

if len(sys.argv) < 2:
    print("usage: python3 ex7_obwaller_nadine.py \"<img.jpg/gif/png/tif>\"")
    sys.exit(1)

files = (sys.argv[1:])

findFormat(files)
