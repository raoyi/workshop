# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-f", "--file", required=False,
        help="path to save barcode")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])

# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(image)

if args["file"]==None:
    print(barcodes[0][0].decode('utf-8'))
else:
    f = open(args["file"], 'wb')
    f.write(barcodes[0][0])
    f.close()
