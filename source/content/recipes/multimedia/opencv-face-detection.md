---
title: Face-detection with OpenCV
ordernum: 2300
references:
  - url: http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
    title: Face Detection using Haar Cascades
  - url: https://realpython.com/blog/python/face-recognition-with-python/
    title: Face Recognition With Python, in Under 25 Lines of Code
---


https://blog.kevinbrown.in/programming/2014/09/27/building-and-installing-opencv-3.html


Or this:...
http://stackoverflow.com/questions/19671827/opencv-installation-on-mac-os-x

Download opencv: http://opencv.org/downloads.html

Install cmake: brew install cmake

```sh
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
make -j4
sudo make install
```
