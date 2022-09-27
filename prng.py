# reads prng service text, if run, then generates random number and writes it to the .txt
import random
import time
source = 'prng-service.txt'

while True:
    time.sleep(1)
    with open(source, 'r') as f:
        text = f.read()

    if text == 'run':
        with open(source, 'w') as f:
            randy = str(random.randint(1, 100))
            f.write(randy)
    f.close()
