import numpy as np
import matplotlib.pyplot as plt


def damped_signal(t, A, gamma, omega):
    """x(t) = A exp(-gamma t) cos(omega t)."""
    return A * np.exp(-gamma * t) * np.cos(omega * t)


def exact_derivative(t, A, gamma, omega):
    """Analytic derivative dx/dt."""
    return (
        A * np.exp(-gamma * t)
        * (-gamma * np.cos(omega * t)
           - omega * np.sin(omega * t))
    )


def centred_derivative(t, h, A, gamma, omega):
    """Centred-difference approximation to dx/dt."""
    return (
        damped_signal(t + h, A, gamma, omega)
        - damped_signal(t - h, A, gamma, omega)
    ) / (2.0 * h)


# Parameters from Exercise 1
A = 1.0
gamma = 0.15
omega = 2.0

# Fixed evaluation times.
# These times DO NOT change when h changes.
t = np.linspace(1.0, 19.0, 501)

# Exact derivative at the fixed evaluation times
dx_exact = exact_derivative(t, A, gamma, omega)

# Values of h: 0.4 / 2**k for k = 0, ..., 30
k_values = np.arange(31)
h_values = 0.4 / (2.0 ** k_values)

errors = []

for h in h_values:
    dx_numeric = centred_derivative(t, h, A, gamma, omega)

    # Maximum absolute error over the same 501 points
    error = np.max(np.abs(dx_numeric - dx_exact))
    errors.append(error)

errors = np.array(errors)

# Print errors and ratios
print(" k          h                 max error          previous/current")
print("----------------------------------------------------------------")

for k in range(len(h_values)):
    if k == 0:
        print(f"{k:2d}  {h_values[k]:.12e}  {errors[k]:.12e}")
    else:
        ratio = errors[k - 1] / errors[k]
        print(
            f"{k:2d}  {h_values[k]:.12e}  "
            f"{errors[k]:.12e}  {ratio:.6f}"
        )

# Plot error versus h
plt.loglog(h_values, errors, "o-")

plt.xlabel("Step size h (s)")
plt.ylabel("Maximum absolute derivative error (m/s)")
plt.title("Centred-Difference Error")
plt.grid(True, which="both")

plt.savefig("centred_difference_error.png", dpi=300)
plt.show()
