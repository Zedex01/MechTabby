from PIL import Image
import pytesseract

print("Getting image")
img = Image.open(r'C:\Users\mmoran\Projects\Git-Repos\MechTabby\CTFs\FlagInFlame\cropped.png')

print("Extracting Text")
text = pytesseract.image_to_string(img)

print("Outputing")
print(text)