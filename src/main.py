"""Run from the repository root with: python -m src.main."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from .model import free_fall


def main():
    initial_height_m = 20.0
    gravity_m_per_s2 = 9.81
    impact_time_s = np.sqrt(2.0 * initial_height_m / gravity_m_per_s2)
    time_s = np.linspace(0.0, impact_time_s, 201)
    height_m, velocity_m_per_s = free_fall(time_s, initial_height_m, gravity_m_per_s2)

    figure, axis = plt.subplots(figsize=(7, 4), constrained_layout=True)
    axis.plot(time_s, height_m)
    axis.set(xlabel="Time (s)", ylabel="Height (m)", title="Free fall from rest")
    axis.grid(alpha=0.25)
    output = Path(__file__).resolve().parents[1] / "figures" / "free_fall.png"
    output.parent.mkdir(exist_ok=True)
    figure.savefig(output, dpi=160)
    plt.close(figure)
    print(f"Impact time: {impact_time_s:.6f} s")
    print(f"Final height: {height_m[-1]:.3e} m")
    print(f"Impact velocity: {velocity_m_per_s[-1]:.6f} m/s")
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
