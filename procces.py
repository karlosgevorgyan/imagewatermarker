import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    images = get_images()
    for input_path, filename in images.items():
        output_path = 'output-images/' + input_path.split(os.path.sep)[-1]
        watermark = u'\u00A9' + ' '.join([s.capitalize() for s in filename.split('-')])
        watermark_text(input_path, output_path, watermark)


def watermark_text(input_image_path, output_image_path, text):
    photo = Image.open(input_image_path)
    draw = ImageDraw.Draw(photo)
    font = ImageFont.truetype("arial.ttf", 50)

    width, height = photo.size
    text_width, text_height = draw.textsize(text, font)

    x = width - text_width - 5
    y = height - text_height - 5

    pos = (x, y)

    draw.text(pos, text, fill='white', font=font)
    photo.save(output_image_path)


def get_images():
    valid_image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    for r, d, f in os.walk('input-images'):
        images = {}
        for file in f:
            path = os.path.join(r, file)
            filename, extension = os.path.splitext(path)
            if extension in valid_image_extensions:
                images[path] = filename.split(os.path.sep)[-1]
    return images


if __name__ == '__main__':
    main()
