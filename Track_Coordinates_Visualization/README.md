# Track_Coordinates_Visualization

## Description
Python tool for coordinate extraction, transformation, and visualization, designed to handle geospatial and data processing tasks.
It is particularly helpful when you need to simulate a track passing through specific coordinates (waypoints) and analyze the actual track trajectory with respect to the provided waypoints (waypoint_coordinates.csv) or waypoint boundaries (boundary_coordinates.csv).

## Features
- Extracts and processes coordinates from XML using SSR codes.
- Parses waypoint and boundary data from CSV files.
- Visualizes combined data with clear plots.

## Getting Started
1. Prepare the `input/` folder with:
   - `waypoint_coordinates.csv`
   - `waypoint_boundary.csv`
   - `tracking_asterix.xml`
2. Run the script:
   ```bash
   python main.py
   ```

## Outputs
- `track_coordinates.csv`: Extracted coordinates.
- `combined_plot.png`: Visual representation of data.

