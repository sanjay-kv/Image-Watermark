import os
from PIL import Image, ImageEnhance

def watermark_photo(input_image_path, watermark_image_path, output_image_path, position, scale, opacity):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")

    # Scale the watermark
    base_width, base_height = base_image.size
    watermark_width = int(base_width * scale)
    watermark_height = int(watermark.size[1] * (watermark_width / watermark.size[0]))
    watermark = watermark.resize((watermark_width, watermark_height))

    # Adjust opacity
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)

    # Determine position
    positions = {
        "top-left": (20, 20),
        "top-right": (base_width - watermark_width - 20, 20),
        "bottom-left": (20, base_height - watermark_height - 20),
        "bottom-right": (base_width - watermark_width - 20, base_height - watermark_height - 20),
        "center": ((base_width - watermark_width) // 2, (base_height - watermark_height) // 2),
    }
    position_coords = positions.get(position, "bottom-right")

    # Create a transparent layer
    transparent = Image.new(mode="RGBA", size=(base_width, base_height), color=(0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position_coords, watermark)

    # Save the final image
    output_format = "PNG" if output_image_path.endswith(".png") else "JPEG"
    transparent = transparent.convert("RGB") if base_image.mode == "RGB" else transparent.convert("P")
    transparent.save(output_image_path, format=output_format, optimize=True, quality=100)
    print(f"Saved: {output_image_path}")


# Main Script
folder = input("Enter Folder Path: ").strip()
watermark = input("Enter Watermark Path: ").strip()
position = input("Enter Position (top-left, top-right, bottom-left, bottom-right, center): ").strip()
scale = float(input("Enter Watermark Scale (0.01 to 0.5, e.g., 0.08 for 8%): "))
opacity = float(input("Enter Watermark Opacity (0.1 to 1.0): "))

os.chdir(folder)
files = os.listdir(os.getcwd())

if not os.path.isdir("output"):
    os.mkdir("output")

total_files = len(files)
processed_files = 0

for f in files:
    if os.path.isfile(f):
        if f.lower().endswith((".png", ".jpg", ".jpeg")):
            output_path = os.path.join("output", f)
            watermark_photo(f, watermark, output_path, position, scale, opacity)
            processed_files += 1
            print(f"Progress: {processed_files}/{total_files} files processed.")

print("Watermarking complete. Check the 'output' folder.")
