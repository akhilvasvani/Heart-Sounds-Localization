# Heart Sounds Localization

Python application that detects S1 and S2 sounds in the human heart using sound source localization.

## Table of Contents

* [General info](#general-info)

* [How to use](#how-to-use)



### General Info

The proprietary heart data, saved in a .mat file (MATLAB file), is read in and split into 24 cycles each labelled in a Folder S1 and S2. 

Next, in the main script, using the distance of arrival (DOA) algorithms, the azimuth and colatitude angles calculated for pairs of three microphones.
Using both angles are found, they are convert them into a cartesian coordiates (x,y,z) and placed them in a K-Dimensional Tree structure to find the S1 and S2 sources. Once an intersection or a small enough area is determined, those cartesian coordinates are saved into a csv file. 

Finally, last of all, all those coordinates are graphed, displayed in a png image, and saved as well. 

Note: csvs are saved in the format width, depth, and then length. This is the most accurate depiction of where the S1 and S2 Sounds are.

## How to Use

Download the code and run ```python3 main.py```



## Time to Run

SRP ~ 1 minute

TOPS ~ 3 minutes

MUSIC ~ 5 minutes


### Requirements

Python 3.x

pyroomacoustics

SciPy

NumPy

itertools

Thread

### Results

There are four folders (two types: Recovered and Non-recovered signals). The recovered signals are the original microphone signals preprocessed using the JADE Algorithm to better seperate the sources. Each folder has a different number of trial results for either a 2 pair microphone combination or a 3 pair microphone combination. For each, there is a statistics text file to provide the statistics of each trial. 

Overall, using the non-recovered signals proved easier to find S1 and S2 than using the recover signals did. Though to truly compare the accurary of the DOA methods, there needs to be an echocardiogram of the patient to compare with. For now though, using the approximate locations provided from an echocardiogram textbook and the paper "Imaging of heart acoustic based on the sub-space methods using a microphone array," we found the closest points to these locations for S1 and S2.

# References

## Heart References

[Diagram of Heart](https://en.wikipedia.org/wiki/Pulmonary_valve#/media/File:Diagram_of_the_human_heart_(cropped).svg)

[Heart Sounds Review 101](https://www.healio.com/cardiology/learn-the-heart/cardiology-review/topic-reviews/heart-sounds)

[Heart Valve Wikipedia](https://en.wikipedia.org/wiki/Heart_valve)

[Very Strong human heart diagram with body](http://www.stethographics.com/heart/main/sites.htm)

[Another good diagram](https://www.google.com/search?q=heart+sound+locations&client=ubuntu&hs=1Go&channel=fs&tbm=isch&source=iu&ictx=1&fir=s559O9wHQ3RQ1M%253A%252CEj2EttfwJrRmzM%252C_&vet=1&usg=AI4_-kQ8ZFczzM9SsLvrI_Pm2fgmukBxgw&sa=X&ved=2ahUKEwiW27Gy27riAhUSy1kKHfTtCZIQ9QEwD3oECAgQDg#imgrc=v_gPbPh7ZpAvfM:&vet=1)

[Mitral Valve Prolapse](https://www.webmd.com/heart/mitral-valve-prolapse-symptoms-causes-and-treatment#1)


## Credits

Thank you [Pyroomacoustics](https://github.com/LCAV/pyroomacoustics) for the open-source library containing the differnt DOA methods. 

[Christos Sapsanis](https://engineering.jhu.edu/ece/2019/05/03/the-stethovest-aims-to-bring-the-stethoscope-up-to-date-with-modern-medical-imaging-techniques/?fbclid=IwAR25OcGjx24N1lLi9fQaTHODp0uNWiCMcliCYSmgdXiFQs7Ea_h_w50cW2o#.XriE4RNKhZJ)

Professor Andreas G. Andreou

## Future
Building a deep neural network to classify the heart sounds to detect potential heart murmurs and classify them accordingly. Below is a paper that builds something similar to what I am attempting to do. The next iteration of my project will focus on this

[Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network](https://stanfordmlgroup.github.io/projects/ecg2/)

[More Data](https://irhythm.github.io/cardiol_test_set/)

[Even More Heart Data](https://physionet.org/physiobank/database/#ecg)

[Diagram of where the leads are put](https://www.theonlinelearningcenter.com/Assets/PMDCBT/PIIC_Fundamentals_1.0/shell/viewer/swfs/assets/downloads/12-lead.pdf)

[Types of Leads used in ECG](https://www.cardiosecur.com/magazine/specialist-articles-on-the-heart/lead-systems-how-an-ecg-works)

[How to put the standard 12-leads on](https://www.adinstruments.com/blog/perform-accurate-12-lead-ecg)

Maybe use some type of clustering ([K-means](https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a), perhaps?) to cluster the points which are close to one another together. This might be a faster way to converge to a centeroid location.

[Single-speaker-localization with CNNs](https://github.com/Soumitro-Chakrabarty/Single-speaker-localization)

Paper: [Towards End-to-End Acoustic Localization using
Deep Learning: from Audio Signal to Source Position
Coordinates](https://arxiv.org/pdf/1807.11094.pdf)
