import cv2 as cv

# get the image from webcam

stream = cv.VideoCapture(0)

# error handling if the stream is not opened

if not stream.isOpened():
    print("no stream detected")
    exit()

# code to execute whenever there is an output

while(True):
    return_output, frame = stream.read()
    if not return_output:
        print("stream finished")
        break

    #show the webcam image frame by frame in the window

    cv.imshow("webcam", frame)
    if cv.waitKey(1) == ord('q'): # press q to get out
        break

stream.release()
cv.destroyAllWindows()