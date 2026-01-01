# projectile-motion-simulation

A small Python project to simulate projectile motion with and without air resistance. The repository contains a simulation script that computes trajectories for varying launch angles and initial speeds, exports a CSV of experimental results, and saves plots illustrating the motion and the relationship between drag coefficient and optimal launch angle.

**Features**
- Simulate projectile trajectories using Euler integration with optional air drag.
- Run experiments varying launch angle or initial velocity.
- Produce PNG plots for trajectories and for optimal angle vs drag coefficient.
- Export experiment results to `projectile_experiment_results.csv`.

**Requirements**
- Python 3.8+ (tested with 3.10)
- `matplotlib`
- `pandas`

Install dependencies with:

```bash
pip install -r requirements.txt
# or
pip install matplotlib pandas
```

**Usage**
Run the simulation script with Python:

```bash
python projectile.py
```

This will:
- Generate trajectory plots (PNG files) for the experiments in the script.
- Create `projectile_experiment_results.csv` containing drag coefficient vs optimal angle.
- Save `optimal_angle_vs_drag_coefficient.png` showing the optimal launch angle as a function of drag.

**Files produced by the script**
- `projectile_experiment_results.csv` — tabulated optimal angles for drag coefficients.
- `optimal_angle_vs_drag_coefficient.png` — plot of optimal angle vs drag coefficient.
- `projectile_motion_with_various_angles_no_air_resistance.png` and
	`projectile_motion_with_various_velocities_no_air_resistance.png` — example trajectory plots.

**Notes & next steps**
- The simulation uses a simple Euler integration and a linear drag model proportional to velocity. In the future, I would like to extend this to have quadratic drag models which are more realistic.
- You can change initial conditions or drag settings by editing `projectile.py`.

**Observations
- As the drag coefficient increased, the optimal angle for the maximum horizontal distance reduces indicating that ball should not spend a lot of time in the air.
- In an ideal condition, the optimal angle for maximum horizontal distance was 45 degrees.
- For a given launch angle, increases in initial velocity results in increased maximum horizontal distances.
- The projectile reaches the maximum height when the initial launch angle is 90 degrees.
