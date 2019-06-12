



import cv2
import numpy as np


def main1(img):

    thres = np.mean(img)
    if thres>150:
        print('light')
        crop = cv2.addWeighted(img, 1.2, np.zeros(img.shape, img.dtype), 0, -30)
        #cv2.imshow("crop", crop)
        return crop
    elif 100 < thres <= 150:
        print('inter')
        crop = cv2.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, -10)
        return crop
        #cv2.imshow("crop", crop)
    else:
        print('dark')
        crop = cv2.addWeighted(img, 2, np.zeros(img.shape, img.dtype), 0, 1)
        return crop


if __name__ == '__main__':
    main1()




