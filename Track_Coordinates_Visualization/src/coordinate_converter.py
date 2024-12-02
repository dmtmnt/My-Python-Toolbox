# coordinate_converter.py
import pandas as pd

# Convert DMS (Degrees, Minutes, Seconds) format to Decimal Degrees
def dms_to_decimal(degrees, minutes, direction):
    decimal = degrees + minutes / 60.0
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# Parse the single DMS coordinate from waypoint_coordinates.csv
def parse_waypoint_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        dms_coord = lines[1].strip()  # Second line has the DMS coordinate

        # Parse latitude and longitude strings
        lat_str, lon_str = dms_coord.split()
        
        # Parse latitude
        lat_deg = int(lat_str[:2])
        lat_min = int(lat_str[2:4])
        lat_dir = lat_str[-1]
        latitude = dms_to_decimal(lat_deg, lat_min, lat_dir)
        
        # Parse longitude
        lon_deg = int(lon_str[:3])
        lon_min = int(lon_str[3:5])
        lon_dir = lon_str[-1]
        longitude = dms_to_decimal(lon_deg, lon_min, lon_dir)
        
        return [(latitude, longitude)]  # Return as a list of one tuple

# Parse multiple DMS coordinates from boundary_coodrinates.csv
def parse_boundary_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line (HOLD_IMPED label)

        coordinates = []
        for dms_coord in lines:
            dms_coord = dms_coord.strip()
            lat_str, lon_str = dms_coord.split()
            
            # Parse latitude
            lat_deg = int(lat_str[:2])
            lat_min = int(lat_str[2:4])
            lat_dir = lat_str[-1]
            latitude = dms_to_decimal(lat_deg, lat_min, lat_dir)
            
            # Parse longitude
            lon_deg = int(lon_str[:3])
            lon_min = int(lon_str[3:5])
            lon_dir = lon_str[-1]
            longitude = dms_to_decimal(lon_deg, lon_min, lon_dir)
            
            coordinates.append((latitude, longitude))
        
        return coordinates
