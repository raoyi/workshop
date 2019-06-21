from pyzbar.pyzbar import decode
from PIL import Image
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-f", "--file", required=False,
        help="path to save barcode")
args = vars(ap.parse_args())

#get barcodes
barcodes = decode(Image.open(args["image"]))
num = len(barcodes)

if args["file"]==None:
    for i in range(num):
        print(barcodes[i][0].decode('utf-8'))
        
else:
    f = open(args["file"], 'w')
    for i in range(num):
        f.write(barcodes[i][0].decode('utf-8')+'\n')
        
    f.close()
