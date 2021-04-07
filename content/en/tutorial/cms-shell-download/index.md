---
date: 2021-04-07
title: "Using Shell.download to Download Files"
linkTitle: "Downloading files with cms"
description: "Using Shell to download files that can be potentially very large in python."
author: Richard Otten ([ottenrichie@gmail.com](mailto:ottenrichie@gmail.com)), Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---

{{< imgproc image Fill "600x300" >}}
{{< /imgproc >}}


{{% pageinfo %}}

**Learning Objectives**

* Install `cloudmesh.common`
* Use `Shell.download` from `cloudmesh-common` to download files from the internet.

**Requirements**

* `python3 --version` > 3.8

**Topics covered**

{{% table_of_contents %}}

{{% /pageinfo %}}


## Python 3 `venv`

Best practice is to use a venv in python to isolate your custom python instalation:

```bash
$ python3 -m venv ~/ENV3
$ source ~/ENV3/bin/activate 
```

or

```bash
$ ~/ENV3/Scripts/activate.exe
```

in Windows `gitbash`.

## Installation of `cloudmesh.commn`


Install `cloudmesh-common` with:

```bash
pip install -U pip
pip install cloudmesh-common
```

## Usage of `Shell.download`

`Shell.download` leverages the streaming capabilities of the `requests` library for large files.

Example download of image where underlying downloader is `requests`:

```python
$ python3
Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> from cloudmesh.common.Shell import Shell
>>> file_url = 'https://github.com/cloudmesh/pi/blob/main/content/en/tutorial/example/featured-image.png?raw=true'
>>> destination = '~/Desktop/image.png'
>>> Shell.download(file_url, destination)
/users/you/Desktop/image.png: 100%|#########| 22.6k/22.6k [00:00<00:00, 3.58MB/s]
'/users/you/Desktop/image.png'
```

## Configuring the Download Cache

`Shell.download` only downloads if the filename in the destination does not 
already exist. If you like to change the behavior and ignore it, you need to use 
the `force` parameter.

```python
Shell.download(file_url, destination, force=True)
```


## Different Providers for `Shell.download`

Example where provider is `system`. Cloudmesh `Shell` will first try to use 
`wget` then `curl` (if `wget` fails)

```python
$ python3
Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> from cloudmesh.common.Shell import Shell
>>> file_url = 'https://github.com/cloudmesh/pi/blob/main/content/en/tutorial/example/featured-image.png?raw=true'
>>> destination = '~/Desktop/image.png'
>>> Shell.download(file_url, destination, provider='system')
sh: wget: command not found
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   153  100   153    0     0    467      0 --:--:-- --:--:-- --:--:--   467
100   164  100   164    0     0    379      0 --:--:-- --:--:-- --:--:--   379
100 22590  100 22590    0     0  43694      0 --:--:-- --:--:-- --:--:-- 43694
INFO: Used curl
'/users/you/Desktop/image.png'
>>>
```

We can see here that `Shell.download` uses `curl` and not `wget`. This is 
because the example system did not have `wget` as a
terminal (`'system'`) command installed.

## Installing other Download Programs

Your OS typically has defined mechanisms to install commands such as `curl` and `wget`.
If they are not installed. Shell.download will use Python requests automatically.
If you like to use wget r curl you need to install them.

On Ubuntu you can fro example say 

```bash
$ sudo apt install wget
```

or 

```bash
$ sudo apt install curl
```

Please find the method that works for your system, or use the default method 
which does not require a third party provider.

The order of the providers is defined as 

1. wget 
2. curl
3. Python requests

We use wget and curl first as many OS have optimized versions of them.