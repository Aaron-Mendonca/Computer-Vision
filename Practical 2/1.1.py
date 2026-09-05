import cv2 as cv

img1 = cv.imread("image1.jpg")
img2 = cv.imread("image2.jpg")

stitcher = cv.Stitcher_create()

status, result = stitcher.stitch([img1, img2])

if status == cv.Stitcher_OK:
    cv.imshow("Panorama", result)

    cv.imwrite("Panorama.jpg", result)

    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("Image stitching failed")