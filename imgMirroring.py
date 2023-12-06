from tkinter import filedialog
from PIL import Image
import numpy as np
import tqdm
import glob
import time

t1 = time.time()
print("Select the Directory Yo!")
inImg = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff")])
imgDir = ('/'.join([x.replace(" ", "~") for x in inImg.split("/")[:-1]])).replace("~", " ") + '/'
print("---->", imgDir)
x = [glob.glob(imgDir+y) for y in ['*.jpg', '*.png', '*.tiff', '*.bmp', '*.jpeg']]

for i in tqdm(x, desc = "Mirrorin' the Images Yo!"):
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