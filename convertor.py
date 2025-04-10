import os
from PIL import Image
import pillow_heif

# Register HEIF support
pillow_heif.register_heif_opener()

input_folder = r"c:\dir"  # Use raw string for Windows paths
# input_folder = "/home/username/dir"  # Use raw string for Linux paths
# input_folder = "/Users/username/dir"  # Use raw string for macOS paths
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

converted_count = 0
max_conversions = 2000

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(".heic"):
            if converted_count >= max_conversions:
                break

            heic_path = os.path.join(root, file)
            base_name = os.path.splitext(file)[0]
            jpg_path = os.path.join(output_folder, base_name + ".jpg")

            try:
                image = Image.open(heic_path)
                image.save(jpg_path, "JPEG")
                print(f"Converted: {heic_path} → {jpg_path}")
                converted_count += 1
            except Exception as e:
                print(f"Failed to convert {heic_path}: {e}")
    if converted_count >= max_conversions:
        break
