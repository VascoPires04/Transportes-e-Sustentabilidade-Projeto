import matplotlib.pyplot as plt
import numpy as np

# Data
pollutants = ['CO', 'NOx', 'PM', 'VOC', 'CO2e']
times = ['off', 'peak']

# Emission values in kg for each pollutant (before and after)
emissions_before = {
    'CO': [14.5, 14.77],
    'NOx': [9.3, 29.09],
    'PM': [0.59, 0.6],
    'VOC': [2.97, 2.98],
    'CO2e': [4465.26, 4577.98]
}

emissions_after = {
    'CO': [9.62, 9.69],
    'NOx': [6.5, 20.11],
    'PM': [0.41, 0.42],
    'VOC': [2.0, 2.0],
    'CO2e': [3072.34, 3148.84]
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
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display
plt.tight_layout()
plt.show()
