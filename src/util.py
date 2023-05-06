import sys
import os
from PIL import Image
import numpy as np


def parse_arg():
	if len(sys.argv) < 3:
		print("Usage: python main.py <model number> <filepath>")
		sys.exit(1)
	if not sys.argv[1].isdigit() and int(sys.argv[1]) not in [1, 2]:
		print("Invalid model number")
		sys.exit(1)
	if not os.path.isfile(sys.argv[2]):
		print("File does not exists")
		sys.exit(1)
	return sys.argv[1], sys.argv[2]

def get_image(filename):
	return np.array(Image.open(filename))