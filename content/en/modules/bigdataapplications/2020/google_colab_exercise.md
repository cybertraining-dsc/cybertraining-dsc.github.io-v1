---
title: Google Colab Exercise and Homework
draft: false
weight: 21
description: >
  MNIST Classification on Google Colab
---

# MNIST Classification on Google Colab


<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/google_colab_mnist_example.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/google_colab_mnist_example.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
    <td><a href="https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/google_colab_mnist_example.ipynb" download><img src="https://www.tensorflow.org/images/download_logo_32px.png" alt=""/></a> Download Notebook</td>    
  </tr>
</table>  
</div>

In this lesson we discuss in how to create a simple IPython Notebook to solve
an image classification problem. MNIST contains a set of pictures


## Import Libraries 

Note: https://python-future.org/quickstart.html


```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
```

## Warm Up Exercise

## Pre-process data

### Load data 

First we load the data from the inbuilt mnist dataset from Keras
Here we have to split the data set into training and testing data. 
The training data or testing data has two components. 
Training features and training labels. 
For instance every sample in the dataset has a corresponding label. 
In Mnist the training sample contains image data represented in terms of 
an array. The training labels are from 0-9. 

Here we say x_train for training data features and y_train as the training labels. Same goes for testing data. 


```python
(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
    11493376/11490434 [==============================] - 0s 0us/step


### Identify Number of Classes

As this is a number classification problem. We need to know how many classes are there. 
So we'll count the number of unique labels. 


```python
num_labels = len(np.unique(y_train))
```

### Convert Labels To One-Hot Vector

Read more on one-hot vector. 


```python
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
```

## Image Reshaping

The training model is designed by considering the data as a vector.
This is a model dependent modification. Here we assume the image is
a squared shape image.


```python
image_size = x_train.shape[1]
input_size = image_size * image_size
```

## Resize and Normalize

The next step is to continue the reshaping to a fit into a vector
and normalize the data. Image values are from 0 - 255, so an 
easy way to normalize is to divide by the maximum value. 



```python
x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255
```

## Create a Keras Model

Keras is a neural network library. The summary function provides tabular summary on the model you created. And the plot_model function provides a grpah on the network you created. 


```python
# Create Model
# network parameters
batch_size = 4
hidden_units = 64

model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='mlp-mnist.png', show_shapes=True)
```

    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_5 (Dense)              (None, 512)               401920    
    _________________________________________________________________
    dense_6 (Dense)              (None, 10)                5130      
    _________________________________________________________________
    activation_5 (Activation)    (None, 10)                0         
    =================================================================
    Total params: 407,050
    Trainable params: 407,050
    Non-trainable params: 0
    _________________________________________________________________


![images](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/bigdataapplications/2020/images/deeplearning/lab1/output_20_1.png)

{{< youtube "UagrQBdrkjM" >}}

## Compile and Train

A keras model need to be compiled before it can be used to train
the model. In the compile function, you can provide the optimization
that you want to add, metrics you expect and the type of loss function
you need to use. 

Here we use adam optimizer, a famous optimizer used in neural networks. 

The loss funtion we have used is the categorical_crossentropy. 

Once the model is compiled, then the fit function is called upon passing the number of epochs, traing data and batch size. 

The batch size determines the number of elements used per minibatch in optimizing the function. 

**Note: Change the number of epochs, batch size and see what happens.**




```python
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
```

    469/469 [==============================] - 3s 7ms/step - loss: 0.3647 - accuracy: 0.8947





    <tensorflow.python.keras.callbacks.History at 0x7fe88faf4c50>



## Testing 

Now we can test the trained model. Use the evaluate function by passing
test data and batch size and the accuracy and the loss value can be retrieved.

**MNIST_V1.0|Exercise: Try to observe the network behavior by changing the number of epochs, batch size and record the best accuracy that you can gain. Here you can record what happens when you change these values. Describe your observations in 50-100 words.**



```python
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
```

    79/79 [==============================] - 0s 4ms/step - loss: 0.2984 - accuracy: 0.9148
    
    Test accuracy: 91.5%


## Final Note

This programme can be defined as a hello world programme in deep
learning. Objective of this exercise is not to teach you the depths of
deep learning. But to teach you basic concepts that may need to design a
simple network to solve a problem. Before running the whole code, read
all the instructions before a code section. 

## Homework

**Solve Exercise MNIST_V1.0.**

{{< youtube "lbCyefwZGlI" >}}

### Reference: 

[Orignal Source to Source Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
