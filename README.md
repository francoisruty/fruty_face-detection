This repo refers to https://fruty.io/2019/07/17/state-of-the-art-2019-face-detection-with-retinaface-and-mxnet/

### General overview

We basically took the pre-trained RetinaFace network from https://github.com/deepinsight/insightface,
provided a working Dockerfile, and a python script to process videos.

### How to test

NOTE: this has been tester on a ubuntu 16.04 machine, with a Nvidia GPU (GTI 1080), with docker, nvidia-docker installed, and all relevant drivers.
We use in Dockerfile mxnet/python:1.4.1_gpu_cu100_py2 as base image. Feel free to go to https://hub.docker.com/r/mxnet/python to use a different tag, depending on your CUDA version.

git clone https://github.com/francoisruty/fruty_face-detection.git

Download the .zip file from https://drive.google.com/file/d/1jxHW3YDYgYPPrXvMHpyWljjioe2JKGnU
and put the 2 files (.params and .json) in a folder on your computer (see {{modelPath}} below).
Those 2 files are the pre-trained network.

Download input.mp4 from https://drive.google.com/open?id=18_ITpmE2Ejx5tns0OVQf19gvlhosdzJI
Put it in a folder on your computer (see {{dataPath}} below)


cd fruty_face-detection

docker build -t retinaface .

docker run -it --runtime=nvidia -v {{dataPath}}:/data -v {{modelPath}}:/model retinaface /bin/bash    

( replace {{dataPath}} with the local folder on your computer containing input.mp4, replace {{modelPath}} with the local folder on your computer containing the model parameters .params and .json)

python script.py

In my case it ran for approximately 15min, I was then able to open output.avi, and see the input footage with the human faces highlighted by a green square.

