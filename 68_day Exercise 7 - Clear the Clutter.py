# my solution
import os 

images = ['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg']

for image in images:
    n = len(images) - 1
    os.rename(image, f'{n}.jpg')
    images.pop(0)













# s = '1.jpg'
# d= "a.webp"

# os.rename(s, d)