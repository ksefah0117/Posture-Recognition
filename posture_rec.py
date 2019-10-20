#Kwaku
#Josiah

##-------------------------------------------------------------------------------------------Posture Recognition-------------------------------------------------------------------------------------##
#import cv2
#import numpy as np
#import pandas as pd

import matplotlib.pyplot as plt
#%matplotlib inline 

#See the dir.
import os
import random 
import gc #gabage collector for cleaning 
import matplotlib.image as mpimg

train_dir = '../Posture-Recognition/train'
test_dir = '../Posture-Recognition/test'


train_one = ['../Posture-Recognition/train/ONE/{}'.format(i) for i in os.listdir(train_dir+"/ONE") if 'ONE' in i] #get ONE
train_two = ['../Posture-Recognition/train/TWO/{}'.format(i) for i in os.listdir(train_dir+"/TWO") if 'TWO' in i] #get TWO
train_three = ['../Posture-Recognition/train/THREE/{}'.format(i) for i in os.listdir(train_dir+"/THREE") if 'THREE' in i] #get ONE
train_four = ['../Posture-Recognition/train/FOUR/{}'.format(i) for i in os.listdir(train_dir+"/FOUR") if 'FOUR' in i] #get ONE
train_five = ['../Posture-Recognition/train/FIVE/{}'.format(i) for i in os.listdir(train_dir+"/FIVE") if 'FIVE' in i] #get ONE

train_imgs = train_one + train_two + train_three + train_four + train_five

random.shuffle(train_imgs)

test_one = ['../Posture-Recognition/test/ONE/{}'.format(i) for i in os.listdir(test_dir+"/ONE") if 'ONE' in i] #get ONE
test_two = ['../Posture-Recognition/test/TWO/{}'.format(i) for i in os.listdir(test_dir+"/TWO") if 'TWO' in i] #get ONE
test_three = ['../Posture-Recognition/test/THREE/{}'.format(i) for i in os.listdir(test_dir+"/THREE") if 'THREE' in i] #get ONE
test_four = ['../Posture-Recognition/test/FOUR/{}'.format(i) for i in os.listdir(test_dir+"/FOUR") if 'FOUR' in i] #get ONE
test_five = ['../Posture-Recognition/test/FIVE/{}'.format(i) for i in os.listdir(test_dir+"/FIVE") if 'FIVE' in i] #get ONE

test_imgs = test_one + test_two + test_three + test_four + test_five

for ima in train_imgs[0:3]:
	img=mpimg.imread(ima)
	imgplot = plt.imshow(img)
	plt.show()
