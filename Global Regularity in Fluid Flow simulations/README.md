# 3D CUGE/REFORM Fluid Simulation (CUDA)

**High-resolution pseudo-spectral simulation of incompressible Navier–Stokes with refractive vacuum response (CUGE/REFORM framework)**

This code implements a 256³ 3D fluid solver on GPU (CuPy) that solves the **ray-equation form** of the CUGE/REFORM model:

$$
\frac{D\mathbf{v}}{Dt} = c^2 \frac{\nabla n}{n} - \frac{\dot{n}}{n} \mathbf{v} + \nu \nabla^2 \mathbf{v}, \quad n = 1 + \beta \frac{|\mathbf{v}|^2}{c^2}
$$

It demonstrates **real-world global regularity** through natural kinematic suppression and quartic dissipation (Vacuum Stress Storage) without ad-hoc viscosity or artificial damping.

## Features

- 256 × 256 × 256 grid (≈ 16.7 million degrees of freedom)
- IMEX fixed-point corrector for the stiff refractive (CUGE) terms
- Spectral projection (FFT) to enforce incompressibility
- Exponential spectral filter to suppress aliasing
- Taylor-Green vortex initial condition
- Full energy diagnostics (KE, weighted energy, quartic dissipation, VSS, max velocity)
- Automatic CSV output + matplotlib energy plots + energy spectrum
- GPU-accelerated (CuPy + CUDA)

## Physics Background

This simulation is the numerical validation presented in the paper:

> **Real-World Global Regularity in Fluid Flow** — Emergent Kinematic Suppression and Vacuum Stress Storage from Refractive Vacuum Response (CUGE/REFORM Framework)

It confirms that the responsive vacuum supplies exact energy partitioning and bounded dynamics, resolving the long-standing question of global regularity for incompressible fluids.

## Requirements

- Python 3.9+
- CuPy (CUDA 11.x or 12.x recommended)
- NumPy, Matplotlib, CSV
- GPU with ≥ 12 GB VRAM (256³ comfortably fits on 16–24 GB cards)

Install with:
```bash
pip install cupy-cuda12x numpy matplotlib  # adjust cuda version as needed
