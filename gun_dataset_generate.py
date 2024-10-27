import numpy as np
import pandas as pd

# Constants
g = 9.81  # Gravity (m/s^2)

# Number of samples
num_samples = 50000

# Generate random values for the features
np.random.seed(42)  # For reproducibility
distance_to_target = np.random.uniform(2600, 30000, num_samples)  # meters
initial_velocity = np.random.uniform(800, 829, num_samples)  # m/s (adjusting the range for more variation)
wind_speed = np.random.uniform(0, 20, num_samples)  # m/s
wind_direction = np.random.uniform(0, 360, num_samples)  # degrees

# Function to calculate firing angle based on distance and velocity
def calculate_firing_angle(distance, velocity, wind_speed, wind_direction):
    # Wind's impact on effective velocity
    wind_effect = wind_speed * np.cos(np.radians(wind_direction))
    effective_velocity = velocity + wind_effect
    # Calculate firing angle (adjusting for broader variation)
    angle = 0.5*(180-np.degrees(np.arcsin(distance*g/effective_velocity**2)))
    
    # Add some noise to simulate real-world conditions
    noise = np.random.normal(0, 2, size=angle.shape)  # Increase noise for broader spread
    angle += noise
    
    return np.clip(angle, 0, 90)  # Limiting angles between 0 and 90 degrees

# Calculate the firing angle based on generated features
firing_angle = calculate_firing_angle(distance_to_target, initial_velocity, wind_speed, wind_direction)

# Create a DataFrame with the generated dataset
data = {
    'Distance_to_Target_m': distance_to_target,
    'Initial_Velocity_m_s': initial_velocity,
    'Wind_Speed_m_s': wind_speed,
    'Wind_Direction_deg': wind_direction,
    'Firing_Angle_deg': firing_angle
}

df_synthetic = pd.DataFrame(data)

# Save the dataset to a CSV file
df_synthetic.to_csv('CSV_files/M777_Howitzer_Artillery.csv', index=False)

# Check distribution of angles
print(df_synthetic['Firing_Angle_deg'].describe())
