from math import gcd

class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other: 'Rational'):
        firstnum = self.numerator * other.denominator
        secondnum = other.numerator * self.denominator
        return firstnum == secondnum

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __lt__(self, other: 'Rational') -> bool:
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other: 'Rational') -> bool:
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __le__(self, other: 'Rational') -> bool:
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __ge_(self, other: 'Rational') -> bool:
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __ne__(self, other: 'Rational'):
        firstnum = self.numerator * other.denominator
        secondnum = other.numerator * self.denominator
        return firstnum != secondnum


if __name__ == '__main__':
    assert Rational(2, 4) * Rational(1, 6) == Rational(2, 24)
    assert Rational(2, 4) == Rational(4, 8)
    assert Rational(5, 9) + Rational(4, 9) == Rational(9, 9)
    assert Rational(5, 9) - Rational(4, 9) == Rational(1, 9)
    assert Rational(2, 4) != Rational(7, 8)
    assert Rational(4, 5) < Rational(9, 2)
    assert Rational(4, 5) <= Rational(8, 10)
    assert Rational(1, 4)*(Rational(3, 2)+Rational(1, 8))+Rational(156, 100) == Rational(1573, 800)


















