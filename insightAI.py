from flask import Flask, render_template, request, redirect, jsonify, g
import gpt_2_simple as gpt2
import flask_login
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import Dynaconf
import PIL
import cv2
import numpy as np
from sklearn.model_selection import train_test_split # as something ez to write pls
import tensorflow as tf
import tensorflow_hub as hub
import os
import matplotlib.pyplot as pplt
import matplotlib.image as ppltimg
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler

"""
for dirname, _, filenames in os.walk('archive/'):
    for filename in filenames:
        
        testSet = os.path.join(dirname, filename)
        print(testSet)
"""
        
bruh = os.listdir("archive/1/1/")

print(bruh[0])

#testShoeImage = ppltimg.imread(bruh)

pplt.imshow(bruh)


#gpt2.download_gpt2(model_name = '124M')

#session = gpt2.start_tf_sess()

#9992



#trainingData1s = os.listdir("/archive")[0:9992]

#####

"""
trainingData2s = os.listdir("archive/2/")[0:11000]
trainingData3s = os.listdir("archive/3/")[0:11000]
trainingData4s = os.listdir("archive/4/")[0:11000]
trainingData5s = os.listdir("archive/5/")[0:11000]
trainingData6s = os.listdir("archive/6/")[0:11000]
trainingData7s = os.listdir("archive/7/")[0:11000]
trainingData8s = os.listdir("archive/8/")[0:11000]
trainingData9s = os.listdir("archive/9/")[0:11000]
trainingData10s = os.listdir("archive/10/")[0:11000]
trainingData11s = os.listdir("archive/11/")[0:11000]
trainingData12s = os.listdir("archive/12/")[0:11000]
trainingData13s = os.listdir("archive/13/")[0:11000]
trainingData14s = os.listdir("archive/14/")[0:11000]
trainingData15s = os.listdir("archive/15/")[0:11000]
trainingData16s = os.listdir("archive/16/")[0:11000]
trainingData17s = os.listdir("archive/17/")[0:11000]
trainingData18s = os.listdir("archive/18/")[0:11000]
trainingData19s = os.listdir("archive/19/")[0:11000]
trainingData20s = os.listdir("archive/20/")[0:11000]
trainingData21s = os.listdir("archive/21/")[0:11000]
"""

#print(trainingData1s[0])


"""
print(trainingData2s[0])
print(trainingData3s[0])
print(trainingData4s[0])
print(trainingData5s[0])
print(trainingData6s[0])
print(trainingData7s[0])
print(trainingData8s[0])
print(trainingData9s[0])
print(trainingData10s[0])
print(trainingData10s[0])
print(trainingData11s[0])
print(trainingData12s[0])
print(trainingData13s[0])
print(trainingData14s[0])
print(trainingData15s[0])
print(trainingData16s[0])
print(trainingData17s[0])
print(trainingData18s[0])
print(trainingData19s[0])
print(trainingData20s[0])
print(trainingData21s[0])

    

testShoeImage = ppltimg.imread("archive/1/1")


pplt.imshow(testShoeImage)

"""

####

"""
for (root,dirs,files) in os.walk('.', topdown=True):
        print (root)
        print (dirs)
        print (files)

labels = []

for typeOfShoe in trainingData1s:
    if "High1s" in typeOfShoe:
        labels.append(0)
    elif "" in typeOfShoe:
        labels.append(1)
    elif "Low1s" in typeOfShoe:
        labels.append(2)
    elif "Low1s" in typeOfShoe:
            labels.append(3)
    elif "Low1s" in typeOfShoe:
            labels.append(4)
    elif "Low1s" in typeOfShoe:
            labels.append(5)
    elif "Low1s" in typeOfShoe:
            labels.append(6)
    elif "Low1s" in typeOfShoe:
            labels.append(7)
    elif "Low1s" in typeOfShoe:
            labels.append(8)
"""

#for fileName in trainingData:
#    image = PIL.Image.open("train/" + fileName)
#    image = image.resize((224, 224))
#    image = image.convert("RGB")
    
#    image.save("resized/" + fileName)

######
