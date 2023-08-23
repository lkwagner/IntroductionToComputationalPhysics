#!/usr/bin/env python
# coding: utf-8

# # Particle Physics

# *Monte Carlo Simulation of a Particle Physics Experiment*

# * **Author:**
# 
# * **Date:**
# 
# * **Time spent on this assignment:**

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle_helper import Kdecay
def resetMe(keepList=[]):
    ll = get_ipython().run_line_magic('who_ls', '')
    keepList=keepList+['resetMe','np','plt','Axes3D','Kdecay']
    for iiii in keepList:
        if iiii in ll:
            ll.remove(iiii)
    for iiii in ll:
        jjjj="^"+iiii+"$"
        get_ipython().run_line_magic('reset_selective', '-f {jjjj}')
    ll = get_ipython().run_line_magic('who_ls', '')
    return
import datetime;datetime.datetime.now()


# ## Background

# ### Some particle physics history
# In 1979 a particle physics experiment led by Jim Christenson published a report[<sup>1</sup>](#fn1)  describing a small anomaly in the behavior of K mesons that suggested a breakdown in causality at subnuclear distance scales. The effect—seen at two standard deviations above background—deserved further investigation. Surely it must have been a matter of bad luck, or unforeseen systematic errors. But confirmation of Christenson’s result would show that the laws of nature were, at small distances, non-local (a string theory, perhaps), or else that physical law could no longer be formulated in mathematical language. Our world would be properly described by string theory, or by magic.  
# 
# 
# Some years after the Christenson result George Gollin proposed a new experiment using a different technique to look for the same effect. We planned to do it at Fermilab, with much better precision and greatly reduced systematic uncertainties, and a few of us set about designing the apparatus for the measurement[<sup>2</sup>](#fn2).   
# 
# 
# We planned to study the decay rates of neutral K mesons into neutral and charged pions:
# $$
# K \rightarrow \pi^0\pi^0;\quad K\rightarrow\pi^+\pi^-
# $$
# in a pair of specially prepared beams. The apparatus would measure the momenta of charged pions using a spectrometer comprising four tracking chambers and a large dipole magnet. We of course needed a hole near the center through which a beam of kaons that hadn’t decayed in flight would pass, rather than smacking into the apparatus.  

# <div><img src="https://clark.physics.illinois.edu/246img/particle1.png" width=600 alt="Answer (start)"></img><br></div>
# 

# We would identify $K$ mesons in our data by seeing that the "invariant mass" $(E^2/c^2 - p^2)^{1/2}$ of the parent particle that had yielded the pions was consistent with the kaon mass of 498 MeV/$c^2$. Because of the manner in which we had prepared the kaon beams before they arrived at the experiment, we would extract physics from our data by measuring the double ratio
# $$
# R \equiv \frac{\Gamma_{beam1}(K\rightarrow\pi^0\pi^0)}{\Gamma_{beam2}(K\rightarrow\pi^0\pi^0)} {\Large /} \frac{\Gamma_{beam1}(K\rightarrow\pi^+\pi^-)}{\Gamma_{beam2}(K\rightarrow\pi^+\pi^-)}
# $$
#  
# Here $\Gamma$ means "decay rate," and the ratios of those decay rates would correspond closely to the ratios of the total number of $K$ meson decays in our data. If Christenson's result had been correct, we would measure $R$ to be about 0.88, with an expected precision of $\pm$0.01. If there were no subnuclear violation of causality we would obtain 1.00.
# We would reconfigure a large device we had used in a previous kaon experiment, so we needed to work within constraints that would allow us to reuse existing instrumentation as much as possible.   
# 
# We needed to maximize the device's "geometrical acceptance" in order to maximize the number of decaying kaons that would put both charged pions (or all four photons) into the tracking chambers and lead glass array. We would lose kaons that decayed too close to the tracking system because pions or photons would go down the holes in the middle of the lead glass. Kaons that decayed too far upstream would send decay products wide of the tracking chambers. So the first question to be answered was how much space to leave between the source of kaons (downstream of which kaons decayed exponentially) and the tracking system. (We would be recording data from one kaon decay at a time, with an average rate of about one per minute.)  
# 
# We used a Monte Carlo simulation of the detector and beam to address this question. After some preliminaries, we're going to begin to set this up; you’ll actually answer the question of optimum target location in this unit.

# ### Monte Carlo simulations in the context of designing an experiment
# Let’s imagine a stripped-down Fermilab experiment to begin with a target, out of which will stream a monoenergetic "pencil" beam of relativistic $K$ mesons. By this I mean that all kaons travel in exactly the same direction with the same energy, and move precisely along the z axis. Some distance downstream of the target will be a pair of tracking chambers and a hadron calorimeter—a device that measures the energies of charged pions—but nothing else. We’ll put a hole down the center of the calorimeter to prevent the beam from damaging the device. Since a high energy neutral $K$ beam can be expected to contain more neutrons than kaons, this is an important feature of our calorimeter, which would otherwise be fried by the beam. In our model we’ll assume that kaons have total energy 60 GeV, typical of kaons in Gollin's experiment. We’ll concentrate on the charged ($\pi^+\pi^-$) decay mode.   
# Here are a couple of diagrams:

# <div><img src="https://clark.physics.illinois.edu/246img/particle2.png" width=600  alt="Answer (start)"></img><br></div>

# How far from the calorimeter should we place the target that produces the kaons? Too close and one or both pions will usually go down the hole so we will not be able to measure their energies. Too far and pions will tend to go wide of the calorimeter. We want to determine the target position that maximizes the probability that a decaying kaon sends both of its pions into the active regions of the tracking chambers and calorimeter.  
# 
# 
# Since I’ve declared that all kaons will have the same energy and travel in the same direction as they leave the target, there are only three more parameters needed to uniquely specify the kinematic properties of the final state. They are the distance from the target to the kaon decay point (as measured in the lab frame) and the $\theta$ and $\phi$ angles that one of the pions (say the $\pi^+$) makes with respect to the $z^\prime$ axis in the kaon rest frame. (Other choices of parameters are possible, but these are especially convenient.) Once we know those three parameters we are able to calculate everything there is to know about the final state pions in the lab frame. In particular, once we know $z$, $\theta^\prime$, and $\phi^\prime$  we are able to determine whether or not both pions will end up hitting the tracking chambers and calorimeter. In particle physics language, once we know $z$, $\theta^\prime$, and $\phi^\prime$ we are able to determine unambiguously whether or not that particular kaon decay "is in the acceptance of our apparatus."  
# 
# Here are figures to clarify what we mean by $z^\prime$, $\theta^\prime$, and $\phi^\prime$. The angles are the usual (physics convention) spherical coordinate angles, with the lab frame coordinate axes parallel to the $K$ rest frame axes. The angle $\phi^\prime$ is between the $x^\prime$ axis and the projection onto the $x^\prime y^\prime$ plane of the vector momentum of the positive pion. The $z^\prime$ axis (in the kaon’s rest frame) is parallel to the lab frame’s $z$ axis.
# 

# <div><img src="https://clark.physics.illinois.edu/246img/particle3.png" width=400 alt="Answer (start)"></img><br></div>

# I can represent a kaon decay as occupying a point in a three dimensional parameter space (we call it a phase space) whose axes represent the decay’s particular $z$, $\theta^\prime$ and $\phi^\prime$ values. The following figure shows a schematic representation of a few dozen kaon decays that took place in our hypothetical experiment’s beamline. Some were accepted, and some were not.

# <div><img src="https://clark.physics.illinois.edu/246img/particle4.png" width=400 alt="Answer (start)"></img><br></div>

# By generating a large number of simulated decays with a Monte Carlo program we can calculate (and maximize) the volume inside the boundary containing accepted events. That sounds more sophisticated than it really is: we move things around (for example the distance from the target to the tracking chambers) and we watch how the fraction of the decays we are able to accept changes. The greater the phase space volume, the larger the fraction of decaying kaons that will end up in our data for later offline analysis. So we use the Monte Carlo in a way that is essentially the same as what you did to estimate the value of $\pi$.

# ## Exercise 1 - Minimal Simulation of the tracking chamber & Calorimeter

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# ### 0. Some Preliminaries
# Here are the apparatus diagrams from above:

# <div><img src="https://clark.physics.illinois.edu/246img/particle5.png" width=600 alt="Answer (start)"></img><br></div>

# There are four elements in the apparatus for us to describe in our code: the kaon production target, the first and second tracking chambers, and the hadron calorimeter. We will model the chambers and calorimeter as infinitesimally thin in the z direction and square in cross section, centered on the z axis, along which the kaon beam travels. The calorimeter has a square hole in its center through which debris from the target, and particles in the beam that have not yet decayed, will pass.  
# 
# The two tracking chambers are separated by 10 meters along the beam direction; the calorimeter is 5 meters downstream of the second tracker. For technical reasons (umm… actually just to simplify things for you) the separation between chambers, and between the calorimeter and the tracking system is not to be changed. You ***can***, however, move all three devices upstream or downstream during your investigations, as long as you don’t alter their separations from each other. Please keep the target at $z = 0$.  
# 
# Here is a table specifying the initial geometry you are to use in your Monte Carlo. Units are in meters.

# |apparatus element| z |x extent |y extent|
# |-----------------|---|---------|--------|
# |production target |0  |0        |0       |
# |tracker 1         |38 |-0.6 < x < 0.6| -0.6 < y < 0.6 |
# |tracker 2| z<sub>tracker1</sub> + 10| -0.7 < x < 0.7 |-0.7 < y < 0.7|
# |calorimeter |z<sub>tracker1</sub> + 15 |-0.75 < x < 0.75 |-0.75 < y < 0.75|
# |hole in calorimeter |z<sub>tracker1</sub> + 15 |-0.25 < x < 0.25 | -0.25 < y < 0.25|
# 

# Only the data from $K$ decays in which both pions pass through the active regions of the two tracking chambers and calorimeter will be accepted—stored for subsequent analysis by your experiment.   
# 
# 
# We have written a class definition that you can instantiate, then use very much like a python library to generate $K$ decays. The definition contains a class function that returns the z position of a decay (with probability of a particular z value distributed according to an exponential decay law), along with the four momenta of the two pions.   
# 
# Here is how to use it,

# In[9]:


# instantiate the kaon decay generator class
KDG = Kdecay()

# now get the kinematic details about a kaon decay. The decay generator returns
# numpy arrays with vertex x, y, z; pi+ four momentum [E/c, px, py, pz];
# pi- four momentum.
vertex, pmu_plus, pmu_minus = KDG.getdecay()


# Since the decay generator returns the momentum components for the pions you can project them from the decay vertex to their downstream x, y positions at the z locations of the tracking chambers and calorimeter. This will let you determine whether or not the pions are inside the active volumes of the tracking chambers and calorimeters.

# ### a. Histograms and so forth

# In our simulated experiment we require both pions to pass through the sensitive regions of the tracking chambers and land in the active region of the calorimeter. An event in which a pion misses a tracking chamber, goes wide of the calorimeter, or goes down the hole in the middle of the calorimeter will not satisfy the trigger (the high speed logic that decides whether or not we should record data from the decay), and won't be written to a data file for further analysis.  **In other words, *both* pions must hit both trackers and the calorimeter in order to satisfy the trigger**.
# 
# 
# 🦉Please generate histograms of the following quantities, assuming the apparatus is configured as described in the above table. Once your program runs, I suggest you have it generate 100,000 kaon decays. 
# 
# 1. pion x positions at the plane in z holding tracking chamber 1 for all k decays
# 2. pion x positions at the plane in z holding tracking chamber 2 for all k decays 
# 3. pion x positions at the calorimeter for all pions that satisfy the experiment’s trigger
# 4. kaon decay z position for all k decays
# 5. kaon decay z position for k decays that satisfy the experiment’s trigger
# 6. pion energies in the lab frame, all k decays
# 7. pion energies in the lab frame for k decays that satisfy the experiment’s trigger
# 
# Here's how everything should look:

# <div><img src="https://clark.physics.illinois.edu/246img/particle6.png" width=1000 alt="Answer (start)"></img><br></div>

# Note that plots 1-3 have `bins=200` and 4-7 have `bins=100`

#  <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[1]:


###ANSWER HERE


# <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ### b. Why events fail to satisfy the trigger

# Please determine the fraction of kaon decays that fall into the following categories:  
# 
# 1. the decay satisfies the experiment trigger: both pions pass through the active areas of the two tracking chambers and strike the active region of the calorimeter;
# 2. one pion goes (or both pions go) down the hole in the calorimeter; 
# 3. one pion goes (or both pions go) wide of the calorimeter;
# 
# You should find that about 77% of the decaying kaons put at least one pion down the hole. Next unit you’ll work on maximizing the fraction of kaon decays that actually satisfy the experiment’s trigger. Here are my results:
# ```
# number of decays: 100000
# number of triggers: 22804
# number of events with pion(s) in hole: 77196 
# number of events with pion(s) wide: 0 
# target-to-first-tracker distance: 38
# ```
# And that’s it!

# <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[2]:


### ANSWER HERE


# <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ## Exercise 2 - Geometrical acceptance

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# ### Background

# Previously in class you determined an approximate value for $\pi$ by dropping random x, y points into a square whose sides were of unit length, then determining the fraction of points that were also contained inside the perimeter of an inscribed circle. You were, in effect, measuring the "geometrical acceptance" of the circle when exposed to a random "beam" of points. There were only two numbers you needed to describe uniquely each "event" (the placing of a point inside the square): the point's x and y coordinates. And the boundary in that x, y parameter space is easy to imagine: it's just a circle of unit diameter.  
# 
# The geometrical acceptance of a particle physics experiment can be characterized in similar fashion as a region (or regions) inside a parameter space from which we will always accept events. In our case we can completely characterize an event by specifying the z position of the decaying kaon and the two (spherical coordinate) angles needed to describe the direction of the positive pion. Everything else—the pion energies in the lab frame, for example, or the momentum of the other pion, or where in the plane of the calorimeter the pions land—can be derived from these. In a more realistic model we would need to specify the kaon’s energy and vector momentum (since it is not possible to create a monochromatic kaon beam), the x, y, z coordinates of its decay point, the pion directions in the kaon rest frame, and so on.  
# 
# You should have found in the homework due this unit that our simple experiment failed to accept most decaying kaons because one (or both) went down the hole in the calorimeter. In our simple model it is only the calorimeter that measures the energies of pions, so we are unable to determine whether or not the signals in the tracking chambers actually came from pions or something else. (Neutral kaons can decay into final states that include neutrinos, electrons, and muons: the di-pion final state is not the only possibility.)    
# 
# You probably also noticed that the pions were concentrated near the center of the tracking chambers and calorimeter. Even though the half-width of the calorimeter was 0.75 meters, almost no pions landed more than a half-meter away from its median plane. It should be obvious that we can move the kaon-producing target upstream to good effect. That will make the “solid angle” subtended by the hole smaller, and fewer pions will find it. Of course, if we move the target too far upstream we will lose events from pions going wide of the calorimeter.
# 

# ### a. Plotting the occupied region of phase space

# I included above a schematic representation of events populating the $\theta^\prime -\phi^\prime-z$ phase space available to decaying kaons. (The angles describe the positive pion’s trajectory.) My figure used the angles in the kaon rest frame, but I could have just as easily filled the plot with the lab-frame values instead. 
# 
# That is what I would like you to do: generate decays with a few different target positions (build your program from the first unit 8 homework problem’s code) and make 3-d plots of the **lab frame** $\theta^\prime -\phi^\prime-z$ phase space, using small markers for the points corresponding to the "coordinates" in the phase space of each event. For each target position put into your plot the points for all events (as red dots, say) and then the points for all decays that trigger the apparatus (as black dots, perhaps). You will want to plot the triggering decays after plotting the “all decays” phase space points.  
# 
# The decay generator provides the lab-frame four momentum for each pion. You will need to calculate the $\theta-\phi$ angles from this. Keep in mind that $\phi$ ranges from $-\pi$ to $+\pi$, so you’ll probably need to use an arctan routine that takes two arguments.
#  
# To save time, let me remind you how to make 3-d plots. Let’s say you’ve generated 50,000 decays and stored the lab-frame phase space coordinate values in arrays this way:
# ```python
# # phase space coordinates in LAB: pi+ theta, phi and kaon decay z, all decays.
# phase_space_theta_mrad = np.array([np.nan] * number_of_decays_to_generate)
# phase_space_phi = np.array([np.nan] * number_of_decays_to_generate)
# phase_space_z = np.array([np.nan] * number_of_decays_to_generate)
# event_satisfied_trigger = np.array([False] * number_of_decays_to_generate)
# 
# # ...
# # fill the arrays of pi+ theta, phi, and z for each decay in a loop here
# # ...
# 
# # now store pi+ theta, phi and kaon decay z for events that satisfied the
# # trigger: define arrays then copy what you want into the arrays.
# phase_space_theta_triggers_mrad = np.array([np.nan] * number_of_triggers)
# phase_space_phi_triggers = np.array([np.nan] * number_of_triggers)
# phase_space_z_triggers = np.array([np.nan] * number_of_triggers)
# 
# # ...
# # fill the arrays
# # ...
# 
# 
# # now create a (blank) figure and get/set its axes.
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# # set the x, y, and z axis limits of the plot axes
# ax.set_xlim(0., 15.)
# ax.set_ylim(-3.5, 3.5)
# ax.set_zlim(0, 20) 
# # label the axes and give the plot a title
# ax.set_xlabel("theta")
# ax.set_ylabel("phi")
# ax.set_zlabel("z")
# ax.set_title("Kaon decay phase space: all decays-- George Gollin") 
# # now make the plot, using small red markers for all decays:
# ax.plot(phase_space_theta, phase_space_phi, phase_space_z, 'ro', markersize = 1)
# 
# # now add into the plot small black markers for triggering events.
# ax.plot(phase_space_theta_triggers_mrad, phase_space_phi_triggers, \
# phase_space_z_triggers, 'ko', markersize = 1)
# plt.show()
# ```
# 
# Try generating plots for these target-to-first-chamber distances, and take note of the number of triggers. My plots follow the table with my results. Rotate your plots around, taking note of the structure they exhibit. Why do they look this way? (A hint: the decay angles are azimuthally [$\phi$] symmetric, but the apparatus is not: it has four corners!)  
# 
# |target-to-tracker 1 distance (meters) |triggered events (out of 50,000)|
# |--------------------------------------|--------------------------------|
# |28 | 2,318|
# |38 | 11,370|
# |58 | 25,886|
# |78 | 16,646|
# 

# <!--![phase_space_28.png](attachment:phase_space_28.png)![phase_space_38.png](attachment:phase_space_38.png)![phase_space_58.png](attachment:phase_space_58.png)![phase_space_78.png](attachment:phase_space_78.png)-->
# <div><img src="https://clark.physics.illinois.edu/246img/particle7.png" width=1000 alt="Answer (start)"></img><br></div>
# 
# <div><img src="https://clark.physics.illinois.edu/246img/particle8.png" width=1000 alt="Answer (start)"></img><br></div>

# <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[3]:


### ANSWER HERE


# <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ## Exercise 3 - Finding Optimal Target Position

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# 🦉Find the target-to-first-tracker distance that maximizes your experiment’s geometrical acceptance. You ought to be able to do something clever with the program that you just wrote: for example, try wrapping a loop around part of your program to hunt for the best target position.  
# 
# Try running about 10,000 decaying kaons per trial target position, with z scans spaced by a meter or two. Once you get close to the optimal z position, do a more fine-grained scan at greater statistical precision. Try for an ultimate accuracy of about 50 centimeters.  
# 
# This is one of the most common uses for a Monte Carlo simulation, helping physicists optimize the configuration of an experiment.  
# 
# I find that the acceptance peaks at about 52% for a target-to-tracker1 separation of  about 59.6 meters. If you’re within a meter of my result, you’ve probably found something that is statistically indistinguishable from my result, so declare victory.  

# <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[4]:


### ANSWER HERE


# <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# *Extra credit (5 points)* - Implement binary search to find the peak acceptance. Don't forget your acceptance ratios have error bars!  
# *Extra credit (5 points)* - Q: Why does golden ratio search not work here?

# **Acknowledgements:**
# George Gollin (original)
# 
# © Copyright 2021  
# 
# ---

# <span id=“fn1”><sup>1</sup> J. H. Christenson, *et al*., Phys. Rev. Lett. *43*, 1209 (1979) and J. H. Christenson, *et al*., Phys. Rev. Lett. *43*, 1212 (1979).</span>  
# 
# <span id=“fn2”><sup>2</sup>It was the 773<sup>rd</sup> proposal received by Fermilab’s Proposal Advisory Committee and was given the catchy name "E773." We did the experiment, achieved the proposed sensitivity, and concluded that Christenson's anomaly was not supported by our data, alas.</span> 
# 

# In[ ]:




