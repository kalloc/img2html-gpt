# Image to HTML Converter

This tool allows you to convert images into HTML format. It supports two modes: converting images to a base64 encoded HTML or creating a pixelated HTML version of the image.

## Requirements

- Python 3.8 or newer
- Poetry for dependency management and running the project

## Installation

### Install Poetry

First, you need to install Poetry, a dependency manager for Python. Run the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

After installing Poetry, you might need to restart your terminal or run the command provided by the installer to add Poetry to your PATH.

## Setup the Project

Clone the repository to your local machine and navigate into the project directory:

```bash
git clone https://github.com/kalloc/img2html-gpt
cd img2html-gpt
```

Install the project dependencies using Poetry:

```bash
poetry install
```

## Usage
After installing the project dependencies, you can run the script using Poetry. Here are some examples of how to use the script:

Convert an image to base64 encoded HTML:
```bash
poetry run img2html -mode base64 -output output.html -format JPEG image.jpg
```

Convert an image to a pixelated HTML version:
```bash
poetry run python script.py -mode pixel -output pixel_output.html -size 10 image.jpg
```


## Help
For more information on the available commands and options, run the script with the -help option:

```bash
poetry run python script.py -help
```

