from PIL import Image
from pathlib import Path

from Steganography import Steganography

#picCTF{Flag} is hidden in the image using LSB of steagongraphy

file = Path(__file__).resolve()
dir = file.parent

image_path = dir / 'red.png'

steg = Steganography()
steg.set_image(image_path)
steg.set_rgba()
steg.red_only_single_lsb()
steg.get_ascii()
steg.output_printable()
#
#steg.red_only_single_lsb()
#print(steg.get_bytes())
#print(steg.get_dec())
#print(steg.get_ascii())

