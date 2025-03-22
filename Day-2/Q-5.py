
class Poly:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)
        
    def __add__(self, other):
        length_difference = len(other.coefficients) - len(self.coefficients)
        self_padded = [0] * max(0, length_difference) + self.coefficients
        other_padded = [0] * max(0, -length_difference) + other.coefficients

        return Poly(*[a + b for a, b in zip(self_padded, other_padded)])

    def __str__(self):
        return f"Polynomial{tuple(self.coefficients)}"

if __name__ == "__main__":
     a = Poly(1,2,3)  
     b = Poly(1,0,1,1,2,3)
     c = a+b 
     print(c)