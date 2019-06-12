import cv2
import numpy as np
import os
from PIL import Image


def main():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces, Id = getImagesAndLabels("faces")
    recognizer.train(faces, np.array(Id))
    print(np.array(Id))
    print(faces)
    recognizer.save("Face_classifier\Classifier.xml")
    # res = "Image Trained"  # +",".join(str(f) for f in Id)
    print("Trained!")


if __name__ == '__main__':
    main()


def getImagesAndLabels(path):
    # get the path of all the images in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []  # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids
