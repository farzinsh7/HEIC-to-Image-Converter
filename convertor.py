from PIL import Image
import pillow_heif

# Register HEIF format support
pillow_heif.register_heif_opener()

# Open the HEIC file
image = Image.open("sample.HEIC")

# Save as JPG
image.save("output/output.jpg", "JPEG")
