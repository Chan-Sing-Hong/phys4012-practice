"""Starter model: an object dropped from rest, with upward-positive height."""

import numpy as np


def free_fall(time_s, initial_height_m=20.0, gravity_m_per_s2=9.81):
    """Return height (m) and vertical velocity (m/s), valid before impact."""
    time_s = np.asarray(time_s)
    height_m = initial_height_m - 0.5 * gravity_m_per_s2 * time_s**2
    velocity_m_per_s = -gravity_m_per_s2 * time_s
    return height_m, velocity_m_per_s
