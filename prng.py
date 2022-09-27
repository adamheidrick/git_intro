# reads prng service text, if run, then generates random number and writes it to the .txt
import random
import time
source = 'prng-service.txt'


def main():
    while True:
        time.sleep(1)
        with open(source, 'r') as f:
            text = f.read()
            print(f'Reading .txt = {text}')

        if text == 'run':
            with open(source, 'w') as f:
                randy = str(random.randint(1, 100))
                print(f'Writing Random {randy} Number to .txt')
                f.write(randy)
        f.close()


if __name__ == "__main__":
    main()
