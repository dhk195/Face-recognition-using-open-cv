# USAGE
# python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

def main():
    def draw_box(Image, x, y, w, h):
        cv2.line(Image, (x, y), (x + int(w / 5), y), (0, 255, 0), 2)
        cv2.line(Image, (x + int((w / 5) * 4), y), (x + w, y), (0, 255, 0), 2)
        cv2.line(Image, (x, y), (x, y + int(h / 5)), (0, 255, 0), 2)
        cv2.line(Image, (x + w, y), (x + w, y + int(h / 5)), (0, 255, 0), 2)
        cv2.line(Image, (x, (y + int(h / 5 * 4))), (x, y + h), (0, 255, 0), 2)
        cv2.line(Image, (x, (y + h)), (x + int(w / 5), y + h), (0, 255, 0), 2)
        cv2.line(Image, (x + (int(w / 5) * 4), y + h), (x + w, y + h), (0, 255, 0), 2)
        cv2.line(Image, (x + w, (y + int(h / 5 * 4))), (x + w, y + h), (0, 255, 0), 2)


    # load our serialized model from disk
    print("[INFO] loading model...")
    # net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
    net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "lbpmodel")
    # initialize the video stream and allow the cammera sensor to warmup
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # time.sleep(2.0)

    # loop over the frames from the video stream
    count=0
    while True:

        no = 0
        # grab the frame from the threaded video stream and resize it
        # to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame)

        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))

        # pass the blob through the network and obtain the detections and
        # predictions
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections
        for i in range(0, detections.shape[2]):

            # extract the confidence (i.e., probability) associated with the
            # prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > 0.5:

                # compute the (x, y)-coordinates of the bounding box for the
                # object
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the bounding box of the face along with the associated
                # probability
                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                #cv2.rectangle(frame, (startX, startY), (endX, endY),(0, 0, 255), 2)
                #cv2.putText(frame, str(no), (startX, startY),	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                draw_box(frame, startX, startY, endX - startX, endY - startY)

                #face=frame[startY:endY,startX:endX]
                #count=count+1
                #file_name_path = "faces/ " + "zzz" + "." + "1" + '.' + str(count) + ".jpg"
                #cv2.imwrite(file_name_path, face)


        cv2.imshow("Frame", frame)
        # show the output frame
        # if the `q` key was pressed, break from the loop
        if cv2.waitKey(1) == 27:
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()


if __name__ == 'main':
    main()
