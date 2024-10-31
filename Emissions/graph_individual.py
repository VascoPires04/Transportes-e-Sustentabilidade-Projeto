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

# Set up individual plots for each pollutant
width = 0.2  # bar width
for pollutant in pollutants:
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Data for this pollutant
    off_before = emissions_before[pollutant][0]
    off_after = emissions_after[pollutant][0]
    peak_before = emissions_before[pollutant][1]
    peak_after = emissions_after[pollutant][1]
    
    # X positions for the bars
    x = np.arange(2)  # two time periods: off and peak
    
    # Plotting bars for before and after, off-peak and peak emissions
    bars1 = ax.bar(x - width, [off_before, peak_before], width, label='Before', color='#800020')
    bars2 = ax.bar(x + width, [off_after, peak_after], width, label='After', color='#008080')
    
    # Apply log scale for better visibility
    #ax.set_yscale('log')
    
    # Labeling
    ax.set_xlabel('Time Period')
    ax.set_ylabel('Total Emissions (kg, log scale)')
    ax.set_title(f'Total Emissions for {pollutant} Before and After by Time Period')
    ax.set_xticks(x)
    ax.set_xticklabels(['Off-Peak', 'Peak'])
    ax.legend(loc='upper right')
    
    # Display each plot separately
    plt.tight_layout()
    plt.show()
