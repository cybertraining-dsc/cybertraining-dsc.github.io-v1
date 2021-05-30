---
date: 2021-02-07
title: "Monnitoring your Nvidia GPUs on Ubuntu"
description: "We present a number of simple to use monitoring tools to inspect your GPUs on your computer."
author: Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
---


## 1. Introduction

So you have installed your long awaited graphics card from NVIDIA and
like to observe its utilization. You may be familiar with nvidia-smi,
but there is more to this tool as you may know. We will provid you
with som examples on what you can do with it. Furtheremore, we will
show case a number of tools that allow you to monitor the Crad(s) as
they provide more sophisticated visuzlisations. We present graphics
and terminal commands. The reason why terminal commands are so popular
is that theu can be called in containers, but also through simple
remote shell invocations where it may be inconvenient to use a GUI.

## 2. Preface

* **Notation:** We use in the document some comamnds issued on the
    terminal, teminal commands are preceeded by a '$' as to easily
    distinguish them from other text.
* **Operating system:** We restricted this review on tools that are
    available on Ubuntu as this is what we use to interact with the
    cards. Several tools also exist for windows, but this may be a
    topic for another day.

## 3. Python3 venv

Some of the tools come as python packages and in order not to effect
your default python instalaation we recommend to use a python virtual
environment. We use in our virtual environment python 3.9. To do so
make sure you have python 3.9 installed, which you can optain in
varius ways.

Then create and source it and you should be ready to go after
you execute the following commands:

```
$ python3 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
$ pip install pip -U
```

To permanently add it to your startup, please add the line: 

```
source ~/ENV3/bin/activate
```

to your `.bash_profile` file


## 4. The tools to monitor your NVIDIA Cards


### 4.1 nvidia-smi

After you installed the nvidia drivers and programs you will finr a
program called `nvidia-smi`. You simply can call it with

```
$ nvidia-smi
```

This gives you the current status of the cards.

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.73.01    Driver Version: 460.73.01    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 3090    On   | 00000000:0B:00.0  On |                  N/A |
| 32%   27C    P8    15W / 350W |    618MiB / 24234MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1544      G   /usr/lib/xorg/Xorg                102MiB |
|    0   N/A  N/A      2663      G   /usr/lib/xorg/Xorg                387MiB |
|    0   N/A  N/A      2797      G   /usr/bin/gnome-shell               89MiB |
|    0   N/A  N/A      4866      G   /usr/lib/firefox/firefox            4MiB |
|    0   N/A  N/A      7884      G   /usr/lib/firefox/firefox            4MiB |
|    0   N/A  N/A      8939      G   /usr/lib/firefox/firefox            4MiB |
|    0   N/A  N/A     10674      G   /usr/lib/firefox/firefox            4MiB |
|    0   N/A  N/A     11148      G   /usr/lib/firefox/firefox            4MiB |
+-----------------------------------------------------------------------------+
```


To get a repeated update
you can use the command

```
$ nvidia-smi -l 1
```

where the parameter after the `-l` specifies the time in seconds between
updates. However it to avoid past traces to be showing up in your
comand histtory, you can als use

```
$ watch -n 1 nvidia-smi
```

which we prefer. Unkown to some users I spoke to they did not know
that this command comes with a lot of features you can access from the
commandline to customize your query. To find out more about it use the
commands

```
$ nvidia-smi --help-query-compute-apps
```

and 

```
$ nvidia-smi --help
```

to get inspired. Here is for example a command that returns the
content of a specific query of selected attributes in csv format for
further processing.

Examples are:

```
nvidia-smi --query-gpu=timestamp,temperature.gpu --format=csv
timestamp, temperature.gpu
2021/05/30 10:39:37.436, 26
```


```
$ nvidia-smi --query-compute-apps=timestamp,pid,gpu_name,process_name,used_gpu_memory --format=csv
```


### 4.3 GreenWithEnvy

[GreenWithEnvy](https://flathub.org/apps/details/com.leinardi.gwe)
[Code on GitLab](https://gitlab.com/leinardi/gwe)

### 4.4 nvtop

Nvtop could not be installed via pip intall as it uses an outdated nvidia library by default.
Hence it is best to install it from source as follows

```
$ git clone https://github.com/Syllo/nvtop.git
$ mkdir -p nvtop/build && cd nvtop/build
$ cmake ..
$ make
$ sudo make install
```

Now run it with

```
$ nvtop
```

[nvtop](https://github.com/Syllo/nvtop)

[review](https://www.linuxuprising.com/2019/06/2-tools-for-monitoring-nvidia-gpus-on.html)

### 4.5 nvitop

[nvitop](https://github.com/XuehaiPan/nvitop)

### 4.6 nvidia-system-monitor

Based on qt

[nvidia-system-monitor](https://github.com/congard/nvidia-system-monitor-qt)

### 4.7 gpustat

[gpustat](https://github.com/wookayin/gpustat)

gpustat -cp --watch

watch -n 0.5 -c gpustat -cp --color

### 4.8 glances

You can use the monitoring program glances with its GPU monitoring plug-in:

open source
to install: sudo apt-get install -y python-pip; sudo pip install glances[gpu]
to launch: sudo glances

### 4.9 prometheus

https://github.com/chhibber/pgme

### 4.10 gmonitor

https://github.com/mountassir/gmonitor

## Conclusion

We have shown you a number of tools for monitoring your GPUs. We found that these tools are incredible useful to make sure you system operates properly. This is espacially the case for showing workloads and temperatures, as well as the available software versions to interact with the cards.

Which one of the tools you like may be a personal choice. Although `nvidia-smi` is the go-to tool, others provide quite good insights while visualizing historical trends enahncing the experience when you for example run workloads over time.

Please leav us a note about which tools you prefer and let us know about tools that we have not listed here.

### 4.2 Install issues: nvgpu

The Web page is located at [Nvgpu](https://pypi.org/project/nvgpu/)

This module could not be easily installed even though we installed


```
sudo apt-get install liblzma-dev
sudo apt-get install liblzma
pip install -U nvgpu
nvgpu available
```

it returns

```
/home/USER/ENV3/lib/python3.9/site-packages/pandas/compat/__init__.py:97: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
```


