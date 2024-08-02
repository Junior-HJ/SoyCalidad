import unittest
from main import SoyCalidad

class PruebaPregunta1(unittest.TestCase):

    soy_calidad = SoyCalidad()
    
    def test_first(self):
        
        resultado = self.soy_calidad.pregunta_1([[2, 2], [2, 2]])

        self.assertEqual(resultado, [0, 1])

    def test_second(self):
        
        resultado = self.soy_calidad.pregunta_1([[2, 1, 3], [4, 5, 2], [6, 6, 6]])

        self.assertEqual(resultado, [4, 2])

class PruebaPregunta2(unittest.TestCase):

    soy_calidad = SoyCalidad()
    
    def test_first(self):

        resultado = self.soy_calidad.pregunta_2(11)

        self.assertEqual(resultado, [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]])

if __name__ == '__main__':
    unittest.main()
