import os
import csv
from src.coordinate_converter import parse_waypoint_coordinates, parse_boundary_coordinates
from src.extract_coordinates_by_ssr import extract_coordinates_by_ssr, save_to_csv
from src.track_coordinates_visualization import plot_coordinates


def get_file_path(base_dir, folder_name, file_name):
    """Construct a file path."""
    return os.path.join(base_dir, folder_name, file_name)


def prepare_directories(base_dir):
    """Set up input and output directories."""
    input_dir = get_file_path(base_dir, "input", "")
    output_dir = get_file_path(base_dir, "output", "")
    os.makedirs(output_dir, exist_ok=True)
    return input_dir, output_dir


def extract_and_save_coordinates(track_file, track_ssr, output_track_file):
    """Extract coordinates and save to CSV."""
    print(f"Extracting coordinates for SSR: {track_ssr} from {track_file}...")
    results = extract_coordinates_by_ssr(track_file, track_ssr)
    if results:
        save_to_csv(track_ssr, results, output_track_file)
        print(f"Coordinates saved to {output_track_file}")
        return True
    print(f"No matching frames found with SSR code '{track_ssr}'")
    return False


def load_track_coordinates(output_track_file):
    """Load track coordinates from a CSV file."""
    try:
        print(f"Loading track coordinates from {output_track_file}...")
        track_coords = {'Latitude': [], 'Longitude': []}
        with open(output_track_file, newline='') as csvfile:
            next(csvfile)  # Skip the SSR code line
            reader = csv.DictReader(csvfile)
            for row in reader:
                track_coords['Latitude'].append(float(row['Latitude']))
                track_coords['Longitude'].append(float(row['Longitude']))
        return track_coords
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading track coordinates: {e}")
        return {'Latitude': [], 'Longitude': []}


def parse_waypoints_and_boundaries(waypoint_file, boundary_file):
    """Parse waypoint and boundary coordinates."""
    print(f"Parsing waypoint data from {waypoint_file} and boundary data from {boundary_file}...")
    waypoint_coords = parse_waypoint_coordinates(waypoint_file)
    boundary_coords = parse_boundary_coordinates(boundary_file)
    return waypoint_coords, boundary_coords


def generate_plot(track_coords, waypoint_coords, boundary_coords, output_dir, plot_file):
    """Generate and save the plot."""
    try:
        print(f"Generating plot and saving to {plot_file}...")
        plot_coordinates(track_coords, waypoint_coords, boundary_coords, output_dir, output_filename=plot_file)
        print(f"Plot successfully saved to {plot_file}")
    except Exception as e:
        print(f"Error generating plot: {e}")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Prepare directories
    input_dir, output_dir = prepare_directories(base_dir)

    # Define file paths
    files = {
        "waypoint": get_file_path(input_dir, "", "waypoint_coordinates.csv"),
        "boundary": get_file_path(input_dir, "", "waypoint_boundary.csv"),
        "track": get_file_path(input_dir, "", "tracking_asterix.xml"),
        "output_track": get_file_path(output_dir, "", "track_coordinates.csv"),
        "plot": get_file_path(output_dir, "", "combined_plot.png"),
    }
    track_ssr = 3055

    # Extract and save coordinates
    if not extract_and_save_coordinates(files["track"], track_ssr, files["output_track"]):
        return

    # Load data
    track_coords = load_track_coordinates(files["output_track"])
    waypoint_coords, boundary_coords = parse_waypoints_and_boundaries(files["waypoint"], files["boundary"])

    # Generate plot
    generate_plot(track_coords, waypoint_coords, boundary_coords, output_dir, files["plot"])


if __name__ == "__main__":
    main()
