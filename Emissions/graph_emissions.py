import matplotlib.pyplot as plt
import numpy as np

# Data
pollutants = ['CO', 'NOx', 'PM', 'VOC', 'CO2e']
times = ['off', 'peak']

# Updated emission values in kg for each pollutant (before and after)
emissions_before = {
    'CO': [8.54, 9.67],
    'NOx': [3.58, 5.06],
    'PM': [0.13, 0.14],
    'VOC': [1.14, 1.28],
    'CO2e': [1908.1, 2040.41]
}

emissions_after = {
    'CO': [5.44, 6.15],
    'NOx': [2.6, 3.64],
    'PM': [0.1, 0.1],
    'VOC': [0.73, 0.82],
    'CO2e': [1320.55, 1409.76]
}

# Set up bar plot
x = np.arange(len(pollutants))  # pollutant indices
width = 0.15  # narrower bar width to prevent overlap

fig, ax = plt.subplots(figsize=(10, 6))

# Bars for off-peak and peak emissions
off_before = [emissions_before[p][0] for p in pollutants]
off_after = [emissions_after[p][0] for p in pollutants]
peak_before = [emissions_before[p][1] for p in pollutants]
peak_after = [emissions_after[p][1] for p in pollutants]

# Plotting bars with consistent colors
bars1 = ax.bar(x - width * 1.5, off_before, width, label='Before (Off-Peak)', color='red')
bars2 = ax.bar(x - width / 2, off_after, width, label='After (Off-Peak)', color='#66b266')
bars3 = ax.bar(x + width / 2, peak_before, width, label='Before (Peak)', color='orange')
bars4 = ax.bar(x + width * 1.5, peak_after, width, label='After (Peak)', color='lightblue')

# Apply log scale for better visibility of smaller values
ax.set_yscale('log')

# Labeling
ax.set_xlabel('Pollutants')
ax.set_ylabel('Total Emissions (kg, log scale)')
ax.set_title('Total Emissions Before and After by Pollutant and Time Period')
ax.set_xticks(x)
ax.set_xticklabels(pollutants)
ax.legend(loc='upper left')

# Display
plt.tight_layout()
plt.show()
