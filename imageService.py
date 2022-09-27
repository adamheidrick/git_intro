import time
import os
source = 'image-service.txt'
num_images = len(os.listdir(path='images'))
image_list = os.listdir(path='images')
cwd = os.getcwd()
images = os.listdir(path='images')

while True:
    time.sleep(1)
    with open(source, 'r') as f:
        text = f.read()

    if text.isnumeric():
        num = int(text) % num_images
        path = cwd + "\\images\\" + image_list[num]
        with open(source, 'w') as f:
            f.write(path)
    f.close()
