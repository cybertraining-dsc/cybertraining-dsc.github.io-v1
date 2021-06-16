---
date: 2021-02-07
> title: "Monnitoring your Nvidia GPUs on Ubuntu"
description: "We present a number of simple to use monitoring tools to inspect your GPUs on your computer."
author: Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
---


## 1. Introduction

So you have installed your long awaited graphics card from NVIDIA and like to observe its utilization. You may be familiar with nvidia-smi, but there is more to this tool as you may know. We will provid you with som examples on what you can do with it. Furtheremore, we will show case a number of tools that allow you to monitor the Crad(s) as they provide more sophisticated visuzlisations. We present graphics and terminal commands. The reason why terminal commands are so popular is that theu can be called in containers, but also through simple remote shell invocations where it may be inconvenient to use a GUI.

## 2. Preface

* **Notation:** We use in the document some comamnds issued on the terminal, teminal commands are preceeded by a '$' as to easily distinguish them from other text.
* **Operating system:** We restricted this review on tools that are available on Ubuntu as this is what we use to interact with the cards. Several tools also exist for windows, but this may be a topic for another day.

## 3. Python3 venv

Some of the tools come as python packages and in order not to effect your default python instalaation we recommend to use a python virtual environment. Create and source it and you should be ready to go after you execute the following commands:

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

After you installed the nvidia drivers and programs you will finr a program called `nvidia-smi`. You simply can call it with 

```
$ nvidia-smi
```

giving you the current status of the cards. To get a repeated update you can use the command 

```
$ nvidia-smi -l 1
```

where the parameter after the -l specifies the time in seconds between updates. However it to avoid past traces to be showing up in your comand histtory, you can als use 

```
$ watch -n 1 nvidia-smi
```

which we prefer. Unkown to some users I spoke to they did not know that this command comes with a lot of features you can access from the commandline to customize your query. To find out more about it use the commands

```
$ nvidia-smi --help-query-compute-app
```

and 

```
$ nvidia-smi --help
```

to get inspired. Here is for example a command that returns the content of a specific query of selected attributes in csv format for further processing 


```
$ nvidia-smi --query-compute-apps=pid,process_name,used_memory --format=csv
```



### 4.2 nvgpu

[nvgpu](https://pypi.org/project/nvgpu/)

### 4.3 GreenWithEnvy

[GreenWithEnvy](https://flathub.org/apps/details/com.leinardi.gwe)
[Code on GitLab](https://gitlab.com/leinardi/gwe)

### 4.4 nvtop

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
