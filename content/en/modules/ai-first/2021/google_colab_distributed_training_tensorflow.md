---
title: Distributed Training for MNIST
draft: false
weight: 21
description: >
  Distributed Training for MNIST
---


<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_distributed_training.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_distributed_training.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
    <td><a href="https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_with_distributed_training.ipynb" download><img src="https://www.tensorflow.org/images/download_logo_32px.png" alt=""/></a> Download Notebook</td>    
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

Here we use the Tensorflow distributed training components to train the model in multiple CPUs or GPUs. 
In the Colab instance multiple GPUs are not supported. 
Hence, the training must be done in the device type 'None' when selecting the 'runtime type' from Runtime menu. 
To run with multiple-GPUs no code change is required. 
[Learn more about distributed training](https://www.tensorflow.org/guide/distributed_training).

```python
StopWatch.start("compile")
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
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
  
  print("Number of devices: {}".format(strategy.num_replicas_in_sync))

  model.compile(loss='categorical_crossentropy',
                optimizer='sgd',
                metrics=['accuracy'])
StopWatch.stop("compile")
```

```bash
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_6 (LSTM)                (None, 28, 256)           291840    
_________________________________________________________________
lstm_7 (LSTM)                (None, 28, 256)           525312    
_________________________________________________________________
lstm_8 (LSTM)                (None, 256)               525312    
_________________________________________________________________
dense_6 (Dense)              (None, 256)               65792     
_________________________________________________________________
activation_6 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_4 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_7 (Dense)              (None, 256)               65792     
_________________________________________________________________
activation_7 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_5 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_8 (Dense)              (None, 10)                2570      
_________________________________________________________________
activation_8 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,476,618
Trainable params: 1,476,618
Non-trainable params: 0
_________________________________________________________________
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:GPU:0',)
Number of devices: 1
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
```

## Train

```python
StopWatch.start("train")
model.fit(x_train, y_train, epochs=30, batch_size=batch_size)
StopWatch.stop("train")
```

```bash
Epoch 1/30
469/469 [==============================] - 7s 16ms/step - loss: 2.0427 - accuracy: 0.2718
Epoch 2/30
469/469 [==============================] - 7s 16ms/step - loss: 1.6934 - accuracy: 0.4007
Epoch 3/30
469/469 [==============================] - 7s 16ms/step - loss: 1.2997 - accuracy: 0.5497
...
Epoch 28/30
469/469 [==============================] - 8s 17ms/step - loss: 0.1175 - accuracy: 0.9640
Epoch 29/30
469/469 [==============================] - 8s 17ms/step - loss: 0.1158 - accuracy: 0.9645
Epoch 30/30
469/469 [==============================] - 8s 17ms/step - loss: 0.1098 - accuracy: 0.9661
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
79/79 [==============================] - 3s 9ms/step - loss: 0.0898 - accuracy: 0.9719

Test accuracy: 97.2%

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
| mem.active          | 2.4 GiB                                                          |
| mem.available       | 10.3 GiB                                                         |
| mem.free            | 4.5 GiB                                                          |
| mem.inactive        | 5.4 GiB                                                          |
| mem.percent         | 18.6 %                                                           |
| mem.total           | 12.7 GiB                                                         |
| mem.used            | 3.3 GiB                                                          |
| platform.version    | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| python              | 3.7.10 (default, Feb 20 2021, 21:17:23)                          |
|                     | [GCC 7.5.0]                                                      |
| python.pip          | 19.3.1                                                           |
| python.version      | 3.7.10                                                           |
| sys.platform        | linux                                                            |
| uname.machine       | x86_64                                                           |
| uname.node          | b39e0899c1f8                                                     |
| uname.processor     | x86_64                                                           |
| uname.release       | 4.19.112+                                                        |
| uname.system        | Linux                                                            |
| uname.version       | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| user                | collab                                                           |
+---------------------+------------------------------------------------------------------+

+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |    Time |     Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |   0.473 |   0.473 | 2021-03-07 11:34:03 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |   0.073 |   0.073 | 2021-03-07 11:34:03 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |   0.876 |   7.187 | 2021-03-07 11:38:05 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 229.341 | 257.023 | 2021-03-07 11:38:44 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |   2.659 |   4.25  | 2021-03-07 11:44:54 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+

# csv,timer,status,time,sum,start,tag,uname.node,user,uname.system,platform.version
# csv,data-load,failed,0.473,0.473,2021-03-07 11:34:03,,b39e0899c1f8,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,data-pre-process,failed,0.073,0.073,2021-03-07 11:34:03,,b39e0899c1f8,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,compile,failed,0.876,7.187,2021-03-07 11:38:05,,b39e0899c1f8,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,train,failed,229.341,257.023,2021-03-07 11:38:44,,b39e0899c1f8,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,evaluate,failed,2.659,4.25,2021-03-07 11:44:54,,b39e0899c1f8,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
```

### Reference: 

1. [Advance Deep Learning with Keras](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
2. [Distributed With Tensorflow](https://www.tensorflow.org/guide/distributed_training)
3. [Keras with Tensorflow Distributed Training](https://keras.io/guides/distributed_training/)
