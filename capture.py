import cv2
import numpy as np

from post import post_numbers
from videorand import serialize_frame

np.seterr(over='ignore')
cap = cv2.VideoCapture(0)
numbers = []
chunk_size = 30
max_numbers = 10
currentNumber = 0
for i in range(0, max_numbers):
    numbers.append(i)

print("Capturing the video...")
print("max frames:", max_numbers)
print("chunk size:", chunk_size)

footprint = {}
max_footprint = 1000
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

            post_numbers(numbers)

        numbers[currentNumber] = int(sid)
        currentNumber += 1

        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release everything if job is finished
cap.release()
cv2.destroyAllWindows()