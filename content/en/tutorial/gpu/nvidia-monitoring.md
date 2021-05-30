---
date: 2021-02-07
title: "10 minus 5 Monnitoring your Nvidia GPUs on Ubuntu 20.04 LTS"
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

Although we started with the hope that all of them are easy to
install, we found out that only five of the 10 did install without
issues. We found especially lack of documentation on the other tools
to make them work. Naturally we have other things to do as likely you,
so we did not spend any time in trying to fix the things. INstead we
moved on and looked at other tools that are easier to install and work
instead.

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
$nvidia-smi --query-gpu=timestamp,temperature.gpu --format=csv
timestamp, temperature.gpu
2021/05/30 10:39:37.436, 26
```

```
$ nvidia-smi --query-gpu=name,index,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv,noheader,nounits
GeForce RTX 3090, 0, 30, 0, 0, 24234, 23512, 722
```

### 4.2 gpustat

[gpustat](https://github.com/wookayin/gpustat) is a minimal terminal command that lists a subset of nvidia-smi.

It is easily installable with

```
$ pip install gpustat
```

you can call it repeatdly with 

```
gpustat -cp --watch
```

or

```
watch -n 1 -c gpustat -cp --color
```

To see more options use

```
gpustat -h
```



### 4.3 nvtop

[nvtop](https://github.com/Syllo/nvtop) is a top like task monitor for NVIDIA GPUs. It can handle multiple GPUs.

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

The putput looks like

![Figure: Nvtop Screenshot](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/raw/main/content/en/tutorial/gpu/nvtop.png)

Figure: Nvtop Screenshot

### 4.4 gmonitor

[gmonitor](https://github.com/mountassir/gmonitor) is a simple GPU monitoring program for monitoring core usage, VRAM usage, PCI-E and memory bus usage, and the temperature of the GPU. 

It is easy to install with

```
clone https://github.com/mountassir/gmonitor.git
cd gmonitor/
mkdir build
cd build
cmake ..
make
sudo make install
```

you start it with 

```
gmonitor
```						   

It looks as shown in the next figure.

![Figure: gmonitor](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/raw/main/content/en/tutorial/gpu/gmonitor.png)

Figure: gmonitor



### 4.5 glances

[Glances](https://nicolargo.github.io/glances/) is a op like tool that reports on many different aspects of the system and not just GPUs. The tool is easy to install with 

```
pip install py3nvml
sudo pip install glances[gpu]
```

You can star tit with

```
$ glances
```

However if you use a white background use

```
$ glances --theme-white
```




### 4.6 Install Issues: nvidia-system-monitor

As we have not installed qt we were suspisious about if this install
woudl even work. Unfortunately the documentation does not provide
enough information on how to install qt. and make it work. The Web
page for the tool is located at

[nvidia-system-monitor](https://github.com/congard/nvidia-system-monitor-qt)


It seems to be complex to install qt for free on a system, thus we
have not followed up on this any further.


### 4.2 Install Issues: nvgpu

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



### 4.5 Install Issues: nvitop

[nvitop](https://github.com/XuehaiPan/nvitop) is Aa interactive
NVIDIA-GPU process viewer, the one-stop solution for GPU process
management. HOwever it is not installable on my system via pip
install, not via compilation from source.

The information on the Web site on how to fix the dependency on
`nvidia-ml-py==11.450.51` and how to fix it could be better described


### 4.3 Install Issues: GreenWithEnvy

[GreenWithEnvy](https://flathub.org/apps/details/com.leinardi.gwe) is
a great looking application, however also its install is not possible
on my system as it fails with an install issue of pycairo. The ode is
available on [GitLab](https://gitlab.com/leinardi/gwe)


### 4.9 Install Issues: pgme

The tool [pgme](https://github.com/chhibber/pgme) could not be
installed on Linux as its instructins wer incomplete and did not work
even after instalation of go with


```
sudo snap install go --classic
```

## Conclusion

We have shown you a number of tools for monitoring your GPUs. We found
that these tools are incredible useful to make sure you system
operates properly. This is espacially the case for showing workloads
and temperatures, as well as the available software versions to
interact with the cards.

Which one of the tools you like may be a personal choice. Although
`nvidia-smi` is the go-to tool, others provide quite good insights
while visualizing historical trends enahncing the experience when you
for example run workloads over time.

Please leave us a note about which tools you prefer and let us know
about tools that we have not listed here. Make sure they can easily be
installed.

