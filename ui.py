# UI for user. If run, then writes run to prng service text.
# Reads from reads prng service text.
# Writes random number to image service text
# Reads from image service text
# displays path or image
# run = int(input("Enter 1 to run program: "))
#
# if run == 1:
#     pass

with open('prng-service.txt', 'w') as f:
    f.write('run')
    f.close()
