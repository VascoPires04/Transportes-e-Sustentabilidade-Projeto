import matplotlib.pyplot as plt
import numpy as np

# Data
pollutants = ['CO', 'NOx', 'PM', 'VOC', 'CO2e']
times = ['off', 'peak']

# Updated emission values in kg for each pollutant (before and after)
emissions_before = {
    'CO': [8.44, 9.56],
    'NOx': [3.34, 4.95],
    'PM': [0.12, 0.13],
    'VOC': [1.13, 1.26],
    'CO2e': [1714.55, 1840.51]
}

emissions_after = {
    'CO': [5.41, 6.12],
    'NOx': [2.44, 3.57],
    'PM': [0.09, 0.10],
    'VOC': [0.73, 0.82],
    'CO2e': [1183.13, 1268.31]
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
