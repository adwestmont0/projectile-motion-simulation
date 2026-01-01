# Projectile Motion with Air Resistance  
*A Physics & Engineering Simulation in Python*

## Overview

This project simulates **two-dimensional projectile motion** under the influence of gravity and air resistance using numerical methods. The simulation compares ideal projectile motion (no air resistance) with more realistic motion that includes **linear air drag**, and investigates how air resistance affects trajectory shape, range, and the **optimal launch angle**.

Rather than relying on closed-form equations, this project uses **time-stepping numerical simulation (Euler’s method)**, similar to how real engineering and physics simulations are performed.

---

## Key Questions Explored

- How does air resistance change the trajectory of a projectile?
- How does increasing drag affect the projectile’s range?
- How does air resistance change the *optimal* launch angle?
- Why is 45° no longer optimal when drag is present?

---

## Numerical Method

The motion is simulated using **Euler’s method**, which updates velocity and position in small time steps:

1. Compute acceleration from forces  
2. Update velocity  
3. Update position  
4. Repeat until the projectile reaches the ground  

This approach avoids calculus-heavy formulas and demonstrates how computers approximate continuous physical systems.

---

## Project Structure

### Core Classes

- **`ProjectileWithAirResistance`**
  - Simulates the motion of a single projectile
  - Models gravity and linear air drag
  - Stores full trajectory data (x and y coordinates)

- **`ProjectileExperiment`**
  - Base class for running and plotting experiments
  - Handles visualization of multiple trajectories

- **`ProjectileExperimentWithAngles`**
  - Varies launch angle
  - Determines which angle produces maximum range for a given drag coefficient

- **`ProjectileExperimentWithVelocities`**
  - Varies initial velocity at a fixed angle
  - Compares resulting trajectories

---

## Requirements
- Python 3.8+ (tested with 3.10)
- `matplotlib`
- `pandas`

Install dependencies with:

```bash
pip install -r requirements.txt
# or
pip install matplotlib pandas
```

## Usage
Run the simulation script with Python:

```bash
python projectile.py
```

## Experiments Conducted

### 1. Trajectory Comparison (No Air Resistance)

- Multiple launch angles
- Multiple initial velocities
- Confirms expected symmetric parabolic motion

### 2. Optimal Launch Angle vs Drag Coefficient

- Launch angles from 1° to 90°
- Drag coefficient varied from 0.0 to 10.0
- For each drag value, the angle producing the maximum range is recorded

Results are:
- Saved to a CSV file for analysis
- Visualized using matplotlib and pandas

---

## Key Observations

- Without air resistance, the optimal launch angle is approximately **45°**
- As air resistance increases:
  - Projectile range decreases significantly
  - Optimal launch angle shifts **below 45°**
- Strong drag favors **lower launch angles**, since vertical motion loses energy more quickly than horizontal motion
- For a given launch angle, increases in initial velocity results in increased maximum horizontal distances.
- The projectile reaches the maximum height when the initial launch angle is 90 degrees.

These results match known physical behavior and demonstrate the impact of drag on real-world motion.

---

## Output Files

- Trajectory plots for different angles and velocities
- `optimal_angle_vs_drag_coefficient.png`
- `projectile_experiment_results.csv` (tabulated data)

---

## Possible Extensions

- Implement **quadratic drag** for higher-speed projectiles
- Compare Euler vs Euler–Cromer methods
- Analyze time of flight and velocity vs time
- Create heatmaps of range vs angle and drag

---

## Motivation

This project was created to explore physics concepts through programming rather than relying solely on analytical equations. It demonstrates how numerical methods are used in engineering and scientific research to model systems that cannot be solved exactly.

---

