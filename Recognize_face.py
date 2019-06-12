import cv2
import pandas as pd
import numpy as np
from enhane import main1

def main():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("Face_classifier/Classifier.xml")
    harcascadePath = "cascade_classifier/haarcascade_frontalcatface.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            draw_box(im, x, y, w, h)
            crop=gray[y:y + h, x:x + w]
            cv2.imshow("gray", crop)
            #crop = cv2.addWeighted(crop, a, crop, 0, b)

            #crop = cv2.addWeighted(crop, a, np.zeros(crop.shape, crop.dtype), 0, b)
            crop=main1(crop)
            cv2.imshow("enhance",crop)

            Id, conf = recognizer.predict(crop)
            #Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if conf < 70:
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = aa
                color =(255, 255, 255)
            else:
                Id = 'Unknown'
                tt = str(Id)
                tt = str(Id)
                color = (0, 0, 255)
            cv2.putText(im, str(tt), (x, y-10), font, 0.5, color, 1)  # text_desc, font, fontScale, lineType
        cv2.imshow('im', im)
        if cv2.waitKey(1) == 27:
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == 'main':
    main()


def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + int(w / 5), y), (0, 255, 0), 2)
    cv2.line(Image, (x + int((w / 5) * 4), y), (x + w, y), (0, 255, 0), 2)
    cv2.line(Image, (x, y), (x, y + int(h / 5)), (0, 255, 0), 2)
    cv2.line(Image, (x + w, y), (x + w, y + int(h / 5)), (0, 255, 0), 2)
    cv2.line(Image, (x, (y + int(h / 5 * 4))), (x, y + h), (0, 255, 0), 2)
    cv2.line(Image, (x, (y + h)), (x + int(w / 5), y + h), (0, 255, 0), 2)
    cv2.line(Image, (x + (int(w / 5) * 4), y + h), (x + w, y + h), (0, 255, 0), 2)
    cv2.line(Image, (x + w, (y + int(h / 5 * 4))), (x + w, y + h), (0, 255, 0), 2)
