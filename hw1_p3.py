##Write a program that reads an image and prints its pixel values.

## In class code
from PIL import Image

#function giving names to color pixels
def convert(pixel):
    if pixel == "(0, 0, 0)": return "B"
    elif pixel == "(255, 242, 0)": return "Y"
    else: return pixel

#Opens the image and creates a output file to write to
image = Image.open("smiley.png").convert("RGBA")
output_text_file = open("awesome_picture.txt", "w")

#Iterate through the pixels and writes the color using our function to the file
for y in range(image.height):
    for x in range(image.width):
        r, g, b, _ = image.getpixel((x, y))
        pixel = (f"({r}, {g}, {b})")
        pixel = convert(pixel)
        output_text_file.write(pixel)
        output_text_file.write(" ")
    output_text_file.write("\n")

#close file
output_text_file.close()