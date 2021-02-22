---
title: MLP + LSTM with MNIST on Google Colab
draft: false
weight: 21
description: >
  MLP + LSTM with MNIST on Google Colab
---


<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_mlp_with_lstm.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_mlp_with_lstm.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
    <td><a href="https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_mlp_with_lstm.ipynb" download><img src="https://www.tensorflow.org/images/download_logo_32px.png" alt=""/></a> Download Notebook</td>    
  </tr>
</table>  
</div>

In this lesson we discuss in how to create a simple IPython Notebook to solve
an image classification problem with Multi Layer Perceptron with LSTM. 

## Pre-requisites

Install the following Python packages

1. cloudmesh-installer
2. cloudmesh-common

```bash
pip3 install cloudmesh-installer
pip3 install cloudmesh-common
```

## Sample MLP + LSTM with Tensorflow Keras

## Import Libraries

```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, SimpleRNN, InputLayer, LSTM, Dropout
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.datasets import mnist
from cloudmesh.common.StopWatch import StopWatch
```

## Download Data and Pre-Process

```python
StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")


StopWatch.start("data-pre-process")
num_labels = len(np.unique(y_train))


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


image_size = x_train.shape[1]
x_train = np.reshape(x_train,[-1, image_size, image_size])
x_test = np.reshape(x_test,[-1, image_size, image_size])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
StopWatch.stop("data-pre-process")

input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2
```

## Define Model

```python
StopWatch.start("compile")
model = Sequential()
# LSTM Layers
model.add(LSTM(units=units,                      
                     input_shape=input_shape,
                     return_sequences=True))
model.add(LSTM(units=units, 
                     dropout=dropout,                      
                     return_sequences=True))
model.add(LSTM(units=units, 
                     dropout=dropout,                      
                     return_sequences=False))
# MLP Layers
model.add(Dense(units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
# Softmax_layer
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='rnn-mnist.png', show_shapes=True)


model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
StopWatch.stop("compile")
```

```bash
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm (LSTM)                  (None, 28, 256)           291840    
_________________________________________________________________
lstm_1 (LSTM)                (None, 28, 256)           525312    
_________________________________________________________________
lstm_2 (LSTM)                (None, 256)               525312    
_________________________________________________________________
dense (Dense)                (None, 256)               65792     
_________________________________________________________________
activation (Activation)      (None, 256)               0         
_________________________________________________________________
dropout (Dropout)            (None, 256)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 256)               65792     
_________________________________________________________________
activation_1 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                2570      
_________________________________________________________________
activation_2 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,476,618
Trainable params: 1,476,618
Non-trainable params: 0
```

## Train

```python
StopWatch.start("train")
model.fit(x_train, y_train, epochs=30, batch_size=batch_size)
StopWatch.stop("train")
```

```bash
469/469 [==============================] - 378s 796ms/step - loss: 2.2689 - accuracy: 0.2075
```

## Test

```python
StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()
```

```bash
79/79 [==============================] - 1s 7ms/step - loss: 2.2275 - accuracy: 0.3120

Test accuracy: 31.2%

+---------------------+------------------------------------------------------------------+
| Attribute           | Value                                                            |
|---------------------+------------------------------------------------------------------|
| BUG_REPORT_URL      | "https://bugs.launchpad.net/ubuntu/"                             |
| DISTRIB_CODENAME    | bionic                                                           |
| DISTRIB_DESCRIPTION | "Ubuntu 18.04.5 LTS"                                             |
| DISTRIB_ID          | Ubuntu                                                           |
| DISTRIB_RELEASE     | 18.04                                                            |
| HOME_URL            | "https://www.ubuntu.com/"                                        |
| ID                  | ubuntu                                                           |
| ID_LIKE             | debian                                                           |
| NAME                | "Ubuntu"                                                         |
| PRETTY_NAME         | "Ubuntu 18.04.5 LTS"                                             |
| PRIVACY_POLICY_URL  | "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" |
| SUPPORT_URL         | "https://help.ubuntu.com/"                                       |
| UBUNTU_CODENAME     | bionic                                                           |
| VERSION             | "18.04.5 LTS (Bionic Beaver)"                                    |
| VERSION_CODENAME    | bionic                                                           |
| VERSION_ID          | "18.04"                                                          |
| cpu_count           | 2                                                                |
| mem.active          | 1.9 GiB                                                          |
| mem.available       | 10.7 GiB                                                         |
| mem.free            | 7.3 GiB                                                          |
| mem.inactive        | 3.0 GiB                                                          |
| mem.percent         | 15.6 %                                                           |
| mem.total           | 12.7 GiB                                                         |
| mem.used            | 2.3 GiB                                                          |
| platform.version    | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| python              | 3.6.9 (default, Oct  8 2020, 12:12:24)                           |
|                     | [GCC 8.4.0]                                                      |
| python.pip          | 19.3.1                                                           |
| python.version      | 3.6.9                                                            |
| sys.platform        | linux                                                            |
| uname.machine       | x86_64                                                           |
| uname.node          | 9810ccb69d08                                                     |
| uname.processor     | x86_64                                                           |
| uname.release       | 4.19.112+                                                        |
| uname.system        | Linux                                                            |
| uname.version       | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| user                | collab                                                           |
+---------------------+------------------------------------------------------------------+

+------------------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |   Time |    Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |  0.61  |  0.61  | 2021-02-21 21:35:06 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |  0.076 |  0.076 | 2021-02-21 21:35:07 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |  6.445 |  6.445 | 2021-02-21 21:35:07 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 17.171 | 17.171 | 2021-02-21 21:35:13 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |  1.442 |  1.442 | 2021-02-21 21:35:31 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+

# csv,timer,status,time,sum,start,tag,uname.node,user,uname.system,platform.version
# csv,data-load,failed,0.61,0.61,2021-02-21 21:35:06,,9810ccb69d08,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,data-pre-process,failed,0.076,0.076,2021-02-21 21:35:07,,9810ccb69d08,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,compile,failed,6.445,6.445,2021-02-21 21:35:07,,9810ccb69d08,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,train,failed,17.171,17.171,2021-02-21 21:35:13,,9810ccb69d08,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,evaluate,failed,1.442,1.442,2021-02-21 21:35:31,,9810ccb69d08,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
```

### Reference: 

[Orignal Source to Source Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
