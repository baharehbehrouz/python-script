import sys
from PIL import Image
images=[]
for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)
images[0].save("costume.gif",append_images=[images[1]] ,save_all=True,duration=200,loop=0)

