import xml.etree.ElementTree as ET
from colorama import Fore, Style
from tkinter import filedialog
from PIL import Image
import numpy as np
import tqdm
import glob
import time

t1 = time.time()
print("Select the Directory Yo!")
imgDir = filedialog.askdirectory()
if "\\" in imgDir:
    imgDir = imgDir + '\\'
else:
    outDir = imgDir + '/'
print("---->", imgDir)
x = [glob.glob(imgDir+y) for y in ['*.jpg', '*.png', '*.tiff', '*.bmp', '*.jpeg']]
x = [y for y in sum(x , []) if 'Mirror' not in y]
for i in tqdm.tqdm(x, desc = "Mirrorin' the Images Yo!", colour = 'red'):
    t1_ = time.time()
    img = Image.open(i).convert('RGB')
    imgAr = np.array(img)
    mirImg = np.fliplr(imgAr)
    outImg = Image.fromarray(mirImg)

    z = i.split(".")
    f = z[0]+'.xml'
    z_ = str('Mirror.').join(z)
    tree = ET.parse(f)
    root = tree.getroot()

    folderElement = root.find('folder')
    fileElement = root.find('filename')
    folderElement.text = 'labels'
    fileElement.text = z_
    pathElement = root.find('path')
    if pathElement is not None:
        pathElement.text = '..//'+root.findtext('folder')+'//'+root.findtext('filename')
    sizeElement = root.find('size')
    widthElement = sizeElement.find('width')
    heightElement = sizeElement.find('height')
    xImg = int(widthElement.text)
    yImg = int(heightElement.text)

    objectElements = root.findall('object')
    for objectElement in objectElements:
        bbxElement = objectElement.find('bndbox')
        xMin = int(float(bbxElement.find('xmin').text))
        yMin = int(float(bbxElement.find('ymin').text))
        xMax = int(float(bbxElement.find('xmax').text))
        yMax = int(float(bbxElement.find('ymax').text))

        xMin_ = xImg - xMax
        yMin_ = yMin
        xMax_ = xImg - xMin
        yMax_ = yMax

        bbxElement.find('xmin').text = str(xMin_)
        bbxElement.find('ymin').text = str(yMin_)
        bbxElement.find('xmax').text = str(xMax_)
        bbxElement.find('ymax').text = str(yMax_)
    xmlString = ET.tostring(objectElement, encoding='utf8').decode('utf8')
    print(xmlString)
    
    f = str('Mirror.').join(f.split('.'))
    tree.write(f)
    outImg.save(z_)
t2 = time.time()
print("\nCompleteExecTime: ", (t2-t1))