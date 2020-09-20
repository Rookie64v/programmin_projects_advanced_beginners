from PIL import Image
from typing import *


def average(p: Tuple[int, int, int]) -> int:
    return round(sum(p) / 3)


im = Image.open('ascii-pineapple.jpg')
width, height = im.size
rgb_pixels = list(im.getdata())
rgb_pixels = [rgb_pixels[_ * width: (_ + 1) * width] for _ in range(height)]
print(f'Loaded image, {height} x {width}...')
grey_pixels = [[0 for i in range(width)] for j in range(height)]
print(f'Initialized black gray-scale matrix, size {len(grey_pixels)} x '
      f'{len(grey_pixels[0])}...')
for index, row in enumerate(rgb_pixels):
    grey_pixels[index] = list(map(average, row))
print(f'Image converted to gray-scale...')
