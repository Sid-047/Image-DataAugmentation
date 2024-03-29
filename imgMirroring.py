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
x = sum(x , [])
for i in tqdm.tqdm(x, desc = "Mirrorin' the Images Yo!", colour = 'red'):
    t1_ = time.time()
    img = Image.open(i).convert('RGB')
    imgAr = np.array(img)
    mirImg = np.fliplr(imgAr)
    outImg = Image.fromarray(mirImg)

    z = i.split(".")
    z = str('_.').join(z)
    outImg.save(z)
    t2_ = time.time()
t2 = time.time()
print("\nCompleteExecTime: ", (t2-t1))