import re
from PIL import Image, ImageDraw, ImageFont # https://pillow.readthedocs.io/en/stable/reference/index.html
from daltonlens import simulate # https://github.com/DaltonLens/DaltonLens-Python
import numpy as np

# This script reads a list of colours and creates an image with them rendered as-is and after processing by simulations of three forms of colour blindness.

WORK_DIR = 'C:/Temp/'
INPUT_PATH = WORK_DIR + 'color-list.txt'

SQUARE_SIDE_LENGTH = 64
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
INTER_COLUMN_GAP = 16
TEXT_WIDTH = 256 + INTER_COLUMN_GAP
TOP_MARGIN = 32

FONT_NAME = "GOTHICB.TTF"
FONT_SIZE = 16
FONT = ImageFont.truetype(FONT_NAME, FONT_SIZE)

FONT2_SIZE = 10
FONT2 = ImageFont.truetype(FONT_NAME, FONT2_SIZE)

SIMULATIONS = [
    simulate.Deficiency.DEUTAN,
    simulate.Deficiency.PROTAN,
    simulate.Deficiency.TRITAN,
]

CATEGORY_NAMES = [
    "Normal",
    "Deuteranopia",
    "Protanopia",
    "Tritanopia"
]

PATTERN_STRING = r"(\S*)\s(#[a-fA-F0-9]{6})"
pattern = re.compile(PATTERN_STRING)

with open(INPUT_PATH, encoding="utf-8") as f:
    lines = f.readlines()

color_names = []
color_codes = []
for line in lines:
    match = pattern.match(line)

    if match == None:
        continue

    #print(f'G1={match.group(1)}|G2={match.group(2)}')

    color_names.append(match.group(1))
    color_codes.append(match.group(2))

del lines

COLOR_COUNT = len(color_codes)

HEIGHT = TOP_MARGIN + SQUARE_SIDE_LENGTH * COLOR_COUNT

image_normal = Image.new('RGB', (SQUARE_SIDE_LENGTH, HEIGHT), color = COLOR_WHITE)
draw_normal = ImageDraw.Draw(image_normal)

image_text = Image.new('RGB', (TEXT_WIDTH, HEIGHT), color=COLOR_WHITE)
draw_text = ImageDraw.Draw(image_text)

for i in range(COLOR_COUNT):
    y0 = TOP_MARGIN + i*SQUARE_SIDE_LENGTH
    y1 = y0 + SQUARE_SIDE_LENGTH
    
    # Normal vision colour square
    draw_normal.rectangle([0, y0, SQUARE_SIDE_LENGTH, y1], fill=color_codes[i])
    
    # Colour name
    draw_text.text((TEXT_WIDTH - INTER_COLUMN_GAP, y0 + SQUARE_SIDE_LENGTH/2), str(color_names[i]), font=FONT, anchor="rm", fill=COLOR_BLACK)

# Regarding simulator choice, see https://daltonlens.org/opensource-cvd-simulation/#So-which-one-should-we-use?
simulator = simulate.Simulator_Brettel1997()

array_normal = np.asarray(image_normal)

images = [
    image_normal,
]

for simulation in SIMULATIONS:
    array_simulated = simulator.simulate_cvd(array_normal, simulation, severity=1.0)
    images.append(Image.fromarray(array_simulated))

COMPOSITE_WIDTH = TEXT_WIDTH + len(images) * SQUARE_SIDE_LENGTH + (len(images) - 1) * INTER_COLUMN_GAP

image_composite = Image.new('RGB', (COMPOSITE_WIDTH, HEIGHT), color = COLOR_WHITE)

for i in range(len(images)):
    x = TEXT_WIDTH + i * (SQUARE_SIDE_LENGTH + INTER_COLUMN_GAP)
    image_composite.paste(images[i], (x, 0))

image_composite.paste(image_text, (0, 0))

draw_composite = ImageDraw.Draw(image_composite)
for i in range(len(CATEGORY_NAMES)):
    x = TEXT_WIDTH + i*(SQUARE_SIDE_LENGTH + INTER_COLUMN_GAP) + SQUARE_SIDE_LENGTH/2
    y = TOP_MARGIN/2
    draw_composite.text((x, y), CATEGORY_NAMES[i], font=FONT2, anchor="mm", fill=COLOR_BLACK)

image_composite.save(WORK_DIR + 'out_composite.png', "PNG")
