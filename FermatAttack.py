# Fermat-Attack on weak RSA-Moduls (Prime Number are to close)
import math

# two close Prime Number (just an Example)
MODUL = 19 * 91


def attack(guess, tries):
    r = pow(guess + tries, 2) - MODUL
    if(math.sqrt(r).is_integer() != True):
        tries += 1
        return attack(guess, tries)
    else:
        return (guess + tries), math.sqrt(r)


def main():
    first_guess = round(math.sqrt(MODUL), 0)
    b, r = attack(first_guess, 0)
    prime1 = b - r
    prime2 = b + r
    print("The Primes are {:d} and {:d}.".format(int(prime1), int(prime2)))
    print(prime1 * prime2)


if __name__ == "__main__":
    main()
