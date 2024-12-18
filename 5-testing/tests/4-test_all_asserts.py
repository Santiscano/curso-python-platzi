import unittest

SERVER = "server_b"


class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10) # esto es igual que "assert 10 == 10"
        self.assertEqual("Hola", "Hola") # esto es igual que "assert "Hola" == "Hola"

    def test_assert_true_or_false(self):
        self.assertTrue(True) # compara si el parametro es True
        self.assertFalse(False) # compara si el parametro es False

    def test_assert_raises(self):
        with self.assertRaises(ValueError): # verifica si se lanza una excepcion de tipo ValueError en el bloque de codigo
            int("no_soy_un_numero") # si esto es un error, el test pasa de manera exitosa

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10]) # verifica si el primer parametro esta en el segundo parametro
        self.assertNotIn(5, [2, 4, 10]) # verifica si el primer parametro NO esta en el segundo parametro

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual({"first_name": "Luis", "last_name": "Martinez"}, user) # verifica si los diccionarios son iguales
        self.assertSetEqual({1, 2, 3}, {1, 2, 3}) # verifica si los sets son iguales

    @unittest.skip("Trabajo en progreso, será habilitada nuevamente") # salta el test y muestra el mensaje en el parametro
    def test_skip(self):
        self.assertEqual("hola", "chao") # en este ejemplo como aun falla, se salta el test

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor") # salta el test si la condicion es True
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure # indica que el test fallará, pero no se mostrará como error
    def test_expected_failure(self):
        self.assertEqual(100, 150)
