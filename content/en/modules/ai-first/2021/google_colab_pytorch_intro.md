---
title: MNIST With PyTorch
draft: false
weight: 21
description: >
  MNIST With PyTorch
---


<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_pytorch.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_pytorch.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
    <td><a href="https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_with_pytorch.ipynb" download><img src="https://www.tensorflow.org/images/download_logo_32px.png" alt=""/></a> Download Notebook</td>    
  </tr>
</table>  
</div>

In this lesson we discuss in how to create a simple IPython Notebook to solve
an image classification problem with Multi Layer Perceptron with PyTorch. 


## Import Libraries

```python
import numpy as np
import torch
import torchvision
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch import nn
from torch import optim
from time import time
import os
from google.colab import drive
```

## Pre-Process Data

Here we download the data using PyTorch data utils and transform the data by using a normalization function. 
PyTorch provides a data loader abstraction called a `DataLoader` where we can set the batch size, data shuffle per batch loading. 
Each data loader expecte a Pytorch Dataset.
The DataSet abstraction and DataLoader usage can be found [here](https://pytorch.org/tutorials/recipes/recipes/loading_data_recipe.html) 

```python
# Data transformation function 
transform = transforms.Compose([transforms.ToTensor(),
                              transforms.Normalize((0.5,), (0.5,)),
                              ])

# DataSet
train_data_set = datasets.MNIST('drive/My Drive/mnist/data/', download=True, train=True, transform=transform)
validation_data_set = datasets.MNIST('drive/My Drive/mnist/data/', download=True, train=False, transform=transform)

# DataLoader
train_loader = torch.utils.data.DataLoader(train_data_set, batch_size=32, shuffle=True)
validation_loader = torch.utils.data.DataLoader(validation_data_set, batch_size=32, shuffle=True)
```

## Define Network

Here we select the matching input size compared to the network definition. 
Here data reshaping or layer reshaping must be done to match input data shape with the network input shape. 
Also we define a set of hidden unit sizes along with the output layers size. 
The `output_size` must match with the number of labels associated with the classification problem. 
The hidden units can be chosesn depending on the problem. `nn.Sequential` is one way to create the network. 
Here we stack a set of linear layers along with a softmax layer for the classification as the output layer. 


```python
input_size = 784
hidden_sizes = [128, 128, 64, 64]
output_size = 10

model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[1], hidden_sizes[2]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[2], hidden_sizes[3]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[3], output_size),
                      nn.LogSoftmax(dim=1))

                      
print(model)
```

```bash
Sequential(
  (0): Linear(in_features=784, out_features=128, bias=True)
  (1): ReLU()
  (2): Linear(in_features=128, out_features=128, bias=True)
  (3): ReLU()
  (4): Linear(in_features=128, out_features=64, bias=True)
  (5): ReLU()
  (6): Linear(in_features=64, out_features=64, bias=True)
  (7): ReLU()
  (8): Linear(in_features=64, out_features=10, bias=True)
  (9): LogSoftmax(dim=1)
)
```

## Define Loss Function and Optimizer

Read more about [Loss Functions](https://pytorch.org/docs/stable/nn.html#loss-functions) and [Optimizers](https://pytorch.org/docs/stable/optim.html) 
supported by PyTorch.



```python
criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.9)
```

## Train

```python
epochs = 5

for epoch in range(epochs):
    loss_per_epoch = 0
    for images, labels in train_loader:
        images = images.view(images.shape[0], -1)
    
        # Gradients cleared per batch
        optimizer.zero_grad()
        
        # Pass input to the model
        output = model(images)
        # Calculate loss after training compared to labels
        loss = criterion(output, labels)
        
        # backpropagation 
        loss.backward()
        
        # optimizer step to update the weights
        optimizer.step()
        
        loss_per_epoch += loss.item()
    average_loss = loss_per_epoch / len(train_loader)
    print("Epoch {} - Training loss: {}".format(epoch, average_loss))
```

```bash
Epoch 0 - Training loss: 1.3052690227402808
Epoch 1 - Training loss: 0.33809808635317695
Epoch 2 - Training loss: 0.22927882223685922
Epoch 3 - Training loss: 0.16807103878669521
Epoch 4 - Training loss: 0.1369301250545995
```

## Model Evaluation

Similar to training data loader, we use the validation loader to load batch by batch and run the feed-forward network to 
get the expected prediction and compared to the label associated with the data point. 

```python
correct_predictions, all_count = 0, 0
# enumerate data from the data validation loader (loads a batch at a time)
for batch_id, (images,labels) in enumerate(validation_loader):
  for i in range(len(labels)):
    img = images[i].view(1, 784)
    # at prediction stage, only feed-forward calculation is required. 
    with torch.no_grad():
        logps = model(img)

    # Output layer of the network uses a LogSoftMax layer
    # Hence the probability must be calculated with the exponential values. 
    # The final layer returns an array of probabilities for each label
    # Pick the maximum probability and the corresponding index
    # The corresponding index is the predicted label 
    ps = torch.exp(logps)
    probab = list(ps.numpy()[0])
    pred_label = probab.index(max(probab))
    true_label = labels.numpy()[i]
    if(true_label == pred_label):
      correct_predictions += 1
    all_count += 1

print(f"Model Accuracy {(correct_predictions/all_count) * 100} %")
```

```bash
Model Accuracy 95.95 %
```

### Reference: 

1. [Torch NN Sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html)
2. [Handwritten Digit Recognition Using PyTorch — Intro To Neural Networks](https://towardsdatascience.com/handwritten-digit-mnist-pytorch-977b5338e627)
3. [MNIST Handwritten Digit Recognition in PyTorch](https://nextjournal.com/gkoehler/pytorch-mnist)


