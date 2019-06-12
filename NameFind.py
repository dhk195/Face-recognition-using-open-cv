#     ----------- FUNCTION TO READ THE FILE AND ADD THE NAMES AND IDs IN TO TUPLES

import cv2


def AddName(Name):

    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info)) + 1)
    Info.write(str(ID) + "," + Name + "\n")
    print("Name Stored in " + str(ID))
    Info.close()
    return ID

