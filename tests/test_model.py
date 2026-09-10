"""One independent physical check; replace it when you replace the model."""

import unittest

import numpy as np

from src.model import free_fall


class FreeFallPhysicsTest(unittest.TestCase):
    def test_mechanical_energy_is_conserved_before_impact(self):
        # The invariant couples height and velocity, catching inconsistent dynamics.
        gravity_m_per_s2 = 9.81
        initial_height_m = 20.0
        time_s = np.linspace(0.0, 1.5, 17)
        height_m, velocity_m_per_s = free_fall(time_s, initial_height_m, gravity_m_per_s2)
        energy_per_mass = 0.5 * velocity_m_per_s**2 + gravity_m_per_s2 * height_m
        expected_energy_per_mass = gravity_m_per_s2 * initial_height_m
        self.assertTrue(np.all(np.isfinite(energy_per_mass)))
        np.testing.assert_allclose(
            energy_per_mass, expected_energy_per_mass, rtol=1e-12, atol=1e-12
        )


if __name__ == "__main__":
    unittest.main()
