from tkinter import filedialog
import random
import tqdm
import glob
import time
import os

t1 = time.time()
print("Select the Directory Yo!")
imgDir = filedialog.askdirectory() + '\\'
print("---->", imgDir)
x = [glob.glob(imgDir+y) for y in ['*.jpg', '*.png', '*.tiff', '*.bmp', '*.jpeg']]
random.shuffle(x)

a=0
for i in tqdm.tqdm(x, desc = "ReNamin' the Images Yo!", color = 'red'):
    os.rename(i, imgDir+str(a)+'.png')
    a+=1
t2 = time.time()
print("\nCompleteExecTime: ", (t2-t1))