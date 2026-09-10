import numpy as np
import matplotlib.pyplot as plt


def damped_oscillation(t, A, gamma, omega):
    """Return x(t) = A exp(-gamma t) cos(omega t)."""
    return A * np.exp(-gamma * t) * np.cos(omega * t)


# Parameters
A = 1.0          # metres
gamma = 0.15     # 1/s
omega = 2.0      # radians/s

# 1001 equally spaced points from 0 to 20 s, including both endpoints
t = np.linspace(0.0, 20.0, 1001)

# Calculate displacement
x = damped_oscillation(t, A, gamma, omega)

# Exponential envelopes
upper_envelope = A * np.exp(-gamma * t)
lower_envelope = -A * np.exp(-gamma * t)

# Plot
plt.plot(t, x, label="x(t)")
plt.plot(t, upper_envelope, "--", label="Upper envelope")
plt.plot(t, lower_envelope, "--", label="Lower envelope")

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Damped Oscillation")
plt.legend()
plt.grid()

# Save before plt.show()
plt.savefig("damped_oscillation.png", dpi=300)
plt.show()
