# coding: utf-8
import dlib
import numpy as np
import urllib
import cv2
from skimage import io

detector_ = dlib.get_frontal_face_detector()


def download_image(url):
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

def face_detect(url, detection_type):
	image = download_image(url)
	dets, scores, idx = detector_.run(image, 1, detection_type)
	return [{'coords': [d.left(), d.top(), d.right(), d.bottom()], 
	         'score': scores[nn], 
	         'face_type': idx[nn]} for nn, d in enumerate(dets)]

