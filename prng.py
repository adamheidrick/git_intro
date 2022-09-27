# reads prng service text, if run, then generates random number and writes it to the .txt
import random
source = 'prng-service.txt'

with open(source, 'r') as f:
    text = f.read()
    f.close()

if text == 'run':
    randy = str(random.randint(1, 100))
    with open(source, 'w') as f:
        f.write(randy)
        f.close()

