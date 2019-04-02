import sys, os
import numpy as np
import random
import dircache
from math import *
from PIL import Image
from pathlib import Path
import re

def filterCoordinate(c,m):
	if c < 0:
		return 0
	elif c > m:
		return m
	else:
		return c

train_file_lists = ['/home/ubnt/datasets/celeba/Anno/list_bbox_celeba.txt']

def prepare_train_val(filename, tran_val, start_num, end_num):

    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    print "skip line 0: " + lines[0]
    print "skip line 1: " + lines[1]
    os.system('mkdir -p train' + str(start_num) + '-' + str(end_num) + '/images ;mkdir -p train' + str(start_num) + '-' + str(end_num) + '/labels/')
    os.system('rm -rf train' + str(start_num) + '-' + str(end_num) + '/images/* ;rm -rf train' + str(start_num) + '-' + str(end_num) + '/labels/*')
    #os.system('rm -rf val'+tart_num+'-'+end_num+'/images/* ;rm -rf val/labels/*')

    i = 2
    while i < len(lines) - 2:
            tokens =  re.split("(\s+)", lines[i])
            i = i + 1

            if i - 2 < start_num or i - 2 > end_num:
                continue

	    img_file = '/home/ubnt/datasets/celeba/Img/img_celeba/img_celeba.7z/' + tokens[0]
            img = Image.open(img_file)
            w = img.size[0]
            h = img.size[1]
            if w > 640 or h > 640:
                continue

            print tokens
            #my_file = Path('train'+tart_num+'-'+end_num+'/images/' + img_file)
            #if my_file.is_file() == False:
            os.symlink(img_file, 'train' + str(start_num) + '-' + str(end_num) + '/images/' + tokens[0])

            f = open('train' + str(start_num) + '-' + str(end_num) + '/labels/' + tokens[0].split('.')[0]+'.txt', 'a')

            img = Image.open(img_file)
	    w = img.size[0]
	    h = img.size[1]

            x_min = int(tokens[2])
            y_min = int(tokens[4])
            x_max = int(tokens[2]) + int(tokens[6])
            y_max = int(tokens[4]) + int(tokens[8])
            text = "face 0 0 0" + ' '  + str(x_min) + ' ' + str(y_min) + ' ' + str(x_max) + ' ' + str(y_max) + ' ' + '0 0 0 0 0 0 0''\n'
            f.write(text)
            f.close()
            i = i + 1

train_img_dir = '/home/ubnt/datasets/fddb/train/images/'
train_label_dir = '/home/ubnt/datasets/fddb/train/labels/'
val_img_dir = '/home/ubnt/datasets/fddb/val/images/'
val_label_dir = '/home/ubnt/datasets/fddb/val/labels/'

start_num = 10001
end_num = 20000

def prepare_val(num):
    i = 0
    while i < num:
        # choose random file
        filename = random.choice(os.listdir(train_img_dir))
        # print filename
        # move .jpg
        # print train_img_dir + filename
        os.rename(train_img_dir + filename, val_img_dir + filename)
        # move label
        os.rename(train_label_dir + filename.split('.')[0] + '.txt', val_label_dir + filename.split('.')[0] + '.txt')
        i = i + 1

# prepare train data
for file_name in train_file_lists:
    prepare_train_val(file_name, 'train', start_num, end_num)

# prepare val data: move 500 sets from train data
#prepare_val(500)



