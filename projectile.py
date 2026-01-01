import math
import matplotlib.pyplot as plt
import pandas as pd

"""
A class to simulate projectile motion with air resistance. It takes the initial velocity, angle of projection, drag coefficient, and time steps as inputs. The simulate method computes the trajectory of
It models the projectile motion considering air resistance proportional to the velocity and the mass of the projectile.
It uses Euler's method to update the position and velocity of the projectile at each time step until it hits the ground (y < 0).
The x and y coordinates of the projectile's trajectory at each time step are stored in lists for further analysis or plotting.
"""
class ProjectileWithAirResistance:
    def __init__(self, initial_velocity, angle_of_projection_in_degrees, drag_coefficient = 0.2, time_steps = 0.01):
        self.initial_velocity = initial_velocity
        self.angle_of_projection_in_radians = angle_of_projection_in_degrees * math.pi / 180
        self.drag_coefficient = drag_coefficient
        self.time_steps = time_steps
        self.x_coordinates = []
        self.y_coordinates = []
        self.g = 9.8
        self.mass_of_projectile = 10.0

    def simulate(self):
        x = 0.0
        y = 0.0
        self.x_coordinates.append(x)
        self.y_coordinates.append(y)
        vx = self.initial_velocity * math.cos(self.angle_of_projection_in_radians)
        vy = self.initial_velocity * math.sin(self.angle_of_projection_in_radians)
        while y >= 0:
            x = x + vx * self.time_steps
            y = y + vy * self.time_steps
            
            self.x_coordinates.append(x)
            self.y_coordinates.append(y)
            vx = vx - self.time_steps * ((self.drag_coefficient * vx) / self.mass_of_projectile)
            vy = vy - self.time_steps * ((self.drag_coefficient * vy ) / self.mass_of_projectile + self.g)
        
'''
ProjectileExperiment is a base class for conducting projectile motion experiments.
It provides methods to plot the results and a placeholder for simulation that must be implemented by subclasses.
'''
class ProjectileExperiment:
    def __init__(self):
        self.all_x_coordinates = []
        self.all_y_coordinates = []
        self.legend = None

    def plot(self, name_of_experiment):
        if self.legend is None:
            raise ValueError("Legend not set. Please run the simulation first.")
        
        for i in range(len(self.all_x_coordinates)):
            plt.plot(self.all_x_coordinates[i], self.all_y_coordinates[i], linestyle = '-')
            plt.legend(self.legend)
        plt.title("Projectile Motion Trajectory")
        plt.xlabel("Horizontal Distance (meters)")
        plt.ylabel("Vertical Distance (meters)")
        
        plt.title("Projectile Motion Trajectory")
        plt.xlabel("Horizontal Distance (meters)")
        plt.ylabel("Vertical Distance (meters)")
        plt.grid(True)
        plt.savefig(f"{name_of_experiment}.png", dpi=300)
        plt.show()
        plt.close()

    def simulate(self):
        raise NotImplementedError("Subclasses should implement this method.")

'''
ProjectileExperimentWithAngles conducts projectile motion experiments varying the launch angle.
It simulates the projectile motion for a set of angles and identifies the angle that yields the maximum
range. It stores the trajectory data for plotting. This is a derived class from ProjectileExperiment.
'''
class ProjectileExperimentWithAngles(ProjectileExperiment):
    def __init__(self, drag_coefficient, angles = None):
        super().__init__()
        self.angles = [15, 30, 45, 60, 75] if angles is None else angles
        self.initial_velocity = 20
        self.drag_coefficient = drag_coefficient
        self.tabulated_data = {}
        
    def simulate(self):
        max_x = 0
        best_angle = None
        for angle in self.angles:
            projectile = ProjectileWithAirResistance(self.initial_velocity, angle, self.drag_coefficient)
            projectile.simulate()
            self.all_x_coordinates.append(projectile.x_coordinates)
            self.all_y_coordinates.append(projectile.y_coordinates)
            # Find the angle that gives the maximum range
            if max_x < projectile.x_coordinates[-1]:
                max_x = projectile.x_coordinates[-1]
                best_angle = angle
        self.legend = [f"{angle} degrees" for angle in self.angles]
        return best_angle, max_x


'''
ProjectileExperimentWithVelocities conducts projectile motion experiments varying the initial velocity.
It simulates the projectile motion for a set of velocities at a fixed angle and stores the trajectory data for plotting.
This is a derived class from ProjectileExperiment.'''
class ProjectileExperimentWithVelocities(ProjectileExperiment):
    def __init__(self, drag_coefficient):
        super().__init__()
        self.velocities = [10, 20, 30, 40, 50]
        self.angle_of_projection = 45
        self.drag_coefficient = drag_coefficient
        
    def simulate(self):
        for velocity in self.velocities:
            projectile = ProjectileWithAirResistance(velocity, self.angle_of_projection, self.drag_coefficient)
            projectile.simulate()
            self.all_x_coordinates.append(projectile.x_coordinates)
            self.all_y_coordinates.append(projectile.y_coordinates)
        self.legend = [f"{velocity} m/s" for velocity in self.velocities]

def main():
    # Initial experiment to plot the projectile motion for various angles and velocities without air resistance
    p = ProjectileExperimentWithAngles(0.0)
    p.simulate()
    p.plot("projectile_motion_with_various_angles_no_air_resistance")
    p = ProjectileExperimentWithVelocities(0.0)
    p.simulate()
    p.plot("projectile_motion_with_various_velocities_no_air_resistance")

    # Experiment to find the optimal angle for various drag coefficients
    drag_coefficients = []
    best_angles = []
    distances = []
    drag_coefficient = 0.0
    interesting_angles = list(range(1, 91))  # 1 to 90 degrees
    while drag_coefficient <= 10.0:
        p = ProjectileExperimentWithAngles(drag_coefficient, interesting_angles)
        (angle, distance) = p.simulate()
        drag_coefficients.append(drag_coefficient)
        best_angles.append(angle)
        distances.append(distance)
        drag_coefficient += 0.2
    
    df = pd.DataFrame({
        "Drag Coefficient": drag_coefficients,
        "Optimal Angle (degrees)": best_angles,
    })
    df.to_csv("projectile_experiment_results.csv", index = False)
    ax = df.plot(kind = 'line', x = "Drag Coefficient", y = "Optimal Angle (degrees)", marker = '*', title = "Optimal Angle vs Drag Coefficient", grid = True)
    ax.set_ylabel('Launch angle (in degrees)')
    ax.set_xlabel('Drag Coefficient')
    plt.savefig("optimal_angle_vs_drag_coefficient.png", dpi=300)
    plt.show()
    print(df.to_string(index = False))

if __name__ == '__main__':
    main()