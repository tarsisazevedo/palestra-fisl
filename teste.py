from unittest import TestCase

from primes import primes_to
from primos_ate_2000000 import primos_ate_2000000

class PrimesTest(TestCase):
    def test_primes_to_30(self):
        self.assertEquals([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primes_to(30))

    def test_primes_to_2000000(self):
        self.assertEquals(primos_ate_2000000, primes_to(2000000))
