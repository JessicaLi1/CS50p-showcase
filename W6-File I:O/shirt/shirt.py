import sys
import os
from PIL import Image, ImageOps


# Check that the correct number of command-line arguments were provided
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

#create input and output variables
infile = sys.argv[1]
outfile = sys.argv[2]

#check if input exits
if not os.path.exists(infile):
    sys.exit("Input does not exit")

#check if the extensions of inputs and outputs meet rquirements
input_ext = os.path.splitext(infile)[1].lower()
output_ext = os.path.splitext(outfile)[1].lower()

if not input_ext in (".jpg",'.jpeg', '.png'):
    sys.exit("Invalid input")
elif not output_ext in ('.jpg', '.jpeg', '.png'):
    sys.exit("Invalid output")

if input_ext!=output_ext:
    sys.exit("Input and output have different extensions")

#open images
shirt=Image.open("shirt.png")
portrait=Image.open(infile)
#resize and crop the input
s_size=shirt.size
portrait=ImageOps.fit(portrait,s_size)

#overlay shirt image onto input
portrait.paste(shirt,shirt)

#save the output image
portrait.save(outfile)