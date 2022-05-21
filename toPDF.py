from PIL import Image
import sys
im = Image.open(r""+sys.argv[1]+"/"+sys.argv[2])
img = im.convert("RGB")
imName = sys.argv[2].split(".")[0]
img.save(r""+sys.argv[1]+"/"+imName+".pdf")
print("Done.")
