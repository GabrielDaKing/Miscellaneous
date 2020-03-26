#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
import random

#importing the downloaded data set into a datafram
df  =  pd.read_csv('iris.csv',header=None)

df.tail()

#shuffling the data as in the raw form it is ordered
df = df.sample(frac=1)

alpha = 0.1

#perceptron for virginica
def perceptron_1(tt):

    random.seed(1)
    w1=random.random()
    w2=random.random()
    w3=random.random()
    w4=random.random()
    theta = random.random()
    w0=-theta
    global alpha

    for i in range(100):
        for item in tt:
            yin = w1*item[0] + w2*item[1] + w3*item[2] + w4*item[3]+ w0
            if yin<0:
                y=-1
            elif yin>0:
                y=1
            else:
                y=0

            if y!= item[4]:
                w1 = w1 + alpha*item[0]* item[4]
                w2 = w2 + alpha*item[1]* item[4]
                w3 = w3 + alpha*item[2]* item[4]
                w4 = w4 + alpha*item[3]* item[4]
                w0 = w0 + alpha*item[4]

    return w1,w2,w3,w4,w0

#perceptron for setosa
def perceptron_2(tt):

    random.seed(1)
    w1=random.random()
    w2=random.random()
    w3=random.random()
    w4=random.random()
    theta = random.random()
    w0=-theta
    global alpha

    for i in range(100):
        for item in tt:
            yin = w1*item[0] + w2*item[1] + w3*item[2] + w4*item[3]+ w0
            if yin<0:
                y=-1
            elif yin>0:
                y=1
            else:
                y=0

            if y!= item[4]:
                w1 = w1 + alpha*item[0]* item[4]
                w2 = w2 + alpha*item[1]* item[4]
                w3 = w3 + alpha*item[2]* item[4]
                w4 = w4 + alpha*item[3]* item[4]
                w0 = w0 + alpha*item[4]

    return w1,w2,w3,w4,w0

#perceptron for versicolor
def perceptron_3(tt):

    random.seed(1)
    w1=random.random()
    w2=random.random()
    w3=random.random()
    w4=random.random()
    theta = random.random()
    w0=-theta
    global alpha

    for i in range(100):
        for item in tt:
            yin = w1*item[0] + w2*item[1] + w3*item[2] + w4*item[3]+ w0
            if yin<0:
                y=-1
            elif yin>0:
                y=1
            else:
                y=0

            if y!= item[4]:
                w1 = w1 + alpha*item[0]* item[4]
                w2 = w2 + alpha*item[1]* item[4]
                w3 = w3 + alpha*item[2]* item[4]
                w4 = w4 + alpha*item[3]* item[4]
                w0 = w0 + alpha*item[4]

    return w1,w2,w3,w4,w0

#seperating into train and test sets
train, test = train_test_split(df, test_size=0.2)

#converting train set from data frame to matrix
train_list = []
for i in range(len(train)):
    x=[]
    for j in range(5):

        x.append(df.iloc[i,j])

    train_list.append(x)

#converting test set from data frame to matrix
test_list = []
for i in range(len(test)):
    x=[]
    for j in range(5):

        x.append(df.iloc[i,j])

    test_list.append(x)

#ensuring that the data is balanced
total = 0
counter_dict = {'Iris-virginica':0,'Iris-setosa':0,'Iris-versicolor':0}

for data in train_list:
    counter_dict[data[4]]+=1
    total+=1


for i in counter_dict:
    print(i,':',counter_dict[i]/total*100)

#creating seperate datasets for each neuron
train_list_virginica = []
train_list_setosa = []
train_list_versicolor = []
for i in range(len(train)):
    x=[]
    for j in range(4):
        x.append(df.iloc[i,j])
    if df.iloc[i,4]=='Iris-virginica':
        x.append(1)
    else:
        x.append(-1)

    train_list_virginica.append(x)

    x=[]
    for j in range(4):
        x.append(df.iloc[i,j])
    if df.iloc[i,4]=='Iris-setosa':
        x.append(1)
    else:
        x.append(-1)

    train_list_setosa.append(x)

    x=[]
    for j in range(4):
        x.append(df.iloc[i,j])
    if df.iloc[i,4]=='Iris-versicolor':
        x.append(1)
    else:
        x.append(-1)

    train_list_versicolor.append(x)

print(train_list_virginica[:5])
print(train_list_setosa[:5])
print(train_list_versicolor[:5])

#applying the training sets on the neurons
weights_1 = list(perceptron_1(train_list_virginica))
weights_2 = list(perceptron_2(train_list_setosa))
weights_3 = list(perceptron_3(train_list_versicolor))

full = 0
correct = 0

#testing the neurons
for item in test_list:
    y1 = weights_1[0]*item[0] + weights_1[1]*item[1] +weights_1[2]*item[2] +weights_1[3]*item[3]+weights_1[4]
    y2 = weights_2[0]*item[0] + weights_2[1]*item[1] +weights_2[2]*item[2] +weights_2[3]*item[3]+weights_2[4]
    y3 = weights_3[0]*item[0] + weights_3[1]*item[1] +weights_3[2]*item[2] +weights_3[3]*item[3]+weights_3[4]

    result_weights = [y1,y2,y3]


    x = result_weights.index(max(result_weights))

    p = str()
    if x==0:
        p = 'Iris-virginica'
    elif x==1:
        p = 'Iris-setosa'
    else:
        p ='Iris-versicolor'

    print('Predicted: ',p,"\t Actual :",item[4])

    full+=1
    if (x==0 and item[4]=='Iris-virginica') or (x==1 and item[4]=='Iris-setosa') or (x==2 and item[4]=='Iris-versicolor'):
        correct+=1

print('Sucess rate: ',correct/full)
