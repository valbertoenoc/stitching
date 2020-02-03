import argparse
import imutils
import cv2
import numpy as np

from imutils import paths


def main(): 
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", default='images/building', help="path to input directory of images to stitch")
    ap.add_argument("-o", "--output", default='images/building/stitched.png', help="path to the output image")
    args = vars(ap.parse_args())

    imagePaths = sorted(list(paths.list_images(args["images"])))
    images = []
    
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        images.append(image)

    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    if status == 0:
        cv2.imwrite(args["output"], stitched)
    
        cv2.imshow("Stitched", stitched)
        cv2.waitKey(0)
    
    else:
        print("[INFO] image stitching failed ({})".format(status))


if __name__ == "__main__":
    main()