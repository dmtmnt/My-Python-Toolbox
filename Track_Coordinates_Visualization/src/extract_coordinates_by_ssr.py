import argparse
import xml.etree.ElementTree as ET
import csv

def extract_coordinates_by_ssr(input_file, ssr_code):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    results = []

    # Loop through each frame element
    for frame in root.findall('frame'):
        found_ssr_code = False
        lat, lon = None, None
        
        # Loop through each Frame_Block_Record
        for block in frame.findall('Frame_Block_Record'):
            # Check if I062_060 item with the desired SSR code is present
            for item in block.findall('item'):
                if item.get('number') == 'I062_060':
                    # Check the no_change element within I062_060
                    no_change_elem = item.find('no_change')
                    if no_change_elem is not None and no_change_elem.text == str(ssr_code):
                        found_ssr_code = True
                        break
            
            # If SSR code is found, search for latitude and longitude in I062_105
            if found_ssr_code:
                for item in block.findall('item'):
                    if item.get('number') == 'I062_105':
                        lat = item.find('Latitude').text if item.find('Latitude') is not None else None
                        lon = item.find('Longitude').text if item.find('Longitude') is not None else None
                        break

            # If both SSR code and coordinates are found, store the result
            if found_ssr_code and lat and lon:
                results.append({
                    'Latitude': lat,
                    'Longitude': lon
                })
                break  # Stop searching within this frame if data is collected

    return results

# Function to save results to CSV with SSR code at the beginning
def save_to_csv(ssr_code, results, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write SSR code at the beginning of the file
        writer.writerow([f"SSR Code: {ssr_code}"])
        
        # Write headers for the coordinates
        writer.writerow(['Latitude', 'Longitude'])
        
        # Write the extracted coordinates
        for result in results:
            writer.writerow([result['Latitude'], result['Longitude']])
