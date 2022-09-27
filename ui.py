# UI for user. If run, then writes run to prng service text.
# Reads from reads prng service text.
# Writes random number to image service text
# Reads from image service text
# displays path or image
# run = int(input("Enter 1 to run program: "))

import time
source = 'prng-service.txt'
destination = 'image-service.txt'
is_running = True

while is_running:
    run = int(input("Enter 1 to run program: "))
    if run == 1:
        with open(source, 'w') as f:
            f.write('run')
            f.close()
            time.sleep(5)

        with open(source, 'r') as f:
            value = f.read()

        if value.isnumeric():
            with open(destination, 'w') as f:
                f.write(value)
            print(value)

    if run == 2:
        is_running = False
        print('End of Program')
