import os
from PIL import Image
import pillow_heif

# Register HEIF support
pillow_heif.register_heif_opener()

input_folder = r"c:\dir"  # Use raw string for Windows paths
# input_folder = "/home/username/dir"  # Use raw string for Linux paths
# input_folder = "/Users/username/dir"  # Use raw string for macOS paths
output_folder = "output"

# Create the main output folder (if it doesn't exist)
try:
    os.makedirs(output_folder, exist_ok=True)
except Exception as e:
    print(f"Error creating main output folder: {e}")
    exit(1)

converted_count = 0
max_conversions = 2000

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(".heic"):
            if converted_count >= max_conversions:
                break

            heic_path = os.path.join(root, file)
            base_name = os.path.splitext(file)[0]

            # Calculate relative path from input_folder to current file's directory
            relative_path = os.path.relpath(root, input_folder)

            # Build full path to output subfolder, preserving directory structure
            output_subfolder = os.path.join(output_folder, relative_path)

            # Create the output subfolder (if it doesn't exist)
            try:
                os.makedirs(output_subfolder, exist_ok=True)
            except Exception as e:
                print(f"Error creating subfolder for {heic_path}: {e}")
                continue

            # Construct full path for the output JPEG file
            jpg_path = os.path.join(output_subfolder, base_name + ".jpg")

            # Attempt to open and convert the HEIC file
            try:
                image = Image.open(heic_path)
                image.save(jpg_path, "JPEG")
                print(f"Converted: {heic_path} → {jpg_path}")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {heic_path}: {e}")
    
    # Exit the loop early if max conversions have been reached
    if converted_count >= max_conversions:
        break
