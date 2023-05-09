from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
if len(sys.argv)==1:
    font=random.choice(figlet.getFonts())
elif len(sys.argv)==3:
    if sys.argv[1] in ('-f','--font'):
        font=sys.argv[2]
        if font not in figlet.getFonts():
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

text = input("Input: ")
fig=Figlet(font=font)
print(f"Output:\n{fig.renderText(text)}")
