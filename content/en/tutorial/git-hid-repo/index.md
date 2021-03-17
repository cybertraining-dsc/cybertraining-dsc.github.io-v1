---
date: 2021-03-15
title: "GitHub hid Repository"
linkTitle: "Git hid repo"
description: "Using the student hid directory"
author: Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---


{{< imgproc image Fill "600x300" >}}
{{< /imgproc >}}

Figure 1: GitHub hid directory.


{{% pageinfo %}}

GitHub provides an extended gh commandline tool that allow easy interaction of 
forking repositories directly from github. IT also provides additional fimctionality 
to interact with other advanced features that are typically not provided in the git command tool.

**Learning Objectives**

* Learn how to cone the repo
* Learn how to use the rego
* Learn how to commit and push changes to GitHub

  
**Topics covered**

{{% table_of_contents %}}

{{% /pageinfo %}}

## 1. Introduction

As part of our open source activities you will be given a GitHub repositorry 

```bash
ssh-keygen
````


```bash
export HID=hit-example
export EDITOR=emacs
````

```bash
git clone ghgit@github.com:cybertraining-dsc/$HID.git
cd $HID/project
$EDITOR index.md
```

Make modifications

```bash
git commit -m "Improved document with this and that" index.md
```

To add new files do 

```bash
git add image/newimage.png
git commit -m "Improved document with this and that" image/newimage.png
```

Push modifications to the repo on GitHub

```bash
git push
```

## 7. Conclusion
