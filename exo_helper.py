import numpy as np
# Here is a special function for later
# pay no attention to the code behind the curtain...
def get_planet_vxvy_barycentric(mass,t):
    # take the average of the aphelion and perihelion as the distance 
    # between the sun and Jupiter.
    orbit_radius_jupiter = 778.295e9

    # take the average of the aphelion and perihelion as the distance 
    # between the sun and Venus. https://en.wikipedia.org/wiki/Venus 
    orbit_radius_venus = 108.208e9

    # orbital period for Jupiter, from Wikipedia, is 4332.59 days.
    # orbital period for Venus, from Wikipedia, is 224.701 days.
    orbit_period_jupiter = 4332.59 * 24 * 3600
    orbit_period_venus = 224.701 * 24 * 3600
    orbit_period = np.array([0.001, orbit_period_jupiter, orbit_period_venus])
    # create arrays for the vx, vy positions
    theta_now = np.array([-np.pi, 0., 0.]) + t*2*np.pi / orbit_period
    # array of orbital speeds for motion in a heliocentric system:
    orbit_speed_jupiter = 2 * np.pi * orbit_radius_jupiter / orbit_period_jupiter
    orbit_speed_venus = 2 * np.pi * orbit_radius_venus / orbit_period_venus

    orbit_speed = np.array([0.,orbit_speed_jupiter,orbit_speed_venus])

    # now get the velocity components. i am assuming that orbits are circles.
    vxarray, vyarray = -orbit_speed * np.sin(theta_now), orbit_speed * np.cos(theta_now)

    # now calculate center of mass velocities, then subtract that from all 
    # the objects
    vx_cm = np.dot(mass, vxarray) / np.sum(mass)
    vy_cm = np.dot(mass, vyarray) / np.sum(mass)

    # now get the velocity components. i am assuming that orbits are circles.
    vxarray = vxarray - vx_cm
    vyarray = vyarray - vy_cm

    return np.array([vxarray, vyarray])
