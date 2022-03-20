import numpy as np
import pandas as pd
import cv2


def converter(a):
    r, g, b = a

    return ('{:X}{:X}{:X}').format(r, g, b)


def process(image):
    def preprocess(raw):
        image = cv2.resize(raw, (900, 600), interpolation=cv2.INTER_AREA)
        image = image.reshape(image.shape[0]*image.shape[1], 3)
        return image

    colorList = []
    modImage = preprocess(image)
    print(modImage.shape)
    for test in modImage:
        colorList.append(converter((test[0], test[1], test[2])))

    df = pd.DataFrame({'colorcode': colorList})

    counts = df['colorcode'].value_counts()

    countdict = counts.to_dict()
    topColors = []
    for index, count in enumerate(countdict):
        topColors.append(count)
        if index > 20:
            break

    return topColors
