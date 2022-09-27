
import time
source = 'image-service.txt'

while True:
    time.sleep(1)
    with open(source, 'r') as f:
        text = f.read()
        if text.isnumeric():
            num = int(text)
            print(num)
            # TODO: Get num of images
            # TODO: Mod num with num of images
            # Write path to image-service.txt
    f.close()
