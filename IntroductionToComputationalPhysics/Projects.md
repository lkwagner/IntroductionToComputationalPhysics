# Cool Projects


Dynamics:

* Understand the relationship between Reynolds number and air resistance.  Given an object compute the right value for the ....  model all sorts of objects and compare their terminal velocity.  

Orbital Dynamics:

* Compute a trajectory to launch from the Earth and land on the moon. To accomplish this, you will need to model both the spacecraft and the moon orbiting around the Earth.  In addition you will need to take into account the fact that the Earth is rotating and so gives an initial velocity to the spacecraft. 

* Compute a trajectory to launch from the Earth to Mars. 


* Model the trajectory of voyager through the Solar System.  This requires some intermediate thrusts from voyager and requires modeling a large part of the solar system.  This is a somewhat challenging project.  If you want to do this, you are essentially allowed to look anything up (i.e. you can go look up any information about voyager).  

* Lagrange points via optimization:  Find the lagrange points between the Sun and Earth by combining your orbital dynamics simulation and scipy.optimize.  Once you've found them, show that they work by modeling them in your simulations nad then show that two of them are stable and three of them are unstable. 


* Modeling the orbit of a spacecraft around a  black hole:  We modeled the perihelion at Mercury by taking the effect of general relativity to first order.  If you want to model orbiting around a black hole you need to actually use the proper GR equations of motion.  See Black Holes book. 
 
* Simulate the twin paradox. 

* Nice model for planetary formation 

Exoplanets: 
* Do the exoplanet assignment but get the data from a many-body simulation with two planets + the sun.  Write code that gets the oscillations for the largest planet.  Also write code that correctly accounts for the fact that the solar system you are emulating isn't aligned with the Earth. 

Chaos:

* Logistics map for chaos

* Chaos on billiard balls. There is a difference between square straight walls and curved walls. 

Many Body Simulations:

* Do a full simulation of the solar system.  You probably want to implement a symplectic integrator to do this.

* Do a galaxy simulation.  You probably want to implement a symplectic integrator to do this.  You may want to implement a method to speed up the use of the gravitiational force.  You can use jax for this project which probably wil make your life simpler.

*  With a few lines of code, I think you should be able to turn your jax result into a code that simulates a gas inside a room.  Copute something interesting for this gas.

Random Walks/Markov Chains:

* Implement a path integral Monte Carlo code for a Harmonic oscillator

* Implement an Ising model. 

Predator-Prey:

*   Epidemic Modeling

    * Agent Based Approach:

    * SIR Model


* On the agent evolution, start with 100 foxes and keep track of who is a given fox descendent.  Visualize this in your animation  by color...separately plot the number of descendants of each original fox as a function of time 

* Add evolution to your simulation ... allow foxes and bunnies to adjust speed , when they starve and fraction to reproduce. You’ll need to add these to the class 

* There is an interesting fact I've hear about humans that you don't have to go too many generations back before you are a descendant of everyone or no one.  Model this in an agent-based model.  

* Hp model of protein folding 

* Implement some version of blast 


Fluid Dynamics: 
* Gpu version of lattice Boltzmann 

* Machine learning on lattice Boltzmann fluid dynamics 

* Model moving objects in your fluid dynamics simulation and measure the air resistance to different types of shapes 

* Take your fluid dynamics data and look at different quantities. Measure the curl and density and visualize these side by side


Machine Learning Galaxies: 
* Break 90% using the full dataset.  You can look up whatever you want to pull this off as well as use pytorch, stax, etc. 


Quantum Computing

* Shadow tomography 

Climate Modeling

* Modify your climate modeling to work in 2D

* Modify your climate modeling to deal with seasonal variation of solar insolation.

* E&M:  Implement code that solve poisson's equation for a bunch of wires and point charges.

* Heat Equation: Implement something that takes a bar with heat on the two edges and models how it distributes


* Simulated Annealing: Implement and do some simulated annealing. 


* Impelement the schrodinger equation

* Do diagramtic Monte Carlo
