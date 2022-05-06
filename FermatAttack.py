# Fermat-Attack on weak RSA-Moduls
import math

# two close Prime Number (just an Example)
MODUL = 18487289 * 18543067


# Method that finds the distance between the mid and primes
def attack(guess, max_tries=1000000):
  for tries in range(max_tries):
    b = pow(guess + tries, 2) - MODUL
    if b >= 0 and pow(math.isqrt(b), 2) == b:
      return guess + tries, math.isqrt(b), tries + 1
  return 0, 0, max_tries


def main():
  first_try = math.isqrt(MODUL)
  a, b, tries = attack(first_try)
  prime1 = a - b
  prime2 = a + b
  if a != 0:
    print(
        f"It took {tries} Tries to find the Primes {prime1} and {prime2}.")
  else:
    print(f"Nothing found in {tries} Tries.")


if __name__ == "__main__":
    main()
