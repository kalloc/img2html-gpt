import cv2
import base64


def img_to_base64_html(img_path, output_html='output_base64.html', img_format="JPEG"):
    img = cv2.imread(img_path)
    _, buffer = cv2.imencode(f'.{img_format.lower()}', img)
    img_str = base64.b64encode(buffer.tobytes()).decode()

    html_img = f'<img src="data:image/{img_format.lower()};base64,{img_str}"/>'
    with open(output_html, 'w') as file:
        file.write(html_img)

def img_to_pixel_html(img_path, output_html='output_pixel.html', pixel_size=2):
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    pixel_size = min(pixel_size, height, width)
    img_small = cv2.resize(img, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_AREA)
    img_large = cv2.resize(img_small, (width, height), interpolation=cv2.INTER_NEAREST)

    html_code = '<html><head></head><body><style>div.pixel { width: %dpx; height: %dpx; float: left; }</style>\n' % (pixel_size, pixel_size)
    for y in range(0, img_large.shape[0], pixel_size):
        for x in range(0, img_large.shape[1], pixel_size):
            b, g, r = img_large[y, x]
            html_code += '<div class="pixel" style="background-color: rgb(%d,%d,%d);"></div>' % (r, g, b)
        html_code += '<div style="clear: both;"></div>\n'
    html_code += '\n</body></html>'

    with open(output_html, 'w') as file:
        file.write(html_code)

