# videorand

videorand is a program that generates random numbers in real-time
based on the input from a video camera and submits generated numbers via http.
## Installation
```bash
$ pip3 install numpy
$ pip3 install opencv-python
$ git clone https://github.com/kisulken/videorand
```
## Example of use
```bash
$ python3 capture.py --addr="127.0.0.1:7890" --key="mySecrectKeyHanlder"
```

Where the key is a unique address that will be availble on a server machine (i.e http://127.0.0.1:7890/mySecrectKeyHanlder)
in order to accept new values.

For this example to operate properly there must be a [server](https://github.com/kisulken/truerandom-mirror) running on port 7890
