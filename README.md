# Image Watermarking

This repository contains a Python script for adding watermarks to images. The script allows you to place a watermark on multiple images in a specified folder with customizable position, scale, and opacity.

## Features

- Add watermark to images in bulk
- Customize watermark position (top-left, top-right, bottom-left, bottom-right, center)
- Adjust the scale and opacity of the watermark
- Supports PNG, JPG, and JPEG image formats

## Requirements

- Python 3.x
- `PIL` (Pillow) library

You can install the required library using pip:
```sh```

pip install pillow
# Usage
Clone the repository:
sh

git clone https://github.com/Ankitaghavate/Image-Watermark.git

cd Image-Watermark

# Run the script:

python Image-Watermark.py

Follow the prompts to enter the folder path containing images, the watermark image path, position, scale, and opacity.
# Example

sh
Enter Folder Path: /path/to/your/images

Enter Watermark Path: /path/to/your/watermark.png

Enter Position (top-left, top-right, bottom-left, bottom-right, center): bottom-right

Enter Watermark Scale (0.01 to 0.5, e.g., 0.08 for 8%): 0.1

Enter Watermark Opacity (0.1 to 1.0): 0.5

The script will process the images and save the watermarked versions in an output folder within the specified directory.

# Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.
