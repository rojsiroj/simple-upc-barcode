from PIL import Image
import barcode
from barcode.writer import ImageWriter

# Define content of the barcode as string
notOkay = True
while notOkay:
    number = input(
        "Enter the code to generate barcode (number only 11 digits): ")
    if len(number) >= 11:
        notOkay = False

# barcode format
barcode_format = barcode.get_barcode_class('upc')

# Generate barcode and generate as Image
image_barcode = barcode_format(number, writer=ImageWriter())

# Save barcode as PNG
generated_name = "barcode_%s" % number
image_barcode.save(generated_name)


# Open image generated
Image.open("%s.png" % generated_name)
