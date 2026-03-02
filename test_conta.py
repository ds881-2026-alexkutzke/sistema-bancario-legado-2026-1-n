import unittest
from conta import ContaBancaria

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria("Cliente Teste", 100.0)

    def test_saque_valido(self):
        sucesso = self.conta.sacar(50.0)
        self.assertTrue(sucesso)
        self.assertEqual(self.conta.obter_saldo(), 50.0)

    def test_saque_invalido_saldo_negativo(self):
        sucesso = self.conta.sacar(150.0)
        self.assertFalse(sucesso)
        self.assertEqual(self.conta.obter_saldo(), 100.0) # Saldo deve permanecer intacto

if __name__ == '__main__':
    unittest.main()
