# RSA - Cryptography

You will be writing your own RSA algorithm. This means you will need to calculate 2 unique prime numbers, etc.

## Getting Started Steps

- running "make setup" will install correct dependencies and check for correct python version (3.7+)
- running "make clean" will clean the project by removing all "pycache" folders and files
- running "make format will run autopep8 and docformatter to auto format the code
- running "make style" will run a lint checker on your code
- running "make test" or "make" will run all unit tests that have been created
- running "make coverage" will run all unit tests and give you a code coverage report

# RSA

## Requirements

- You must implement a class that handles the below interfaces for calculating RSA.
- The class name must be called "RSA".
- You must implement at least 14 unit tests.
- Must get a 10/10 when running "make style"
- Your unit tests must reach 100% code coverage

## Interface

- The initialization of the class must be RSA(self, prime_size=1024, max_iterations=10)
    - Within initialize create a dictionary rsa that contains {'message': None, 'encrypted': None, 'decrypted': None, 'p': None, 'q': None, 'phi': None, 'e': None, 'n': None, 'd': None}
    - In any of the loops required, the max number of iterations is max_iterations. If your loop count is >= max_iterations then you must invalidate all values in the rsa variable
- The function calc_p_and_q(self, size) needs to calculate P and Q as primes that do not equal eachother (stored in self.rsa['p']/self.rsa['q'])
- The function calc_phi(self) needs to calculate Phi (or totient) which is P-1 * Q-1 (stored in self.rsa['phi'])
- The function calc_e(self, phi) needs to calculate the encryption exponenet also known as e (stored in self.rsa['e'])
- The function calc_n(self) needs to calcualte N which is P * Q (stored in self.rsa['n'])
- The function mod_inv(self, number, modular) needs to calculate decryption exponent by using Modular Inverse and returns the decryption exponent
- The function gcd(self, num_one, num_two) calculate Greatest Commond Divisor
- The function generate_prime_number(self, size) Generate a random prime number for use by calc_p_and_q
- The function is_prime(self, number) check if number is a prime number
- The function get_data(self) return the dictionary self.rsa
- The function get_public_key(self) return public key in tuple form (e, n)
- The function get_private_key(self) return private key in tuple form (d, n)
- The function encrypt(self, plain_text) return the encryption of the plain_text
- The function decrypt(self, cipher_text) return the decrypted cipher_text

## Tests

- Check if the alphabet can be encrypted and decrypted
- Check if digits can be encrypted and decrypted
- Check if special characters can be encrypted and decrypted

## Corner Cases

- If prime_size is None or less than 2 mark all values as None
- If P or Q is None, encryption and decryption should return None
- If P or Q is None, mod_inv should return None
- If the modular inverse does not exist, it should return None
- If P or Q is None, all other values within self.rsa should be marked as None
- Must pass time limits (tbd)

## Library

You can only use basic python libraries and you can use "from random import randrange".
