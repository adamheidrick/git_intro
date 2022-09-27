from PIL import Image
import time


def main():
    source = 'prng-service.txt'
    destination = 'image-service.txt'
    is_running = True
    while is_running:
        run = int(input("Enter 1 to run program or 2 to quit: "))
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
                    f.close()
                    time.sleep(5)

                with open(destination, 'r') as f:
                    path = f.read()
                    f.close()
                image = Image.open(path)
                image.show()

        elif run == 2:
            is_running = False
            print('End of Program')

        else:
            print('Unknown Command. Please try again.')


if __name__ == "__main__":
    main()
