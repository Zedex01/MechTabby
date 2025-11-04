from PIL import Image
from pathlib import Path

from Steganography import Steganography

#picCTF{Flag} is hidden in the image using LSB of steagongraphy

file = Path(__file__).resolve()
dir = file.parent

image_path = dir / 'red.png'

#Create object and set target image
steg = Steganography(image_path)

#Extract all the RGBA data from the image
steg.set_rgba()

#Extract the lsb for all 4 channels
steg.rgba()

#Print out the ascii results
ascii = steg.get_ascii()
print("".join(ascii))


