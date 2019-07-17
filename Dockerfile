FROM mxnet/python:1.4.1_gpu_cu100_py2

RUN apt-get update --fix-missing
RUN apt-get install -y make cython python-numpy vim python-setuptools python-opencv
RUN pip install opencv-python==3.4.1.15
RUN pip install numpy
RUN pip install future

COPY . /app
RUN cd /app && make

WORKDIR /app
