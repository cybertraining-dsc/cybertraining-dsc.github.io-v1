---
title: Physics
draft: false
weight: 4
description: >
  Week 4: Big Data applications and Physics
---

## E534 2020 Big Data Applications and Analytics Discovery of Higgs Boson 

Summary: This section of the class is devoted to a particular Physics experiment but uses this to discuss so-called counting experiments. Here one observes “events” that occur randomly in time and one studies the properties of the events; in particular are the events collection of subatomic particles coming from the decay of particles from a “Higgs Boson” produced in high energy accelerator collisions. The four video lecture sets (Parts I II III IV) start by describing the LHC accelerator at CERN and evidence found by the experiments suggesting the existence of a Higgs Boson. The huge number of authors on a paper, remarks on histograms and Feynman diagrams is followed by an accelerator picture gallery. The next unit is devoted to Python experiments looking at histograms of Higgs Boson production with various forms of the shape of the signal and various backgrounds and with various event totals. Then random variables and some simple principles of statistics are introduced with an explanation as to why they are relevant to Physics counting experiments. The unit introduces Gaussian (normal) distributions and explains why they have seen so often in natural phenomena. Several Python illustrations are given. Random Numbers with their Generators and Seeds lead to a discussion of Binomial and Poisson Distribution. Monte-Carlo and accept-reject methods. The Central Limit Theorem concludes the discussion.

## Looking for Higgs Particle Part I : Bumps in Histograms, Experiments and Accelerators

This unit is devoted to Python and Java experiments looking at histograms of Higgs Boson production with various forms of the shape of the signal and various backgrounds and with various event totals. The lectures use Python but the use of Java is described. Students today can ignore Java!

[Slides](https://drive.google.com/file/d/1KxK2XKnjqqvQI9gjga7EYwcm_z0zZt-Z/view?usp=sharing) {20 slides}

### Looking for Higgs Particle and Counting Introduction 1

We return to the particle case with slides used in introduction and stress that particles often manifested as bumps in histograms and those bumps need to be large enough to stand out from the background in a statistically significant fashion.

Video: {{< syoutube "L0wIh0Z-ZwI" >}} {slides1-5} 

### Looking for Higgs Particle II Counting Introduction 2

We give a few details on one LHC experiment ATLAS. Experimental physics papers have a staggering number of authors and quite big budgets. Feynman diagrams describe processes in a fundamental fashion

Video: {{< syoutube "UAMzmOgjj7I" >}} {slides 6-8}

### Experimental Facilities 

We give a few details on one LHC experiment ATLAS. Experimental physics papers have a staggering number of authors and quite big budgets. Feynman diagrams describe processes in a fundamental fashion.

Video: {{< syoutube "BW12d780qT8" >}} {slides 9-14}

### Accelerator Picture Gallery of Big Science 

This lesson gives a small picture gallery of accelerators. Accelerators, detection chambers and magnets in tunnels and a large underground laboratory used for experiments where you need to be shielded from the background like cosmic rays.

{{< syoutube "WLJIxWWMYi8" >}} {slides 14-20}

### Resources
http://grids.ucs.indiana.edu/ptliupages/publications/Where%20does%20all%20the%20data%20come%20from%20v7.pdf 
http://www.sciencedirect.com/science/article/pii/S037026931200857X

http://www.nature.com/news/specials/lhc/interactive.html

## Looking for Higgs Particles Part II: Python Event Counting for Signal and Background

Python Event Counting for Signal and Background (Part 2) This unit is devoted to Python experiments looking at histograms of Higgs Boson production with various forms of the shape of the signal and various backgrounds and with various event totals.

[Slides](https://drive.google.com/file/d/1n3vu5LvW5WkD9Eaz57GUsG3wp4PbOxHs/view?usp=sharing) {1-29 slides}

### Class Software

We discuss Python on both a backend server (FutureGrid - closed!) or a local client. We point out a useful book on Python for data analysis. 

{{< syoutube "ulX3oIiAusI" >}} {slides 1-10}

Refer to **A: Studying Higgs Boson Analysis. Signal and Background, Part 1 The background** 

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Event Counting 

We define event counting of data collection environments. We discuss the python and Java code to generate events according to a particular scenario (the important idea of Monte Carlo data). Here a sloping background plus either a Higgs particle generated similarly to LHC observation or one observed with better resolution (smaller measurement error).

{{< syoutube "h8-szCeFugQ" >}} {slides 11-14}

### Examples of Event Counting I with Python Examples of Signal and Background

This uses Monte Carlo data both to generate data like the experimental observations and explore the effect of changing amount of data and changing measurement resolution for Higgs.

{{< syoutube "bl2f0tAzLj4" >}} {slides 15-23}

Refer to **A: Studying Higgs Boson Analysis. Signal and Background, Part 1,2,3,4,6,7**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Examples of Event Counting II: Change shape of background and number of Higgs Particles produced in experiment

This lesson continues the examination of Monte Carlo data looking at the effect of change in the number of Higgs particles produced and in the change in the shape of the background.

{{< syoutube "bw3fd5cfQhk" >}} {slides 25-29} 

Refer to **A: Studying Higgs Boson Analysis. Signal and Background, Part 5- Part 6**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

Refer to **B: Studying Higgs Boson Analysis. Signal and Background**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_B.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_B.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Resources 

Python for Data Analysis: Agile Tools for Real-World Data By Wes McKinney, Publisher: O’Reilly Media, Released: October 2012, Pages: 472. 

http://jwork.org/scavis/api/ 

https://en.wikipedia.org/wiki/DataMelt

## Looking for Higgs Part III: Random variables, Physics and Normal Distributions

We introduce random variables and some simple principles of statistics and explain why they are relevant to Physics counting experiments. The unit introduces Gaussian (normal) distributions and explains why they have seen so often in natural phenomena. Several Python illustrations are given. Java is not discussed in this unit.

[Slides](https://drive.google.com/file/d/1eH59S0G43RTLHI-YCr6uGFaAcp1NcS0P/view?usp=sharing) {slides 1-39}

### Statistics Overview and Fundamental Idea: Random Variables 

We go through the many different areas of statistics covered in the Physics unit. We define the statistics concept of a random variable

{{< syoutube "jCgY6MEfLWI" >}} {slides 1-6}

### Physics and Random Variables 

We describe the DIKW pipeline for the analysis of this type of physics experiment and go through details of the analysis pipeline for the LHC ATLAS experiment. We give examples of event displays showing the final state particles seen in a few events. We illustrate how physicists decide what’s going on with a plot of expected Higgs production experimental cross sections (probabilities) for signal and background.

#### Part 1

{{< syoutube "Tn3GBxgplxg" >}} {slides 6-9}

#### Part 2

{{< syoutube "qWEjp0OtvdA" >}} {slides 10-12}

### Statistics of Events with Normal Distributions 

We introduce Poisson and Binomial distributions and define independent identically distributed (IID) random variables. We give the law of large numbers defining the errors in counting and leading to Gaussian distributions for many things. We demonstrate this in Python experiments.

{{< syoutube "LMBtpWOOQLo" >}} {slides 13-19}

Refer to **C: Gaussian Distributions and Counting Experiments, Part 1**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Gaussian Distributions 

We introduce the Gaussian distribution and give Python examples of the fluctuations in counting Gaussian distributions.

{{< syoutube "LWIbPa-P5W0" >}} {slides 21-32}

Refer to **C: Gaussian Distributions and Counting Experiments, Part 2**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Using Statistics 

We discuss the significance of a standard deviation and role of biases and insufficient statistics with a Python example in getting incorrect answers.

{{< syoutube "n4jlUrGwgic" >}} {slides 33-39}

Refer to **C: Gaussian Distributions and Counting Experiments, Part 3**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>


### Resources 

http://indico.cern.ch/event/20453/session/6/contribution/15?materialId=slides
http://www.atlas.ch/photos/events.html (this link is outdated) 
https://cms.cern/

## Looking for Higgs Part IV: Random Numbers, Distributions and Central Limit Theorem

We discuss Random Numbers with their Generators and Seeds. It introduces Binomial and Poisson Distribution. Monte-Carlo and accept-reject methods are discussed. The Central Limit Theorem and Bayes law conclude the discussion. Python and Java (for student - not reviewed in class) examples and Physics applications are given

[Slides](https://drive.google.com/file/d/1IlAACaEiuw6c9HUlHmLxAgtyTw-iTOXk/view?usp=sharing) {slides 1-44}

### Generators and Seeds 

We define random numbers and describe how to generate them on the computer giving Python examples. We define the seed used to define how to start generation.

#### Part 1

{{< syoutube "r80Sk_KVG2s" >}} {slides 5-6}

#### Part 2

{{< syoutube "9QY5qkQj2Ag" >}} {slides 7-13}

Refer to **D: Random Numbers, Part 1**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_D.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_D.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

Refer to **C: Gaussian Distributions and Counting Experiments, Part 4**
<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Binomial Distribution 

We define the binomial distribution and give LHC data as an example of where this distribution is valid.

{{< syoutube "DPd-eVI_twQ" >}} {slides 14-22}

### Accept-Reject Methods for generating Random (Monte-Carlo) Events

We introduce an advanced method accept/reject for generating random variables with arbitrary distributions.

{{< syoutube "GfshkKMKCj8" >}} {slides 23-27}

Refer to **A: Studying Higgs Boson Analysis. Signal and Background, Part 1**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_A.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>

### Monte Carlo Method 

We define the Monte Carlo method which usually uses the accept/reject method in the typical case for distribution.

{{< syoutube "kIQ-BTyDfOQ" >}} {slides 27-28}

### Poisson Distribution 

We extend the Binomial to the Poisson distribution and give a set of amusing examples from Wikipedia.

{{< syoutube "WFvgsVo-k4s" >}} {slides 30-33}

### Central Limit Theorem 

We introduce Central Limit Theorem and give examples from Wikipedia

{{< syoutube "ZO53iKlPn7c" >}} {slides 35-37}

### Interpretation of Probability: Bayes v. Frequency

This lesson describes the difference between Bayes and frequency views of probability. Bayes’s law of conditional probability is derived and applied to Higgs example to enable information about Higgs from multiple channels and multiple experiments to be accumulated.

{{< syoutube "jzDkExAQI9M" >}} {slides 38-44}

Refer to **C: Gaussian Distributions and Counting Experiments, Part 5**

<div class="aside">
  <table style="width:100%">
  <tr>
    <td><a href="https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>    
    <td><a href="https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/E534_Higgs_Discovery_C.ipynb" target="_parent"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" alt=""/> View in Github</a></td>
  </tr>
</table>  
</div>
