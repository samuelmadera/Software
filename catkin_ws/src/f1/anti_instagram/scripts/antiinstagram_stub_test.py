#!/usr/bin/env python

from anti_instagram import (
	AntiInstagram, L2_image_distance, load_image, logger, random_image)
from duckietown_utils import col_logging  # @UnusedImport
import cv2
import sys
import timeit
import traceback
from anti_instagram.utils import wrap_test_main

# calculate transform for each image set
def testImages(ai, imageset, gtimageset, error_threshold):
	error = []
	for i, image in enumerate(imageset):
		#print(image.shape)
		ai.calculateTransform(image,True)
		logger.info('health: %s' % ai.health)
		transimage = ai.applyTransform(image)
		testimgf = "testimage%d.jpg" % i
		cv2.imwrite(testimgf,transimage)
		testimg = cv2.imread(testimgf)
		# uncorrected is > 500
		e = L2_image_distance(testimg, gtimageset[i])
		if e > error_threshold:
			logger.error("Correction seemed to fail for image %s" % i)
		error.append(e)
	return error

def anti_instagram_test():
	ai = AntiInstagram()

	#### TEST SINGLE TRANSFORM ####
	error_threshold = 500
	# load test images
	failure = False
	imagesetf = [
		"inputimage0.jpg",
		"inputimage1.jpg"
	]
	gtimagesetf = [
		"groundtruthimage0.jpg",
		"groundtruthimage1.jpg"
	]
	#
	imageset = map(load_image, imagesetf)
	gtimageset = map(load_image, gtimagesetf)
	errors = testImages(ai, imageset, gtimageset, error_threshold)
	logger.info("Test Image Errors: %s" % errors)

	if max(errors) > error_threshold:
		failure = True

	if failure:
		raise Exception("Tests not passed.")

	logger.info("All tests passed.")
	
if __name__ == '__main__':
	wrap_test_main(anti_instagram_test)
