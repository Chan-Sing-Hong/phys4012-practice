import numpy as np
import matplotlib.pyplot as plt


def x_position(t, v0, theta):
    """Horizontal position x(t)."""
    return v0 * np.cos(theta) * t


def y_position(t, v0, theta, g):
    """Vertical position y(t)."""
    return v0 * np.sin(theta) * t - 0.5 * g * t**2


# Parameters
v0 = 20.0       # m/s
angle_deg = 45.0
g = 9.81        # m/s^2

# Convert degrees to radians explicitly
theta = angle_deg * np.pi / 180.0

# Exact flight time for launch and landing at the same height
flight_time = 2.0 * v0 * np.sin(theta) / g

# 201 equally spaced times, including both endpoints
t = np.linspace(0.0, flight_time, 201)

# Calculate trajectory
x = x_position(t, v0, theta)
y = y_position(t, v0, theta, g)

# Horizontal range
horizontal_range = x[-1]

# Maximum height
max_height = (v0 * np.sin(theta))**2 / (2.0 * g)

# Print results
print(f"Flight time:      {flight_time:.4f} s")
print(f"Horizontal range: {horizontal_range:.4f} m")
print(f"Maximum height:   {max_height:.4f} m")

# Plot trajectory
plt.plot(x, y)

plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Trajectory")

# Equal scale on both axes
plt.axis("equal")
plt.grid()

plt.savefig("projectile_trajectory.png", dpi=300)
plt.show()
