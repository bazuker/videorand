# videorand

videorand is a program that generate true random numbers in real-time
based on the input from a video camera and submits generated numbers via http.

Example of use
```bash
$ python3 caption.py --addr="127.0.0.1:7890" --key="mySecrectKeyHanlder"
```

Where the key is a unique address that will be availble on a server machine (i.e http://127.0.0.1:7890/mySecrectKeyHanlder)
in order to accept new values.

For this example to operate properly there must be a [server](https://github.com/kisulken/truerandom-mirror) running on port 7890
