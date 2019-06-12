import csv
import NameFind
import numpy as np
from enhane import main1
import cv2  # computer vision for real time application

multi=0
def main(name):

    face_classifier = cv2.CascadeClassifier('cascade_classifier/haarcascade_frontalcatface.xml')

    def face_extractor(img):

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converts to gray scale
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)  # 1.3 scaling factor reduce image size 30%, 5 neighbours

        if faces is ():  # if no face
            return None
        global multi
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]  # cropped_face as list
            multi=multi+1
        return cropped_face

    cap = cv2.VideoCapture(0)  # use webcam
    count = 0  # to cound captured faces

    if name.isalpha():
        Id = str(NameFind.AddName(name))

        while True:
            global multi
            multi=0
            ret, frame = cap.read()  # ret is boolean and frame is image
            if face_extractor(frame) is not None:

                face = cv2.resize(face_extractor(frame), (200, 200))  # crops face to specific dimension for uniformity
                showface = face  # show face to display color cropped image
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts to gray scale
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    draw_box(frame, x, y, w, h)  # draws rectangle ; color ; thickness
                # img=cv2.resize(img,(1300, 800)) # resize the image
                cv2.putText(frame, "DETECTED", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Capture face', frame)
                if multi<=2: #To capture only single face
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # converted to grays cale to store as dataset
                    face=main1(face)
                    cv2.imshow("face",face)
                    #face = cv2.addWeighted(face, a, np.zeros(face.shape, face.dtype), 0, b)

                    file_name_path = "faces/ " + name + "." + Id + '.' + str(count) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    count += 1
                    cv2.putText(showface, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)  # font face,
                    # size,color,thickness
                    cv2.imshow('Face Cropper', showface)



            else:
                cv2.putText(frame, "NO FACE ", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Capture face', frame)
                print("Face not Found")

            if cv2.waitKey(1) == 27 or count == 100:
                break

        cap.release()
        cv2.destroyAllWindows()
        print('Samples Collection Complete!!!')
        row = [Id, name]
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        print("Images Saved for ID : " + Id + " Name : " + name)
        # message.configure(text=res) for saying images saved
    else:
        # res = "Enter Numeric Id"
        # message.configure(text=res) for saying name is not in string
        print("Enter valid name")


if __name__ == '__main__':
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
