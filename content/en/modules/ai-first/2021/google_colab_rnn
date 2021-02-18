---
title: MNIST-RMM Classification on Google Colab
draft: false
weight: 21
description: >
  MNIST with Recurrent Neural Networks: Classification on Google Colab
---


<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_rnn.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_rnn.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
    <td><a href="https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_rnn.ipynb" download><img src="https://www.tensorflow.org/images/download_logo_32px.png" alt=""/></a> Download Notebook</td>    
  </tr>
</table>  
</div>


## Prerequisites

Install the following packages

```python
! pip3 install cloudmesh-installer
! pip3 install cloudmesh-common
```

## Import Libraries

```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, SimpleRNN
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
model.add(SimpleRNN(units=units,
                    dropout=dropout,
                    input_shape=input_shape, return_sequences=True))
model.add(SimpleRNN(units=units,
                    dropout=dropout,
                    return_sequences=True))
model.add(SimpleRNN(units=units,
                    dropout=dropout,
                    return_sequences=False))
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
simple_rnn (SimpleRNN)       (None, 28, 256)           72960     
_________________________________________________________________
simple_rnn_1 (SimpleRNN)     (None, 28, 256)           131328    
_________________________________________________________________
simple_rnn_2 (SimpleRNN)     (None, 256)               131328    
_________________________________________________________________
dense (Dense)                (None, 10)                2570      
_________________________________________________________________
activation (Activation)      (None, 10)                0         
=================================================================
Total params: 338,186
Trainable params: 338,186
Non-trainable params: 0
```

## Train

```python
StopWatch.start("train")
model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
StopWatch.stop("train")
```

```bash
469/469 [==============================] - 125s 266ms/step - loss: 0.6794 - accuracy: 0.7783

<tensorflow.python.keras.callbacks.History at 0x7f35d4b104e0>
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
79/79 [==============================] - 7s 80ms/step - loss: 0.2581 - accuracy: 0.9181

Test accuracy: 91.8%

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
| mem.active          | 1.3 GiB                                                          |
| mem.available       | 11.6 GiB                                                         |
| mem.free            | 9.7 GiB                                                          |
| mem.inactive        | 1.5 GiB                                                          |
| mem.percent         | 8.5 %                                                            |
| mem.total           | 12.7 GiB                                                         |
| mem.used            | 978.6 MiB                                                        |
| platform.version    | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| python              | 3.6.9 (default, Oct  8 2020, 12:12:24)                           |
|                     | [GCC 8.4.0]                                                      |
| python.pip          | 19.3.1                                                           |
| python.version      | 3.6.9                                                            |
| sys.platform        | linux                                                            |
| uname.machine       | x86_64                                                           |
| uname.node          | 8f16b3b1f784                                                     |
| uname.processor     | x86_64                                                           |
| uname.release       | 4.19.112+                                                        |
| uname.system        | Linux                                                            |
| uname.version       | #1 SMP Thu Jul 23 08:00:38 PDT 2020                              |
| user                | collab                                                           |
+---------------------+------------------------------------------------------------------+

+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |    Time |     Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |   0.36  |   0.36  | 2021-02-18 15:16:12 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |   0.086 |   0.086 | 2021-02-18 15:16:12 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |   0.51  |   0.51  | 2021-02-18 15:16:12 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 126.612 | 126.612 | 2021-02-18 15:16:13 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |   6.798 |   6.798 | 2021-02-18 15:18:19 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+

# csv,timer,status,time,sum,start,tag,uname.node,user,uname.system,platform.version
# csv,data-load,failed,0.36,0.36,2021-02-18 15:16:12,,8f16b3b1f784,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,data-pre-process,failed,0.086,0.086,2021-02-18 15:16:12,,8f16b3b1f784,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,compile,failed,0.51,0.51,2021-02-18 15:16:12,,8f16b3b1f784,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,train,failed,126.612,126.612,2021-02-18 15:16:13,,8f16b3b1f784,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020
# csv,evaluate,failed,6.798,6.798,2021-02-18 15:18:19,,8f16b3b1f784,collab,Linux,#1 SMP Thu Jul 23 08:00:38 PDT 2020


```
