# Fermat-Attack on weak RSA-Moduls
import math

# two close Prime Number (just an Example)
MODUL = 18487289 * 18543067


# recursive Method that finds the distance between the mid and primes
def attack(guess, tries):
    b = pow(guess + tries, 2) - MODUL
    if b < 0 or not math.sqrt(b).is_integer():
        tries += 1
        return attack(guess, tries)
    else:
        return (guess + tries), math.sqrt(b), tries + 1


def main():
    first_guess = round(math.sqrt(MODUL), 0)
    a, b, tries = attack(first_guess, 0)
    prime1 = a - b
    prime2 = a + b
    print("It took {:d} Tries to find the Primes {:d} and {:d}.".format(
        tries, int(prime1), int(prime2)))


if __name__ == "__main__":
    main()
