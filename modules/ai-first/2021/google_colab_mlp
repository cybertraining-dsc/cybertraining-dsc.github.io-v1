---
title: MNIST-MLP Classification on Google Colab
draft: false
weight: 21
description: >
  MNIST-MLP Classification on Google Colab
---


<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mlp_mnist.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mlp_mnist.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
    <td><a href="https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mlp_mnist.ipynb" download><img src="https://www.tensorflow.org/images/download_logo_32px.png" alt=""/></a> Download Notebook</td>    
  </tr>
</table>  
</div>

In this lesson we discuss in how to create a simple IPython Notebook to solve
an image classification problem with Multi Layer Perceptron. 

## Pre-requisites

Install the following Python packages

1. cloudmesh-installer
2. cloudmesh-common

```bash
pip3 install cloudmesh-installer
pip3 install cloudmesh-common
```

## Sample MLP with Tensorflow Keras

```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time 

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
#import pydotplus
from keras.utils.vis_utils import model_to_dot
#from keras.utils.vis_utils import pydot


from cloudmesh.common.StopWatch import StopWatch

StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")

num_labels = len(np.unique(y_train))


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


image_size = x_train.shape[1]
input_size = image_size * image_size


x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

batch_size = 128
hidden_units = 512
dropout = 0.45

model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='mlp-mnist.png', show_shapes=True)

StopWatch.start("compile")
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
StopWatch.stop("compile")
StopWatch.start("train")
model.fit(x_train, y_train, epochs=5, batch_size=batch_size)
StopWatch.stop("train")

StopWatch.start("test")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("test")

StopWatch.benchmark()
```

```bash
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11493376/11490434 [==============================] - 0s 0us/step
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 512)               401920    
_________________________________________________________________
activation (Activation)      (None, 512)               0         
_________________________________________________________________
dropout (Dropout)            (None, 512)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_1 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_3 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_4 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_4 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,195,018
Trainable params: 1,195,018
Non-trainable params: 0
_________________________________________________________________
Epoch 1/5
469/469 [==============================] - 14s 29ms/step - loss: 0.7886 - accuracy: 0.7334
Epoch 2/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1981 - accuracy: 0.9433
Epoch 3/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1546 - accuracy: 0.9572
Epoch 4/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1302 - accuracy: 0.9641
Epoch 5/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1168 - accuracy: 0.9663
79/79 [==============================] - 1s 9ms/step - loss: 0.0785 - accuracy: 0.9765

Test accuracy: 97.6%

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
| mem.active          | 1.2 GiB                                                          |
| mem.available       | 11.6 GiB                                                         |
| mem.free            | 9.8 GiB                                                          |
| mem.inactive        | 1.4 GiB                                                          |
| mem.percent         | 8.4 %                                                            |
| mem.total           | 12.7 GiB                                                         |
| mem.used            | 913.7 MiB                                                        |
| platform.version    | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| python              | 3.6.9 (default, Oct  8 2020, 12:12:24)                           |
|                     | [GCC 8.4.0]                                                      |
| python.pip          | 19.3.1                                                           |
| python.version      | 3.6.9                                                            |
| sys.platform        | linux                                                            |
| uname.machine       | x86_64                                                           |
| uname.node          | 6609095905d1                                                     |
| uname.processor     | x86_64                                                           |
| uname.release       | 4.19.112+                                                        |
| uname.system        | Linux                                                            |
| uname.version       | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| user                | collab                                                           |
+---------------------+------------------------------------------------------------------+

+-----------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name      | Status   |   Time |    Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|-----------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load | failed   |  0.549 |  0.549 | 2021-02-15 15:24:00 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile   | failed   |  0.023 |  0.023 | 2021-02-15 15:24:01 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train     | failed   | 69.1   | 69.1   | 2021-02-15 15:24:01 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| test      | failed   |  0.907 |  0.907 | 2021-02-15 15:25:10 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+-----------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+

# csv,timer,status,time,sum,start,tag,uname.node,user,uname.system,platform.version
# csv,data-load,failed,0.549,0.549,2021-02-15 15:24:00,,6609095905d1,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,compile,failed,0.023,0.023,2021-02-15 15:24:01,,6609095905d1,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,train,failed,69.1,69.1,2021-02-15 15:24:01,,6609095905d1,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,test,failed,0.907,0.907,2021-02-15 15:25:10,,6609095905d1,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
```

### Reference: 

[Orignal Source to Source Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
