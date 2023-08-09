"""This RSA Module can be used to Encrypt and Decrypt text using RSA algorithm."""

from random import randrange


# Citation: From GeeksforGeeks
def power(x_x, y_y, p_p):
    """Return (x^y) % p."""
    # Initialize result
    res = 1
    # Update x if it is more than or
    # equal to p
    x_x = x_x % p_p
    while y_y > 0:

        # If y is odd, multiply
        # x with result
        if y_y & 1:
            res = (res * x_x) % p_p

        # y must be even now
        y_y = y_y >> 1  # y = y/2
        x_x = (x_x * x_x) % p_p

    return res


# Citation: From GeeksforGeeks
def miller_test(d_d, n_n, loopcount):
    """Return false if n is composite and returns false if n is probably prime."""
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    # a_a = 2 + randrange(1, n_n - 4)
    a_a = randrange(2, n_n - 2)
    # Compute a^d % n
    x_x = power(a_a, d_d, n_n)

    # if (x == 1 or x == n - 1):
    #     return True
    if x_x in (1, n_n - 1):
        return True

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    i = 0
    while d_d != n_n - 1 and i <= loopcount:
        x_x = (x_x * x_x) % n_n
        d_d *= 2
        i += 1
        if x_x == 1:
            return False
        if x_x == n_n - 1:
            return True

    # Return composite
    return False


class RSA():
    """Class represents the RSA Algorithm."""

    def __init__(self, prime_size=1024, max_iterations=10):
        """Intialize all values."""
        self.rsa = {}
        options = ['message', 'encrypted', 'decrypted', 'p', 'q', 'phi', 'e', 'n', 'd']
        for option in options:
            self.rsa[option] = None

        if max_iterations <= 10:
            self.prime_size = prime_size
            self.max_iterations = max_iterations
        else:
            self.prime_size = None
            self.max_iterations = None
            for option in options:
                self.rsa[option] = None

    def calc_p_and_q(self, size):
        """Need to calculate P and Q as primes that do not equal eachother."""
        if size is None or size < 2:
            for option in self.rsa:
                self.rsa[option] = None
            return

        p_val = self.generate_prime_number(size)
        q_val = self.generate_prime_number(size)
        self.rsa['p'] = p_val
        self.rsa['q'] = q_val

        while p_val == q_val:
            p_val = self.generate_prime_number(size)
            q_val = self.generate_prime_number(size)
            self.rsa['p'] = p_val
            self.rsa['q'] = q_val

    def calc_phi(self):
        """Need to calculate Phi (or totient) which is P-1 * Q-1."""
        self.rsa['phi'] = (self.rsa['p'] - 1) * (self.rsa['q'] - 1)

    def calc_e(self, phi):
        """Need to calculate the encryption exponenet also known as e."""
        temp_e = 2
        self.rsa['e'] = temp_e
        while temp_e < phi:
            tempgcd, _, _ = self.gcd(temp_e, phi)
            if tempgcd == 1:
                self.rsa['e'] = temp_e
                break
            temp_e += 1

    def calc_n(self):
        """Need to calcualte N which is P * Q."""
        self.rsa['n'] = (self.rsa['p']) * (self.rsa['q'])

    # Citation: GeeksforGeeks
    def mod_inv(self, number, modular):
        """Need to calculate decryption exponent by using Modular Inverse."""
        if self.rsa['p'] is None or self.rsa['q'] is None:
            for option in self.rsa:
                self.rsa[option] = None
            return None
        # d * number = 1 mod(modular)
        gcd, temp_x, _ = self.gcd(number, modular)
        if gcd != 1:  # mod_inv doesn't exist
            return None
        temp_d = (temp_x % modular + modular) % modular
        self.rsa['d'] = temp_d
        return temp_d

    def gcd(self, num_one, num_two):
        """Calculate Greatest Commond Divisor."""
        if num_one == 0:
            return num_two, 0, 1
        gcd, x_1, y_1 = self.gcd(num_two % num_one, num_one)
        x_result = y_1 - (num_two // num_one) * x_1
        y_result = x_1
        return gcd, x_result, y_result

    def generate_prime_number(self, size):
        """Generate a random prime number for use by calc_p_and_q."""
        if size is None or size < 2:
            for option in self.rsa:
                self.rsa[option] = None
            return None
        flag = True
        temp_p = randrange(0, size)
        while flag:
            if self.is_prime(temp_p):
                flag = False
                break
            temp_p = randrange(0, size)
        return temp_p

    def is_prime(self, number):
        """Check if number is a prime number."""
        if number <= 1 or number == 4:
            return False
        if number <= 3:
            return True
        # Find r such that n =
        # 2^d * r + 1 for some r >= 1
        odd_num = number - 1
        while odd_num % 2 == 0:
            odd_num //= 2

        # Iterate given number of 'max_iterations' times
        for _ in range(self.max_iterations):
            if miller_test(odd_num, number, self.max_iterations) is False:
                return False

        return True

    def get_data(self):
        """Return all data associated with RSA."""
        return self.rsa

    def get_public_key(self):
        """Return public key in tuple form (e, n)."""
        return (self.rsa['e'], self.rsa['n'])

    def get_private_key(self):
        """Return private key in tuple form (d, n)."""
        return (self.rsa['d'], self.rsa['n'])

    def encrypt(self, plain_text):
        """Return the encryption of the plain_text."""
        self.rsa['message'] = plain_text
        if self.rsa['p'] is None or self.rsa['q'] is None:
            for option in self.rsa:
                self.rsa[option] = None
            return None
        e_key, n_key = self.get_public_key()
        self.rsa['encrypted'] = ''
        for _, element in enumerate(plain_text):
            self.rsa['encrypted'] += (chr((ord(element) ** e_key) % n_key))
        return self.rsa['encrypted']

    def decrypt(self, cipher_text):
        """Return the decrypted cipher_text."""
        if self.rsa['p'] is None or self.rsa['q'] is None:
            for option in self.rsa:
                self.rsa[option] = None
            return None
        self.rsa['decrypted'] = ''
        d_key, n_key = self.get_private_key()
        for _, element in enumerate(cipher_text):
            self.rsa['decrypted'] += (chr((ord(element) ** d_key) % n_key))
        print(self.rsa)
        return self.rsa['decrypted']
