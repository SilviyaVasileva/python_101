from fractions import Fraction

class Fractions:
    def __init__(self, nominator, denominator):
        fraction_element = Fraction(nominator, denominator)
        self.nominator = fraction_element.numerator
        self.denominator = fraction_element.denominator

    def __add__(self, other):
        x1 = self.nominator
        x2 = other.nominator
        y1 = self.denominator
        y2 = other.denominator

        x1 = x1 * y2 + x2 * y1
        y1 = y1 * y2

        fraction_element = Fraction(x1,y1)
        return Fractions(fraction_element.numerator, fraction_element.denominator)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'

    def __eq__(self, other):
        return self.nominator == other.nominator and self.denominator == other.denominator
    
    def __gt__(self, other):
        return self.nominator/self.denominator > other.nominator/other.denominator


def sorted(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor

    return arr

def main():
    pass

if __name__ == '__main__':
    main()