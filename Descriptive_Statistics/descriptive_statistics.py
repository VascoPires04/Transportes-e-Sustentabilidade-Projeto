import os
import pandas as pd

# Define o diretório de trabalho como o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Caminho relativo para o arquivo no diretório pai
file_path = os.path.join("..", "TS_Project_SurveyUBike.xlsx")

# Load the dataset
df = pd.read_excel("../TS_Project_SurveyUBike.xlsx", sheet_name='Raw data')

# Prepare a dictionary to hold the descriptive statistics
descriptive_stats = {}

# 1. Unique IDs
descriptive_stats['Unique IDs'] = df['ID'].nunique()

# 2. Who are you?
who_distribution = df['Who are you? (Student - 1; Faculty or researcher - 2; Staff - 3)'].value_counts(normalize=True) * 100
descriptive_stats['Who are you?'] = who_distribution

# 3. Which campus of IST?
campus_distribution = df['Which campus of IST? (Campus Tecnológico e Nuclear - 0; Alameda - 1; Tagus Park - 2)'].value_counts(normalize=True) * 100
descriptive_stats['Campus Distribution'] = campus_distribution

# 4. Age
descriptive_stats['Average Age'] = df['Age'].mean()
descriptive_stats['Age Standard Deviation'] = df['Age'].std()
descriptive_stats['Age Minimum'] = df['Age'].min()
descriptive_stats['Age Maximum'] = df['Age'].max()

# 5. Gender Distribution
gender_distribution = df['Gender (Female - 1)'].value_counts(normalize=True) * 100
descriptive_stats['Gender Distribution'] = gender_distribution

# 6. Where do you live (Municipality)?
municipality_distribution = df['Where do you live (Municipality)?'].value_counts(normalize=True) * 100
descriptive_stats['Municipality Distribution'] = municipality_distribution

# 7. Number of children aged under 1
descriptive_stats['Average Children Under 1'] = df['How many children do you have aged under 1?'].mean()
descriptive_stats['Children Under 1 Standard Deviation'] = df['How many children do you have aged under 1?'].std()

# 8. Number of children aged between 1 to 5 years
descriptive_stats['Average Children Aged 1 to 5'] = df['How many children do you have aged between 1 to 5years?'].mean()
descriptive_stats['Children Aged 1 to 5 Standard Deviation'] = df['How many children do you have aged between 1 to 5years?'].std()

# 9. Number of children aged between 6 to 10 years
descriptive_stats['Average Children Aged 6 to 10'] = df['How many children do you have aged between 6 to 10years?'].mean()
descriptive_stats['Children Aged 6 to 10 Standard Deviation'] = df['How many children do you have aged between 6 to 10years?'].std()

# 10. Number of children aged between 11 to 15 years
descriptive_stats['Average Children Aged 11 to 15'] = df['How many children do you have aged between 11 to 15years?'].mean()
descriptive_stats['Children Aged 11 to 15 Standard Deviation'] = df['How many children do you have aged between 11 to 15years?'].std()

# 11. Number of children aged more than 15 years
descriptive_stats['Average Children Aged More Than 15'] = df['How many children do you have aged more than 15years?'].mean()
descriptive_stats['Children Aged More Than 15 Standard Deviation'] = df['How many children do you have aged more than 15years?'].std()

# 12. Vehicle Usage Distribution
vehicle_distribution = df['Do you usually come to IST in your private vehicle? (no - 1; yes, with a car - 2; yes, with a motorbike - 3)'].value_counts(normalize=True) * 100
descriptive_stats['Vehicle Usage Distribution'] = vehicle_distribution

# 13. Average Travel Time to IST
descriptive_stats['Average Travel Time (minutes)'] = df['What is your usual travel time to IST, from home? (minutes)'].mean()
descriptive_stats['Travel Time Standard Deviation'] = df['What is your usual travel time to IST, from home? (minutes)'].std()
descriptive_stats['Travel Time Minimum'] = df['What is your usual travel time to IST, from home? (minutes)'].min()
descriptive_stats['Travel Time Maximum'] = df['What is your usual travel time to IST, from home? (minutes)'].max()

# 14. Modes combined in daily commuting
combined_modes_distribution = df['In case you don\'t travel by car to IST, which modes are combined in your daily commuting? (1 - walking only; 2 - Private car; 3 - Carpool; 4 - Bus: 5 - Ferry; 6 - Bike; 7 - Rail; 8 - Metro; 9 - motorbike; 10 - IST Shutle; 11 - Taxi; 12 - Other)'].value_counts(normalize=True) * 100
descriptive_stats['Combined Modes Distribution'] = combined_modes_distribution

# 15. Regular intermediate stops
intermediate_stops_distribution = df['Is there any regular intermediate stop in your daily commuting (morning and/or afternoon)? If yes, chose the most common activity (more that twice a week)? (No - 0; Support to children (e.g., drive/walk children to/from school school) - 1; Support to elderlies - 2; Shopping - 3; Gym/Sports - 4; Work (e.g., working student) - 5; Other - 6)'].value_counts(normalize=True) * 100
descriptive_stats['Intermediate Stops Distribution'] = intermediate_stops_distribution

# 16. Do you have a Transit monthly card?
transit_card_distribution = df['Do you have a Transit monthly card? (Yes - 1)'].value_counts(normalize=True) * 100
descriptive_stats['Transit Monthly Card Distribution'] = transit_card_distribution

# 17. Travel distance
descriptive_stats['Average Travel Distance (km)'] = df['What is the travel distance of your commuting trip? (km)'].mean()
descriptive_stats['Travel Distance Standard Deviation'] = df['What is the travel distance of your commuting trip? (km)'].std()
descriptive_stats['Travel Distance Minimum'] = df['What is the travel distance of your commuting trip? (km)'].min()
descriptive_stats['Travel Distance Maximum'] = df['What is the travel distance of your commuting trip? (km)'].max()

# 18. Fuel type of car
fuel_type_distribution = df['What is the fuel type of your car (if you use car to come to IST)? (Diesel or Diesel Hybrid - 1; Petrol or Hybrid petrol - 2; LPG - 3; Electric - 4)'].value_counts(normalize=True) * 100
descriptive_stats['Fuel Type Distribution'] = fuel_type_distribution

# 19. Type of vehicle owned
vehicle_type_distribution = df['What type of vehicle to you own or us to come to IST? (City car - 1; Utilitarian - 2; Break - 3; MPV - 4; SUV - 5; Bigger engines (>3ltrs) - 6; Scooter - 7; Motorbike (>12cc) - 8)'].value_counts(normalize=True) * 100
descriptive_stats['Vehicle Type Distribution'] = vehicle_type_distribution

# 20. Average consumption of vehicle
descriptive_stats['Average Vehicle Consumption (lt/100km)'] = df['Do you know what is the average consumption of your vehicle (lt/100km)?'].mean()
descriptive_stats['Vehicle Consumption Standard Deviation'] = df['Do you know what is the average consumption of your vehicle (lt/100km)?'].std()

# 21. Urban cycling experience
cycling_experience_distribution = df['Are you used to cycle in urban areas (besides segregated bike paths)? (No - 0; Yes - 1; A bit - 2)'].value_counts(normalize=True) * 100
descriptive_stats['Urban Cycling Experience Distribution'] = cycling_experience_distribution

# 22. Interest in bike-sharing system
bike_sharing_interest_distribution = df['Would you use a bike-sharing system at IST and shift to cycling for daily commuting? (Not interested - 0; Definitely yes, even if it is not electric - 1; Definitely yes, if it is  electric - 2; I have to think - 3)'].value_counts(normalize=True) * 100
descriptive_stats['Bike Sharing Interest Distribution'] = bike_sharing_interest_distribution

# 23. Space to park a bike at home
bike_parking_space_distribution = df['Do you have space to park a bike at home? (No - 0; yes, inside my flat/house - 1; Yes, in the building / garage - 1;  Yes, in a sheltered space (balcony, backyard, etc.) - 3; Yes, in an unsheltered space (balcony, backyard, etc.) - 4)'].value_counts(normalize=True) * 100
descriptive_stats['Bike Parking Space Distribution'] = bike_parking_space_distribution

# 24. Floor of residence
floor_distribution = df['If you live in a building, which floor do you live in? (note: "0" - ground floor; "-1" - basement; "-2" - sub-basement; "5" - higher than 4th floor)'].value_counts(normalize=True) * 100
descriptive_stats['Floor Distribution'] = floor_distribution

# 25. Profile Distribution decision tree
profile_distribution_dt = df['Profile'].value_counts()
descriptive_stats['Profile Distribution for the Decision Tree'] = profile_distribution_dt

# 26. Profile Distribution survey
profile_distribution_s = df['Would you use a bike-sharing system at IST and shift to cycling for daily commuting? (Not interested - 0; Definitely yes, even if it is not electric - 1; Definitely yes, if it is  electric - 2; I have to think - 3)'].value_counts()
descriptive_stats['Profile Distribution for the Survey'] = profile_distribution_s

# Save the descriptive statistics to a .txt file
output_file_path = 'Descriptive_Statistics.txt'  # Change the path as needed
with open(output_file_path, 'w') as f:
    for key, value in descriptive_stats.items():
        f.write(f"{key}:\n")
        if isinstance(value, pd.Series):
            f.write(value.to_string() + '\n')  # Convert Series to string for better formatting
        else:
            f.write(f"{value}\n")
        f.write('\n' * 2)  # Add extra newlines for better readability

print(f"Descriptive statistics saved to: {output_file_path}")
