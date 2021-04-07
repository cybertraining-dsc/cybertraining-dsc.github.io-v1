---
date: 2021-02-07
title: "Using Shell.download to Download Files"
linkTitle: "Downloading files with Shell"
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

* Use `Shell.download` from `cloudmesh-common` to download files (such as disk images) from the internet.

**Topics covered**

* Usage of `Shell.download`
* Underlying implementations for `Shell.download`

**Requirements**

* `python3 --version` > 3.8

{{% table_of_contents %}}

{{% /pageinfo %}}

## Basic Usage

Install `cloudmesh-common` with:

```
pip install -U pip
pip install cloudmesh-common
```

`Shell.download` leverages the streaming capabilities of the `requests` library for large files.

Example download of image where underlying downloader is `requests`:

```
$ python3
Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> from cloudmesh.common.Shell import Shell
>>> file_url = 'https://github.com/cloudmesh/pi/blob/main/content/en/tutorial/example/featured-image.png?raw=true'
>>> destination = '~/Desktop/image.png'
>>> Shell.download(file_url, destination)
/users/you/Desktop/image.png: 100%|###################################################################################| 22.6k/22.6k [00:00<00:00, 3.58MB/s]
'/users/you/Desktop/image.png'
>>>
```

Example where provider is `system`. Cloudmesh `Shell` will first try to use `wget` then `curl` (if `wget` fails)

```
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

We can see here that `Shell.download` uses `curl` and not `wget`. This is because the example system did not have `wget` as a
terminal (`'system'`) command.