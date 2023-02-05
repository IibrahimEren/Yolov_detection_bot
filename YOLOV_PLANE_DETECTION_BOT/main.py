import os
import shutil

import cv2
import numpy as np

####################################################################################################################3
# folder path - klasör yolu
dir_path = r'images\\'

# list to store files - dosyaları depolamak için liste
res = []

# Iterate directory      1   - dizini yenile
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
# print(res)

########################################################################################################################
classesFile = 'coco.names'
classNames = []

with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'yolov4.cfg'
modelWeights = 'yolov4.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


#####################################################################################################################

############################################################################################
## find us object on the image and move to specified path func
def findObjects(outputs, img):
    # Object detection stuff. I didn't know that either :D
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []
    # print("shape of the image")
    # print("ht " + str(hT) + "   wt " + str(wT) + "  ct " + str(cT))
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))

    # print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nms_threshold)
    for i in indices:
        # i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        # these global variable uses for coordinats labels
        global middle_x
        middle_x = w / 2 + x
        global middle_y
        middle_y = h / 2 + y
        global b_width
        b_width = h
        global b_height
        b_height = w
        global pix_x
        pix_x = wT
        global pix_y
        pix_y = hT

        name = classNames[classIds[i]].upper()
        # name of our object

        # print(name)
        if name == "AEROPLANE":
            ## If you want to see results of image, obj, img_shape or something you can remove the comment '#'
            # x,y is left-top corner of image(obj) x+w,y+h is right-down corner of image
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            # print(str(x) + " " + str(y) + "       " + str(x + w) + " " + str(y + h))
            # print("👍")
            # print(str(middle_x) +" "+ str(middle_y) +" "+ str(b_width) +" "+ str(b_height))

            # print("Resulation: " + str(pix_x) + "x" + str(pix_y))

            # print("EXPORT: 0 " + str("%.6f" %(middle_x/pix_x)) + " " + str("%.6f" %(middle_y/pix_y)) + " " + str("%.6f" %(b_height/pix_x)) + " " + str("%.6f" %(b_width/pix_y)))
            path = open("labels\\{}.txt".format(file[0]), "w")
            path.write("0 " + str("%.6f" % (middle_x / pix_x)) + " " + str("%.6f" % (middle_y / pix_y)) + " " + str(
                "%.6f" % (b_height / pix_x)) + " " + str("%.6f" % (b_width / pix_y)))
            path.close()
            ##################Move the detected image to another path
            # try:
            shutil.move("images\\{}".format(res[l]), "images2\\{}".format(res[l]))
            # except:
            #    print("algılanan dosya diğer klasöre taşındı")

        else:
            print(name)
            # replaces files that not pic of a plane or similar
            try:

                shutil.move("images\\{}".format(res[l]), "replaced\\{}".format(res[l]))
            except:
                print("this file moved but algorythm still read it -->")


#############################################################################################

print(len(res))
l = 0
# change direction for your own project
for length in res:
    img = cv2.imread('D:\\Projeler\\Python\\YOLOV_PLANE_DETECTION_BOT\\images\\{}'.format(res[l]))
    whT = 320
    confThreshold = 0.5
    nms_threshold = 0.3
    try:
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
        net.setInput(blob)

        layerNames = net.getLayerNames()
    #if the image is broken(?) or something move it to another path
    except:
        try:
            shutil.move("images\\{}".format(res[l]), "must_be_delete\\{}".format(res[l]))
        except:
            print("damaged file is replaced")
        print("whrong path")

    # print(layerNames)
    outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    outputs = net.forward(outputNames)
    print(res[l])
    # If the image is not suitable for function (Reason might be pix or ex. you will see your bulk image after code is done)
    try:
        findObjects(outputs, img)
    except:
        try:
            shutil.move("images\\{}".format(res[l]), "must_be_delete\\{}".format(res[l]))
        except:
            print("damaged file is replaced")
        print("FindObject Exception")

    file = os.path.splitext(res[l])
    # print(file[0])

    # cv2.imshow('Airplane Detected', img)

    if l != len(res):
        l = l + 1
        # print(l)

    if cv2.waitKey(200) == 27:
        break
    cv2.destroyAllWindows()
