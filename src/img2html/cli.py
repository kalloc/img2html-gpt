#!/usr/bin/env python
import sys

from . import img_to_base64_html, img_to_pixel_html

def print_help():
    help_text = """
    Usage: python script.py -mode [mode] [options] <path_to_image>
    
    Modes:
      base64         Generate base64 encoded image HTML (default).
      pixel          Generate pixelated image HTML.
      
    Options:
      -output [file] Specify output HTML file name.
      -format [fmt]  Specify image format for base64 encoding (default JPEG).
      -size [size]   Specify pixel size for pixelated image (default 2).
      
    Example:
      python script.py -mode pixel -output pixel_art.html -size 5 myimage.jpg
      python script.py -mode base64 -output encoded.html -format PNG myimage.png
    """
    print(help_text)

def main():
    if '-help' in sys.argv or len(sys.argv) < 3:
        print_help()
        return

    mode = 'base64'  # Default mode
    img_path = ''
    output_html = 'output.html'
    img_format = "JPEG"
    pixel_size = 2 
    
    i = 1  # Skip the script name
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '-mode' and i + 1 < len(sys.argv):
            mode = sys.argv[i + 1]
            i += 2
        elif arg == '-output' and i + 1 < len(sys.argv):
            output_html = sys.argv[i + 1]
            i += 2
        elif arg == '-format' and i + 1 < len(sys.argv):
            img_format = sys.argv[i + 1]
            i += 2
        elif arg == '-size' and i + 1 < len(sys.argv):
            pixel_size = int(sys.argv[i + 1])
            i += 2
        else:
            img_path = arg
            i += 1

    if not img_path:
        print("Image path not specified. Use -help for usage information.")
        return
    
    if mode == 'base64':
        img_to_base64_html(img_path, output_html, img_format)
    elif mode == 'pixel':
        img_to_pixel_html(img_path, output_html, pixel_size)
    else:
        print(f"Unknown mode: {mode}. Use -help for usage information.")

if __name__ == "__main__":
    main()
