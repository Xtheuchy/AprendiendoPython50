#Pruebas con unittest (factorial)
import unittest

#funcion a probar
def factorial(n):
    if n ==0 or n ==1 :
        return 1
    return n * factorial(n-1)

#Clase de pruebas
class Test_factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        
    def test_factorial_uno(self):
        self.assertEqual(factorial(1), 1)
        
    def test_factorial_cinco(self):
        self.assertEqual(factorial(5), 120)
#Ejecutar pruebas

if __name__ == "__main__":
    unittest.main()
        