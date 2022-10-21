import os
import random

trainval_percent = 0.9
train_percent = float(8 / 9)
script_path = os.getcwd()
# xmlfilepath = 'C:/Users/Laona--LJJ/PycharmProjects/pythonProject7/VOC2007/Annotations'
xmlfilepath = os.path.join(script_path, "VOC2007/Annotations")
# txtsavepath = 'ImageSets/main'
txtsavepath = os.path.join(script_path, "VOC2007/ImageSets/main")
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('VOC2007/ImageSets/main/trainval.txt', 'w')
ftest = open('VOC2007/ImageSets/main/test.txt', 'w')
ftrain = open('VOC2007/ImageSets/main/train.txt', 'w')
fval = open('VOC2007/ImageSets/main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
