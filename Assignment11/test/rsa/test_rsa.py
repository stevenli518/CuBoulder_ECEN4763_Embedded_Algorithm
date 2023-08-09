"""test rsa implementation."""

import unittest
from random import randrange
from cryptography.rsa import rsa
# pylint: disable = W0201


class RSATest(unittest.TestCase):
    """Class TowerTest."""

    def setUp(self):
        """setUp."""
        self.rsa = rsa.RSA()

    def test_rsa_prime(self):
        """1.Is prime test."""
        prime_num = self.rsa.generate_prime_number(1024)
        self.assertEqual(self.rsa.is_prime(prime_num), True)
        self.rsa.generate_prime_number(None)
        self.rsa.is_prime(4)
        self.rsa.is_prime(3)

    def test_rsa_calculate_p_and_q(self):
        """2.Calculate_p_and_q."""
        self.rsa.calc_p_and_q(1024)
        self.assertEqual(self.rsa.is_prime(self.rsa.rsa['p']), True)

    def test_miller(self):
        """3. Test miller."""
        for _ in range(10):
            self.rsa.calc_p_and_q(10)
            rsa.miller_test(randrange(1024), randrange(2, 1024), 10)

    def test_rsa_calculate_p_and_q_corner_case(self):
        """4.Calculate_p_and_q."""
        self.rsa.calc_p_and_q(None)

    def test_gcd(self):
        """5. Test GCD."""
        gcd, _, _ = self.rsa.gcd(10, 35)
        self.assertEqual(gcd, 5)

    def test_mod_inverse(self):
        """6. Test mod_inverse."""
        temp_d = self.rsa.mod_inv(21, 352)
        print(temp_d)

    def test_encry(self):
        """7. Test encryption."""
        plaintext = 'TEST'
        self.rsa.calc_p_and_q(self.rsa.prime_size)    
        self.rsa.calc_n()
        self.rsa.calc_phi()
        self.rsa.calc_e(self.rsa.rsa['phi'])
        self.rsa.mod_inv(self.rsa.rsa['e'], self.rsa.rsa['phi'])  
        encryption_text = self.rsa.encrypt(plaintext)
        decryption_test = self.rsa.decrypt(encryption_text)
        _ = self.rsa.get_data()
        self.assertEqual(plaintext, decryption_test)

    def test_gcd_corner(self):
        """8. Test gcd corner case."""
        self.rsa.rsa['p'] = 12
        self.rsa.rsa['q'] = 12
        self.rsa.mod_inv(15, 3)

    def test_decrypt_corner(self):
        """9. Test decrypt corner case."""
        self.rsa.decrypt(12)

    def test_encry_digit(self):
        """10. Test encryption digit."""
        plaintext = '1234'
        self.rsa.calc_p_and_q(self.rsa.prime_size)    
        self.rsa.calc_n()
        self.rsa.calc_phi()
        self.rsa.calc_e(self.rsa.rsa['phi'])
        self.rsa.mod_inv(self.rsa.rsa['e'], self.rsa.rsa['phi']) 
        encryption_text = self.rsa.encrypt(plaintext)
        decryption_test = self.rsa.decrypt(encryption_text)
        self.assertEqual(plaintext, decryption_test)

    def test_encry_special(self):
        """11. Test encryption special c."""
        plaintext = '!@#$'
        self.rsa.calc_p_and_q(self.rsa.prime_size)    
        self.rsa.calc_n()
        self.rsa.calc_phi()
        self.rsa.calc_e(self.rsa.rsa['phi'])
        self.rsa.mod_inv(self.rsa.rsa['e'], self.rsa.rsa['phi']) 
        encryption_text = self.rsa.encrypt(plaintext)
        decryption_test = self.rsa.decrypt(encryption_text)
        self.assertEqual(plaintext, decryption_test)

    def test_encry_alphabet2(self):
        """12. Test encryption alphabet2."""
        plaintext = 'qwert'
        self.rsa.calc_p_and_q(self.rsa.prime_size)    
        self.rsa.calc_n()
        self.rsa.calc_phi()
        self.rsa.calc_e(self.rsa.rsa['phi'])
        self.rsa.mod_inv(self.rsa.rsa['e'], self.rsa.rsa['phi']) 
        encryption_text = self.rsa.encrypt(plaintext)
        decryption_test = self.rsa.decrypt(encryption_text)
        self.assertEqual(plaintext, decryption_test)

    def test_encry_digit2(self):
        """13. Test encryption digit."""
        plaintext = '789'
        self.rsa.calc_p_and_q(self.rsa.prime_size)    
        self.rsa.calc_n()
        self.rsa.calc_phi()
        self.rsa.calc_e(self.rsa.rsa['phi'])
        self.rsa.mod_inv(self.rsa.rsa['e'], self.rsa.rsa['phi']) 
        encryption_text = self.rsa.encrypt(plaintext)
        decryption_test = self.rsa.decrypt(encryption_text)
        self.assertEqual(plaintext, decryption_test)

    def test_encry_special2(self):
        """14. Test encryption special c."""
        plaintext = '/*-+'
        self.rsa.calc_p_and_q(self.rsa.prime_size)    
        self.rsa.calc_n()
        self.rsa.calc_phi()
        self.rsa.calc_e(self.rsa.rsa['phi'])
        self.rsa.mod_inv(self.rsa.rsa['e'], self.rsa.rsa['phi']) 
        encryption_text = self.rsa.encrypt(plaintext)
        decryption_test = self.rsa.decrypt(encryption_text)
        self.assertEqual(plaintext, decryption_test)

    def test_encry_cornercase(self):
        """15. Test encryption cornercase."""
        self.rsa1 = rsa.RSA(5, 10)
        plaintext = '/*-+'
        self.rsa1.calc_p_and_q(self.rsa1.prime_size)    
        self.rsa1.calc_n()
        self.rsa1.calc_phi()
        self.rsa1.calc_e(self.rsa1.rsa['phi'])
        self.rsa1.mod_inv(self.rsa1.rsa['e'], self.rsa1.rsa['phi']) 
        self.rsa1.encrypt(plaintext)

        self.rsa2 = rsa.RSA(5, 11)
        plaintext = '/*-+'
        self.rsa2.encrypt(plaintext)
