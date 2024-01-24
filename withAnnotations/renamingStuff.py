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
x = [glob.glob(imgDir+y) for y in ['*.jpg', '*.png', '*.bmp']]
x = sum(x , [])
random.shuffle(x)

a=0
for i in tqdm.tqdm(x, desc = "ReNamin' the Images n Txt Labels Yo!", colour = 'red'):
    os.rename(i, imgDir+str(a)+'cone'+'.jpg')
    os.rename(i[:-4]+'.txt', imgDir+str(a)+'cone'+'.txt')
    a+=1
t2 = time.time()
print("\nCompleteExecTime: ", (t2-t1))