import sys
from optparse import OptionParser

import cv2
import numpy as np

from post import post_numbers
from videorand import serialize_frame

parser = OptionParser()
parser.add_option("-a", "--addr", dest="addr",
                  help="address to publish", metavar="ADDR")
parser.add_option("-k", "--key", dest="key",
                  help="key address of the host", metavar="KEY")
parser.add_option("-f", "--footprint", dest="footprint",
                  help="maximum amount of numbers to keep in cache", metavar="FOOT")
parser.add_option("-s", "--show", dest="show",
                  help="show the camera output", metavar="SHOW")


(options, args) = parser.parse_args()
if options.key is None:
    print("--key was not provided!")
    sys.exit()

print("key is", options.key)

addr = "127.0.0.1:7890"

if options.addr is None:
    print("address was not provided, using default")
else:
    addr = options.addr

if not (addr.startswith("http://") or addr.startswith("https://")):
    addr = "http://" + addr

if not addr.endswith("/"):
    addr = addr + "/"

print("target address is", addr)

max_footprint = 1000

if options.footprint is not None:
    max_footprint = options.footprint

print("max footprint:", max_footprint)

show = options.show is not None

np.seterr(over='ignore')
cap = cv2.VideoCapture(0)
numbers = []
chunk_size = 30
max_numbers = 10
currentNumber = 0
for i in range(0, max_numbers):
    numbers.append(i)

print("max frames:", max_numbers)
print("chunk size:", chunk_size)
print("capturing the video...")

footprint = {}
total = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        width = len(frame[0])
        height = len(frame)

        sid = serialize_frame(frame, width, height, chunk_size)
        if currentNumber == max_numbers:
            currentNumber = 0

            if len(footprint) > max_footprint:
                print("footprint cleared,", len(footprint), "elements removed")
                footprint.clear()
                total = 0

            total += max_numbers
            for n in numbers:
                footprint[n] = n

            print(numbers)
            print("uniqueness", (total / len(footprint)) * 100.0, "%")

            post_numbers(numbers, addr, options.key)

        numbers[currentNumber] = int(sid)
        currentNumber += 1

        if show:
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release everything if job is finished
cap.release()
cv2.destroyAllWindows()