from service import *
class Complex:
    def __init__(self, real: int, imaginary: int):
        """
        Initialize a Complex number with real and imaginary parts.
        """
        self.__real = real
        self.__imaginary = imaginary

    @property
    def real(self):
        """
        Return the real part of the complex number.
        """
        return self.__real

    @property
    def imaginary(self):
        """
        Return the imaginary part of the complex number.
        """
        return self.__imaginary

    @property
    def __str__(self):
        """
        String representation of the complex number.
        """
        return f"{self.real} + {self.imaginary}i"


if __name__ == "__main__":
    # Example usage
    complex_number = Complex(2, 3)
    print(complex_number)
