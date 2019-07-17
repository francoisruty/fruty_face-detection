import cv2
import sys
import numpy as np
import datetime
import os
import glob
from retinaface import RetinaFace

cap = cv2.VideoCapture()
cap.open("/data/input.mp4")

thresh = 0.8
scales = [1024, 1980]

gpuid = 0
detector = RetinaFace('/model/R50', 0, gpuid, 'net3')

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width,height)

fps = 24

frames = []
counter = 0

flip = False

while True:
    (rv, im) = cap.read()   # im is a valid image if and only if rv is true

    if not rv: #we reached the end of video file, we write the modified frames to a new video file
        filename = '/data/output.avi'
        out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'DIVX'), fps, size, True)
        for i in range(len(frames)):
            out.write(frames[i])
        out.release()
        break

    counter = counter + 1
    
    im_shape = im.shape
    target_size = scales[0]
    max_size = scales[1]
    im_size_min = np.min(im_shape[0:2])
    im_size_max = np.max(im_shape[0:2])
    im_scale = float(target_size) / float(im_size_min)
    if np.round(im_scale * im_size_max) > max_size:
        im_scale = float(max_size) / float(im_size_max)
    faces, landmarks = detector.detect(im, thresh, scales=[im_scale], do_flip=flip)
    if faces is not None:
        #For each face, we draw a rectangle
        for i in range(faces.shape[0]):
            box = faces[i].astype(np.int)
            cv2.rectangle(im, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
    frames.append(im)

    if counter % fps == 0:
        print(counter)


cap.release()



