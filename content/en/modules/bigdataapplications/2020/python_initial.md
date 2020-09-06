## Python Warm Up

In this exercise, we will take a look at some basic Python Concepts needed for
day-to-day coding. 

Check the installed Python version.


```python
! python --version
```

    Python 3.7.6


## Simple For Loop


```python
for i in range(10):
  print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9


## List


```python
list_items = ['a', 'b', 'c', 'd', 'e']
```

### Retrieving an Element


```python
list_items[2]
```




    'c'



### Append New Values


```python
list_items.append('f')
```


```python
list_items
```




    ['a', 'b', 'c', 'd', 'e', 'f']



### Remove an Element


```python
list_items.remove('a')
```


```python
list_items
```




    ['b', 'c', 'd', 'e', 'f']



## Dictionary


```python
dictionary_items = {'a':1, 'b': 2, 'c': 3}
```

### Retrieving an Item by Key


```python
dictionary_items['b']
```




    2



### Append New Item with Key


```python
dictionary_items['c'] = 4
```


```python
dictionary_items
```




    {'a': 1, 'b': 2, 'c': 4}



### Delete an Item with Key


```python
del dictionary_items['a'] 
```


```python
dictionary_items
```




    {'b': 2, 'c': 4}




```python

```

## Comparators


```python
x = 10
y = 20 
z = 30
```


```python
x > y 
```




    False




```python
x < z
```




    True




```python
z == x
```




    False




```python
if x < z:
  print("This is True")
```

    This is True



```python
if x > z:
  print("This is True")
else:
  print("This is False")  
```

    This is False


## Arithmetic


```python
k = x * y * z
k
```




    6000




```python
j = x + y + z
j
```




    60




```python
m = x -y 
m
```




    -10






```python
n = x / z
n
```




    0.3333333333333333



## Numpy

### Create a Random Numpy Array 


```python
import numpy as np
```


```python
a = np.random.rand(100)
a.shape
```




    (100,)



### Reshape Numpy Array


```python
b = a.reshape(10,10)
b.shape
```




    (10, 10)



b[0]

### Manipulate Array Elements


```python
c = b * 10
c[0]
```




    array([3.33575458, 7.39029235, 5.54086921, 9.88592471, 4.9246252 ,
           1.76107178, 3.5817523 , 3.74828708, 3.57490794, 6.55752319])




```python

```
