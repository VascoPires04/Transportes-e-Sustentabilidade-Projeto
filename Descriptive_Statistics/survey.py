import pandas as pd
import re
import sys
import os

# Reconfigura a saída padrão para UTF-8 (opcional)
sys.stdout.reconfigure(encoding='utf-8')

# Define o diretório de trabalho como o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Caminho para o arquivo, subindo três níveis
file_path = os.path.join("..", "TS_Project_SurveyUBike.xlsx")

# Carregar os dados
df = pd.read_excel(file_path, sheet_name='Raw data', engine='openpyxl')

# Function to assign profile based on decision tree
def assign_profile(row):
    # Extract relevant information from the row
    children_under_10 = row['How many children do you have aged between 6 to 10years?']
    children_under_5 = row['How many children do you have aged between 1 to 5years?']
    children_under_1 = row['How many children do you have aged under 1?']
    travel_time = row['What is your usual travel time to IST, from home? (minutes)']
    intermediate_stops = row['Is there any regular intermediate stop in your daily commuting (morning and/or afternoon)? If yes, chose the most common activity (more that twice a week)? (No - 0; Support to children (e.g., drive/walk children to/from school school) - 1; Support to elderlies - 2; Shopping - 3; Gym/Sports - 4; Work (e.g., working student) - 5; Other - 6)']
    cycling_experience = row['Are you used to cycle in urban areas (besides segregated bike paths)? (No - 0; Yes - 1; A bit - 2)']
    willing_bike_sharing = row['Would you use a bike-sharing system at IST and shift to cycling for daily commuting? (Not interested - 0; Definitely yes, even if it is not electric - 1; Definitely yes, if it is  electric - 2; I have to think - 3)']
    live_district = row['Where do you live (Municipality)?']
    commuting_distance = row['What is the travel distance of your commuting trip? (km)']
    transport_modes = row['In case you don\'t travel by car to IST, which modes are combined in your daily commuting? (1 - walking only; 2 - Private car; 3 - Carpool; 4 - Bus: 5 - Ferry; 6 - Bike; 7 - Rail; 8 - Metro; 9 - motorbike; 10 - IST Shutle; 11 - Taxi; 12 - Other)']
    age = row['Age']
    bike_parking = row['Do you have space to park a bike at home? (No - 0; yes, inside my flat/house - 1; Yes, in the building / garage - 1;  Yes, in a sheltered space (balcony, backyard, etc.) - 3; Yes, in an unsheltered space (balcony, backyard, etc.) - 4)']
    
    # List of municipalities considered as Lisboa district north
    lisboa_district_north = ["Lisboa", "Loures", "Odivelas", "Amadora", "Sintra", "Oeiras", "Cascais"]

     
    if children_under_10 !=0 or children_under_5 != 0 or children_under_1 != 0:
        if travel_time > 30:
            return 0
        else:
            if intermediate_stops == 1:
                return 0
            else:
                if cycling_experience in [1, 2]:  # "Yes" or "A bit"
                    if willing_bike_sharing in [1, 2, 3]:
                        return 2
                    else:
                        return 0
                else:
                    return 0
    else:
        if live_district not in lisboa_district_north:
            if willing_bike_sharing in [1, 2, 3]:
                return 3
            else:
                return 0
        else:
            if commuting_distance > 7:
                if cycling_experience in [1, 2]:
                    if willing_bike_sharing in [1, 2, 3]:
                        return 2
                    else:
                        return 3
                else:
                    return 0
            else:
                if any(mode in ["1", "4", "5", "6", "7", "8"] for mode in str(transport_modes).split(',')):
                    if cycling_experience in [1, 2]:
                        if bike_parking != 0:
                            if willing_bike_sharing == 1:
                                return 1
                            elif willing_bike_sharing in [2, 3]:
                                return 2
                            else:
                                return 3
                        else:
                            if willing_bike_sharing == 1:
                                return 1
                            elif willing_bike_sharing == 2:
                                return 2
                            else:
                                return 0
                    else:
                        if age > 40:
                            if willing_bike_sharing == 1:
                                return 1
                            elif willing_bike_sharing == 2:
                                return 2
                            else:
                                return 0
                        else:
                            if bike_parking != 0:
                                if willing_bike_sharing == 1:
                                    return 1
                                elif willing_bike_sharing == 2:
                                    return 2
                                else:
                                    return 3
                            else:
                                if willing_bike_sharing == 1:
                                    return 1
                                elif willing_bike_sharing == 2:
                                    return 2
                                else:
                                    return 0
                else:
                    if age > 50:
                        if willing_bike_sharing in [1, 2]:
                            return 2
                        else:
                            return 0
                    else:
                        if intermediate_stops in [1, 2]:
                            if willing_bike_sharing in [1, 2]:
                                return 3
                            else:
                                return 0
                        else:
                            if cycling_experience in [1, 2]:
                                if willing_bike_sharing == 1:
                                    return 1
                                elif willing_bike_sharing == 2:
                                    return 2
                                else:
                                    return 3
                            else:
                                return 0

# Apply the function to each row and create a new column 'Profile'
df['Profile'] = df.apply(assign_profile, axis=1)

# Save the updated DataFrame to the SAME Excel file without overwriting the existing content
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, sheet_name='Raw data', index=False)
