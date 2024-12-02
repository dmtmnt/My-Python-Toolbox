import os
import matplotlib.pyplot as plt
import csv


# Plot the coordinates from all files
def plot_coordinates(track_coords, waypoint_coords, boundary_coords, output_dir, output_filename="combined_plot.png"):
    plt.figure(figsize=(10, 6))
    
    # Plot track coordinates in green
    track_lons = [float(lon) for lon in track_coords['Longitude']]
    track_lats = [float(lat) for lat in track_coords['Latitude']]
    plt.plot(track_lons, track_lats, c='green', marker='s', alpha=0.5, label='Track Coordinates')
    
    # Add arrow markers along the track path to indicate direction
    for i in range(len(track_lons) - 1):
        plt.arrow(track_lons[i], track_lats[i], 
                  track_lons[i + 1] - track_lons[i], 
                  track_lats[i + 1] - track_lats[i], 
                  shape='full', lw=0, length_includes_head=True, head_width=0.0002, color='green')
    
    # Plot waypoint coordinates in red
    waypoint_lons = [lon for _, lon in waypoint_coords]
    waypoint_lats = [lat for lat, _ in waypoint_coords]
    plt.scatter(waypoint_lons, waypoint_lats, c='red', marker='o', label='IMPED Waypoint')
    
    # Plot boundary coordinates in blue
    boundary_lons = [lon for _, lon in boundary_coords]
    boundary_lats = [lat for lat, _ in boundary_coords]
    plt.scatter(boundary_lons, boundary_lats, c='blue', marker='^', label='HOLD_IMPED Air Boundary')
    
    # Customize plot
    plt.title("Plot Track, Waypoint and Air Boundary Coordinates")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.legend()
    
    # Save the plot as an image file
    plt.savefig(os.path.join(output_dir, output_filename))
    plt.show()
