# AVIF to [JPG, JPEG, PNG] Converter

This Python program converts AVIF images to JPEG, JPG, or PNG format. It utilizes the `av` library for decoding AVIF images and the `Pillow` library for image processing.

## Features

- Convert AVIF images to JPEG, JPG, or PNG.
- Simple command-line interface for input and output specifications.

## Requirements

- Python 3.x
- `av` library
- `Pillow` library

## Installation

First, ensure you have Python installed. Then, install the required libraries:

```bash
pip install av pillow
```

## Usage

1. Clone this repository or download the script.
2. Run the script and follow the prompts.

```bash
python convert_avif_to_jpg.py
```

3. Enter the folder path containing AVIF images.
4. Choose the desired output image extension (jpeg, jpg, or png).

## Example

```bash
>> Please enter the folder path containing AVIF images: /path/to/avif/images

AVAILABLE EXTENSIONS: [jpeg, jpg, png]

>> What is the image extension you want: jpg
```

The script will convert all AVIF images in the specified folder to the chosen format and save them in the same folder.


## Contributing

Feel free to fork this repository and make improvements. Pull requests are welcome!
