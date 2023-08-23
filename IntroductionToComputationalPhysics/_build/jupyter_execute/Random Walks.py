#!/usr/bin/env python
# coding: utf-8

# # Random Walks

# * **Author:**
# 
# * **Date:**
# 
# * **Time spent on this assignment:**

# Remember to execute this cell to load numpy and pylab.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
def resetMe(keepList=[]):
    ll = get_ipython().run_line_magic('who_ls', '')
    keepList=keepList+['resetMe','np','plt']
    for iiii in keepList:
        if iiii in ll:
            ll.remove(iiii)
    for iiii in ll:
        jjjj="^"+iiii+"$"
        get_ipython().run_line_magic('reset_selective', '-f {jjjj}')
    ll = get_ipython().run_line_magic('who_ls', '')
    return


# ## Exercise 1: Unbiased Random Walks

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# In 1827, the botanist Robert Brown noticed that pollen grains floating in water would bounce around randomly, but was confused as to the reason. In 1905, Einstein successfully described the motion of the pollen particles, dubbed *Brownian motion*, as a random walk resulting from microscopic particles bombarding the large pollen grain. For the first half of this unit, we will study the random motion of Brown’s pollen grains in one and two dimensions.
# 
# First, let’s visualize a random walk in one-dimension. Let’s say that we are looking at a pollen particle stuck in a tube full of water so that it can only move left or right. 
# 

# <!--![image.png](attachment:image.png)-->
#  <div><img src="https://clark.physics.illinois.edu/246img/RW1.png" width=400 alt="RW"></img><br></div>

# We mark its original position as $x_0=0 \mu m$. Every 30 seconds, we take a picture and record the position of the particle $x_t$ in $\mu m$.  What we would record is something like this:

# <!--![image.png](attachment:image.png)-->
#  <div><img src="https://clark.physics.illinois.edu/246img/RW2.png" width=450 alt="RW"></img><br></div>

# In simulating this random walk, we assumed that every time we measured the particle’s position, it only depended on its previous position 30 seconds ago plus some random noise $\delta$.
# 
# $$x_{t+1} = x_t + \delta.$$
# 
# In python, we can model the random jumps we see using numpy’s random number
# generators:
# ```python
# x[t+1] = x[t] + averageJumpDistance * np.random.randn()
# ```
# where `averageJumpDistance` is the typical distance the pollen particle jumps every 30 seconds, which I set to 6 $\mu m$. The `np.random.randn()` command generates a random number from the Gaussian (or Normal) distribution with mean zero and standard deviation one.
# 
#    

# ### a.  Plot a random walk

# 🦉Generate your own random walk and plot it. Use the same parameters as in the above figure, i.e., simulate $6 \mu m$ jumps every 30 seconds for 30,000 seconds, or 1,000 jumps.
# 
# The first thing you will notice is that random walks can vary a lot. Yours will probably look very different than the one in the above figure. Generate another random walk using your code and notice that it too is different form your first walk. So what can we learn about how the pollen grain moves if every time the motion is random? Well, we can try simulating many random walks and looking at what happens on average.

#  <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[2]:


### ANSWER ME


#  <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ### b. Random Walk Averages

# 🦉Generate 2,000 random walks and write code to calculate, then graph the average position $\langle x_k \rangle$ after the kth jump, for k running from 0 to 1,999. What do I mean by averaging over walks? For example, say that we have two random walks, each made of 1,000 steps. I store the positions of the random walks as two length 1,000 arrays walk1 and walk2. Averaging over the two walks, the average position after each jump is an array I can calculate as 
# 
# `average_array = (walk1 + walk2) / 2.0`.
# 
# There’s a more graceful way to do this than storing all the arrays, then calculating the average at the end. Instead, add the position after each jump while generating a walk into a single accumulator array. After you are done generating walks divide each element in your accumulator array by the number of walks.
# Let me illustrate what I mean with a table of hypothetical data, for 2,000 random walks, each of 1,000 jumps.
# 
# 

# |which random walk| $x_0$(µm)|$x_1$(µm)|$x_2$(µm)|...|$x_{999}$(µm)|
# |-----------------|----------|---------|---------|---|-----------|
# |0                | 0 | 0.48|7.4|&nbsp;|0.81|
# |1                | 0 | -1.5|1.3|&nbsp;|7.5|
# |2                | 0 | -3.3|-2.6|&nbsp;|6.8|
# |...                | ... | ...|...|&nbsp;|...|
# |1,999                | 0. | 88.5|-42.2|nbsp;|74.1|
# |averages| $\langle x_0\rangle=0$ |$\langle x_1\rangle=37.8$|$\langle x_2\rangle=45.1$|...|$\langle x_{999}\rangle=0.51$|

# Before you compute the average positions, think about what you expect. Once you see the result, does it agree with your expectations? Does it make sense to you? Here’s my plot:
# 

# <!--![image.png](attachment:image.png)-->
#  <div><img src="https://clark.physics.illinois.edu/246img/RW3.png" width=450 alt="RW"></img><br></div>

#  <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[3]:


### ANSWER ME


#  <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ### c. Computing average distance

#  An interesting quantity to consider for random walks is the root-mean-square (RMS) displacement as a function of time. For the $k$'th jump the RMS tells us how much the pollen particle’s position will have tended to drift by the time it executes the $k$'th jump in a typical walk.
#  
# Is is easy to calculate the RMS displacement for each bin without storing the position arrays of individual walks. Here’s how: 

# $$
# \begin{align}
# RMS_{k^{th} jump} &= \sqrt{\frac{1}{N}\sum_{j=0}^{j=N}\left(x_{k,walk\,j}-\langle x_k\rangle\right)^2}\\
# &= \sqrt{\left( \frac{1}{N}\sum_{j=0}^{j=N}\left(x_{k,walk\,j}\right)^2\right)- \left(\sqrt{\frac{2}{N}\sum_{j=0}^{j=N} x_{k,walk\, j} \langle x_k \rangle} \right) + \left( \frac{1}{N}\sum_{j=0}^{j=N}\langle x_k \rangle^2\right)}\\
# &= \sqrt{\langle x_k^2 \rangle - \left(\sqrt{2\langle x_k \rangle\frac{1}{N}\sum_{j=0}^{j=N} x_{k,walk\, j} } \right) + \left( \frac{\langle x_k \rangle^2}{N}\sum_{j=0}^{j=N}1 \right)}\\
# &=\sqrt{\langle x_k^2\rangle -2\langle x_k\rangle\langle x_k\rangle+\langle x_k\rangle^2}\\
# &=\sqrt{\langle x_k^2\rangle - \langle x_k\rangle^2}
# \end{align}
# $$

# All you need to do is calculate the average value of $x_k^2$ and the average value of $x_k$. So each time you generate a walk, add the position of each jump into an accumulator array and the square of the position into another accumulator array. At the end, divide the contents of each bin in your accumulator arrays by the number of walks.
# 
# 🦉Write code to compute the RMS displacement as a function of time using 2,000 random walks and plot the result. You should get something similar to the following curve:

# <!--![image.png](attachment:image.png)-->
#  <div><img src="https://clark.physics.illinois.edu/246img/RW4.png" width=450 alt="RW"></img><br></div>

# We see that, on average, there is a very clear trend for the pollen particle to drift farther away over time. If we ignore the small value of the average position $\langle x_k \rangle$ we can write
# 
# $$RMS_\textrm{kth jump} = \sqrt{\langle x_k^2\rangle - \langle x_k \rangle^2} \approx \sqrt{\langle x_k^2 \rangle} \propto \sqrt{t_k}$$
# 
# The square root here is very important and characterizes all diffusive motion. Note that a free particle moving with constant velocity will have $x\propto t$. Such motion is sometimes called ballistic motion. The main takeaway is that diffusive motion is much slower than ballistic motion. Intuitively, this makes sense since, in diffusive motion, a particle is being severely slowed down by random bombardments from its environment.
# 
# 🦉In addition to the plot above, make another log-log plot (of the same data) and show:
# * you get a line on this log-log plot (this shows that $x \propto t^{\alpha}$)
# * Find the value of $\alpha$ by computing the slope of your (log-log) line using `np.polyfit`. Show that it goes as $t^{1/2}$

#  <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[4]:


### ANSWER ME


#  <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ## Exercise 2: Random Walks in Two Dimensions

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# Now, let’s consider a two-dimensional random walk. We put our pollen particle on a petri dish covered with a thin layer of water so that it can move in a plane.

#  <div><img src="https://clark.physics.illinois.edu/246img/RW5.png" width=1000 alt="RW"></img><br></div>

# ### a. 2D Walks

# 
# We mark the pollen grain’s initial position as   $(x_0,y_0)=(0,0) \mu  m$. We measure every 30 seconds and see each component of the pollen particle’s position $x_k,y_k$ jump from its previous
# position. We’ll expect the typical jump distance to be $\approx 6\sqrt{2}$ $\mu m$.
# 
# Write code that generates 2,000 two-dimensional random walks and plots the average radial displacement over time:
# 
# $$\langle r \rangle = \langle \sqrt{x_k^2 + y_k^2}  \rangle$$
# 
# You should obtain a similar curve to that obtained in the one-dimensional case, but increased somewhat in amplitude. Even in two-dimensions, the displacement goes with the square root of time. It turns out that you also see this behavior in three dimensions. In general, the RMS displacement always scales as the square root of time for any physical system undergoing diffusive motion.
# 
# 🦉Generate and plot the radial displacement vs time for 2,000 2D random walks. Also show it on a log-log plot and compute the slope.
# 
# 

#  <div><img src="https://clark.physics.illinois.edu/246img/AnsStart.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# In[5]:


### ANSWER ME


#  <div><img src="https://clark.physics.illinois.edu/246img/AnsEnd.svg" width=200 align=left alt="Answer (start)"></img><br></div>

# ## Exercise 3: Uniform walks (EC - 5 points)
# *(Extra credit: 5 points)*
# 

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# Do a similar analysis to the work above (in two dimensions) using walks that randomly make a step in one of four directions of unit length. Notice that this explicitly breaks the circular symmetry of the two-dimensional Gaussian random walks.  Show that these uniform walks still have a diffusive aspect at large distances and (at large distances) restore this symmetry (i.e. the two-dimensional density profile of being a distance $r$ aways doesn't differ for up vs up-right).  This restoration of symmetry is an aspect of universality.  

# In[ ]:





# ## Exercise 4: Gaussian Random Walks (EC)
# *(Extra credit: 20 points)*

# * **List of collaborators:**
# 
# * **References you used in developing your code:**

# (Some of the explanaitions here are abbreviated even for an extra credit.  I am sneakily having you do Quantum Monte Carlo (QMC) here.  If you want to do this extra credit [particularly after part **a.**] you should probably come talk to me)

# ### a. Fixed Points

# Imagine we were to produce the walks in exercise 2 and then throw out any of the walks that didn't end at $(x,y)=(5,5)$.  This would induce some probability distribution over walks.  Unfortunately this would be very inefficient.  Instead figure out (read about Levy Flights and Brownian bridges) how to generate the same probability distribution as this efficiently. Write code that does so and then plot 10 paths between two fixed points (you can choose where they are fixed).

# In[ ]:





# ### b.  Connected Points

# Start with 100 connected (in order) points all at $(0,0)$ (i.e. $x_0=(0,0); x_1=(0,0);...$ . We will have $x_{99}$ connceted to $x_0.$ Choose a window of ten points at random (maybe 33-43) and use the algorithm you described in **4a** to regenerate points $x_{34},x_{35},..,x_{42}$.   Then pick another window and do this again.  Repeat this process 1000 times and 
# * make a plot of your points (connected by lines)
# * Report the average distance between consecutive points. 
# * Make a histogram of the distances between average points. 

# In[ ]:





# ### c. Fixed Region

# Repeat **b.** with the constraint that you should just not rebuild your window if, after making the new points, any of the points are outside a box that extends $-1 \leq x \leq 1$ and $-1 \leq y \leq 1$.
# 
# Graph the probability points are at given places in the box.

# In[ ]:





# ### d. 1D

# Redo this for one dimension.

# In[ ]:





# **Acknowledgements:
# 
# * George Gollin and Ryan Levy and Eli Chertkov (original); Bryan Clark (modifications)
# 
# ---
# © Copyright 2021
# 
