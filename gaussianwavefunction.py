import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

hbar = 1.0  # Natural units

def compute_gamma_squared(t, m, hbar=1.0):
    """Compute γ² = 1 + (2iħt)/m (more stable than computing sqrt first)."""
    return 1 + (2j * hbar * t) / m

def psi(x, t, a, m, hbar=1.0):
    """Compute the time-dependent Gaussian wave packet."""
    gamma_squared = compute_gamma_squared(t, m, hbar)
    gamma = cmath.sqrt(gamma_squared)  # Only needed for (1/γ) term
    
    prefactor = (2 * a / math.pi) ** (1/4)
    gamma_term = 1 / gamma
    exponent = -(a * x**2) / gamma_squared  # More stable
    exp_term = cmath.exp(exponent)
    

    return prefactor * gamma_term * exp_term

# Test
a, m, x, t = 1.0, 1.0, 0.5, 0.1
wave_function = psi(x, t, a, m)
print(f"ψ({x}, {t}) = {wave_function}")
print(f"Magnitude: {abs(wave_function)}")
print(f"Phase: {cmath.phase(wave_function)} radians")

# Plot
x_vals = np.linspace(-5, 5, 500)
t_fixed =t
psi_vals = [psi(xi, t_fixed, a, m) for xi in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, [z.real for z in psi_vals], label='Real part')
plt.plot(x_vals, [z.imag for z in psi_vals], label='Imaginary part')
plt.xlabel("Position (x)")
plt.ylabel("ψ(x,t)")
plt.title(f"Wave Function at t = {t_fixed}")
plt.legend()
plt.grid(True)
plt.show()

# Probability density over time
times = [0, 0.5, 1.0, 2.0]
plt.figure(figsize=(10, 6))
for t in times:
    psi_vals = [psi(x, t, a, m) for x in x_vals]
    prob_density = [abs(z)**2 for z in psi_vals]  # Correct probability density
    plt.plot(x_vals, prob_density, label=f't = {t}')
plt.xlabel("Position (x)")
plt.ylabel("|ψ(x,t)|²")
plt.title("Probability Density at Different Times")
plt.legend()
plt.grid(True)
plt.show()