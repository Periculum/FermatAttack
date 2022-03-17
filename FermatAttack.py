# Fermat-Attack on weak RSA-Moduls
import math

# two close Prime Number (just an Example)
MODUL = 18487289 * 18543067


# recursive Method that finds the distance between the mid and primes
def attack(guess, tries):
    r = pow(guess + tries, 2) - MODUL
    if not math.sqrt(r).is_integer():
        tries += 1
        return attack(guess, tries)
    else:
        return (guess + tries), math.sqrt(r), tries + 1


def main():
    first_guess = round(math.sqrt(MODUL), 0)
    b, r, tries = attack(first_guess, 0)
    prime1 = b - r
    prime2 = b + r
    print("It took {:d} Tries to find the Primes {:d} and {:d}.".format(
        tries, int(prime1), int(prime2)))
    # print(prime1 * prime2)


if __name__ == "__main__":
    main()
