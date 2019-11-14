---
title: 'Sound Classification Assignment'
disqus: hackmd
---

Sound Classification
===

## Table of Contents

[TOC]

## Introduction

In this project, there are five different sounds that are classified, Microwave, Vacuum, Blender, Music, and an Alarm. Twenty, 30 second samples were recorded of each sound, totaling 100 different samples. A machine learning model is trained using the sound to classify the sounds. Four different models were trained, a windowed implementation, a windowed and binned implementation, a binned implemenation, and a normal implementation (features were selected over the whole sound sample).


## Data Collection and Preprocessing

Each sample is in its own WAV file which is approximately 30 seconds long. The audio was recorded on an iPad Pro, which saves the audio under a .m4a extension, so each sample was converted to WAV using a converter. The samples are read in and pre-processed for each implementation seperately. For example, the whole windowed implementation will read the WAV files and process them, then the windowed and binned implementation will read and process the files again. 

Median filtering was used to pre-process the signal before features were extracted for all implementations. This was done to reduce the noise from the recording. The median filter size was selected so that important data is not lost due to the filtering.

## Features

```python
        fv = []
        fv.append(len(zero_crossings))#number of zero crossings
        fv.append(np.percentile(y,50))#find value halfway between sorted list
        fv.append(np.percentile(y, 70))#find value 70% up the sorted list
        fv.append(np.percentile(y, 80))#find value 80% up the sorted list
```
The domain specific features were take from the original signal and not the FFT output. This feature set was used in both the windowed and non windowed domain specific implemenation. I started collecting features in the time domain, with the intention of collecting more features in the frequency domain, but this feature set is giving me very accurate classification. The frequency domain features I would have added if needed are finding the peaks of the frequency after averaging the vector across time. This would have been very useful since the different classes all worked on different frequencies, and some would also have no peaks. Another feature would have been the change in frequency over a set amount of time. 

The number of zero crossing deemed very definitive in classifying the audio signal, this is because the number of zero crossing varied drastically between the different sound origins. Where as, remaining quite similar between samples of the same origin. The zero crossing can tell how many times the signal crossed the y=0, this allows us to roughly seperate a frequency component of the entire signal into one value. The other nth-percentile values also told the model alot about each signal. This value signifies the "loudness" of each signal and how much of it was loud. The higher the value the louder the signal. I chose to use three differents n values because the output will not be linear from 50th percentile and the 80th percentile, two origins may share a 50th percentile number but can be drastically different in the 80th. Mainly because the the values above could be extremely close to the 50th percentile or extremely far and every where in between.

## Results

All the models trained were highly accurate. They always scored above 90% accuracy. Changing the number of folds did effect the accuracy, but that is as expected. This is because there is a possibility to create folds that dont have enough of one sample to train it effectively. The binning was definitely the most accurate and the simplest to implement. Visually being able to see what the model uses to train in binning, allows the models to be trained with confidence. It can almost be assured that the models will train properly with binning. 

The cleanliness of the recordings also seemed to make the model training simpler, this allowed less preprocessing. This is because there was no background noise or other stuff going on in the background that would effect the sample, and it wouldnt allow the models to overfit due to those noises. The graphs plotted in the Jupyter Notebook show the binning output visually, there is one plot for each sample type. There is also a spectrograph of each type of sample and the relationships were drawn out from there.