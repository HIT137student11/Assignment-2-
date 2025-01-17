import os
import csv
from collections import defaultdict

# Function to calculate average temperature for each month
def calculate_average_temperature():
    temperature_data = defaultdict(list)
    years = os.listdir('temperatures')

    # Read data from all CSV files
    for year in years:
        with open(f'temperatures/{year}', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                month = int(row[0])  # Assuming first column is month
                temperature = float(row[1])  # Assuming second column is temperature
                temperature_data[month].append(temperature)

    # Calculate average temperature for each month
    avg_temp = {month: sum(temps) / len(temps) for month, temps in temperature_data.items()}

    # Save the result to "average_temp.txt"
    with open('average_temp.txt', 'w') as file:
        for month, avg in avg_temp.items():
            file.write(f"Month: {month}, Average Temperature: {avg:.2f}\n")



            # Function to find the station with the largest temperature range
def find_largest_temp_range():
    stations = os.listdir('temperatures')
    temp_ranges = {}

    for station in stations:
        with open(f'temperatures/{station}', 'r') as file:
            reader = csv.reader(file)
            temperatures = [float(row[1]) for row in reader]
            temp_range = max(temperatures) - min(temperatures)
            temp_ranges[station] = temp_range

    # Find the station with the largest temperature range
    max_range_station = max(temp_ranges, key=temp_ranges.get)

    # Save the result to "largest_temp_range_station.txt"
    with open('largest_temp_range_station.txt', 'w') as file:
        file.write(f"Station with largest temperature range: {max_range_station}\n")

# Function to find the station with the largest temperature range
def find_largest_temp_range():
    stations = os.listdir('temperatures')
    temp_ranges = {}

    for station in stations:
        with open(f'temperatures/{station}', 'r') as file:
            reader = csv.reader(file)
            temperatures = [float(row[1]) for row in reader]
            temp_range = max(temperatures) - min(temperatures)
            temp_ranges[station] = temp_range

     # Find the station with the largest temperature range
    max_range_station = max(temp_ranges, key=temp_ranges.get)

    # Save the result to "largest_temp_range_station.txt"
    with open('largest_temp_range_station.txt', 'w') as file:
        file.write(f"Station with largest temperature range: {max_range_station}\n")
        # Function to find the warmest and coolest station
def find_warmest_and_coolest():
    stations = os.listdir('temperatures')
    station_temps = {}

    for station in stations:
        with open(f'temperatures/{station}', 'r') as file:
            reader = csv.reader(file)
            temperatures = [float(row[1]) for row in reader]
            avg_temp = sum(temperatures) / len(temperatures)
            station_temps[station] = avg_temp

    warmest_station = max(station_temps, key=station_temps.get)
    coolest_station = min(station_temps, key=station_temps.get)

    # Save the result to "warmest_and_coolest_station.txt"
    with open('warmest_and_coolest_station.txt', 'w') as file:
        file.write(f"Warmest station: {warmest_station}\n")
        file.write(f"Coolest station: {coolest_station}\n")

# Run the functions
calculate_average_temperature()
find_largest_temp_range()
find_warmest_and_coolest()








